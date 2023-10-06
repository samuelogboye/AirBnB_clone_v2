#!/usr/bin/python3
"""
A fabric script that generates a .tgz archive from the web_static folder,
ready to be uploaded to the servers.
"""

from fabric.api import local
from time import strftime


def do_pack():
    """
    do_pack function that generates a .tgz archive from the web_static folder,
    ready to be uploaded to the servers.
    """
    date = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "versions/web_static_{}.tgz".format(date)
    except Exception as e:
        return None
