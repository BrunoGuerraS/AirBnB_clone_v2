#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""
from datetime import datetime
from fabric.api import local

thisdate = "%Y%m%d%H%M%S"

def do_pack():
    """function generation a .tgz"""
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime(thisdate)
        namefile = "versions/web_static_{}.tgz".format(date)
        local("tar -zcvf {} web_static".format(namefile))
        return namefile
    except Exception:
        return None