#!/usr/bin/env python
# coding=utf-8
from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = 'git@github.com:shanyongxu/blog.git'

env.user = '不能让你们知道我的用户名'

env.password = '不能让你们知道我的密码'

env.hosts = ['www.syx666.com']

env.port = '22'

def deploy():
    
    source_folder = '/home/shanyx/sites/syx666.com/blog'
    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3.4 manage.py collectstatic --noinput &&
        ../env/bin/python3.4 manage.py makemigrations &&
        ../env/bin/python3.4 manage.py migrate
        """.format(source_folder)) 
    run('restart gunicorn-www.syx666.com')
    run('service nginx restart')

