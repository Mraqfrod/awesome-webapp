



import os, re

from datetime import datetime
from fabric.api import *


env.user = 'michael'
env.sudo_user = 'root'
env.hosts = ['192.168.0.3']

db_user = 'www-data'
db_password = 'www-data'

_TAR_FILE = 'dist-awesome.tar.gz'

_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE

_REMOTE_BASE_DIR = '/srv/awesome'

def _current_path():
    return os.path.abspath('.')