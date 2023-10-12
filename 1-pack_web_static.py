#!/usr/bin/python3
"""script that generates a .tgz archive from the contents of the web_static"""

from fabric.api import local
from time import strftime

from datetime import date


def do_pack():
    """ script to generate archive content of web_static """
    filename_s = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename_s))

        return "versions/web_static_{}.tgz".format(filename_s)

    except Exception as e:
        return None
