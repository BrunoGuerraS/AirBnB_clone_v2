#!/usr/bin/python3
"""
Deploying tgz file
"""

from unicodedata import name
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['35.237.96.82', '54.164.136.88']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    deploy web static with fabric
    """
    if exists(archive_path) is False:
        return False

    try:
        name = archive_path.split("/")[-1]
        no_excep = name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_excep))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(name, path, no_excep))
        run('rm /tmp/{}'.format(name))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, no_excep))
        run('rm -rf {}{}/web_static'.format(path, no_excep))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_excep))
        return True
    except Exception:
        return False
