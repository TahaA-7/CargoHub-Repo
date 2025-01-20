from .base import *

SECRET_KEY = os.getenv('DEPLOY_SSH_KEY')

DEBUG = False

ALLOWED_HOSTS = ['http://145.24.223.158:80']
