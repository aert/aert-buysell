from os.path import join
from fabric.api import *
from fabric.contrib.project import rsync_project

here = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')
BASE = '/opt/aert/bee3'
SRC_DIR = join(BASE, 'sources')
ENV_DIR = join(BASE, 'env')


@task
def publish():
    send()
    install()
    restart()

@task
def send():
    my_local_dir = './'
    my_remote_dir = SRC_DIR

    rsync_project(local_dir=my_local_dir, remote_dir=my_remote_dir,
                  delete=True)

@task
def install():
    cmd = 'source %s/bin/activate && ' \
          'cd %s && ' \
          'pip install -e .' % (ENV_DIR, SRC_DIR)
    sudo(cmd)


@task
def restart():
    cmd = 'source %s/bin/activate && ' \
          'cd %s && chown -R www-data:www-data . && ' \
          'supervisorctl restart bee3' % (ENV_DIR, BASE)
    sudo(cmd)


@task
def h_remote():
  "use aert.fr"
  env.user = 'root'
  env.hosts = ['aert.fr:7022']

