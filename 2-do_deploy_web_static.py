#!/usr/bin/python3
"""script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy
"""
from fabric.api import *
from datetime import datetime

from os import path


env.hosts = ['54.227.129.58', '54.160.124.73']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'


def do_deploy(archive_path):
        """deploy the web files to server """
        try:
                if not (path.exists(archive_p)):
                        return False

                put(archive_p, '/tmp/')

                timestamp = archive_p[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timestamp))

                run('sudo rm -rf /data/web_static/current')

                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False
        return True
