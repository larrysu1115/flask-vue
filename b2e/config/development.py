DEBUG = True
LOGGER_NAME = 'dodoApp'

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/dodo'

SECRET_KEY = 'change-on-production-env'