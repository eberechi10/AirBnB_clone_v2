#!/usr/bin/python3
"""script (based on the file 2-do_deploy_web_static.py)
an archive to your web servers, using the function deploy
"""
import os.path
from fabric.api import local
from fabric.api import put
from fabric.api import run
from datetime import datetime
from fabric.api import env

env.hosts = ['54.227.129.58', '54.160.124.73']


def do_pack():
    """archive of the directory web_static."""

    dati = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dati.year,
                                                         dati.month,
                                                         dati.day,
                                                         dati.hour,
                                                         dati.minute,
                                                         dati.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_p):
    """ module to distributes an archive to a web server.
    Args:
        archive_p: path of the archive.
    Returns:
        If the file doesn't exist at archive_p or error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_p) is False:
        return False
    file = archive_p.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_p, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """distributes archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
