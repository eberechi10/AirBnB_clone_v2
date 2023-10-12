#!/usr/bin/python3
"""script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean
"""

import os
from fabric.api import *

env.hosts = ['54.227.129.58', '54.160.124.73 ']


def do_clean(number=0):
    """ module to delete out-of-date archives.
    """
    number = 1 if int(number) == 0 else int(number)

    archives_w = sorted(os.listdir("versions"))
    [archives_w.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives_w]

    with cd("/data/web_static/releases"):
        archives_w = run("ls -tr").split()
        archives_w = [a for a in archives_w if "web_static_" in a]

        [archives_w.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives-w]
