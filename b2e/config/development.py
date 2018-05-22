DEBUG = True
LOGGER_NAME = 'dodoApp'

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/dodo'

SECRET_KEY = 'change-on-production-env'

SECURITY_PASSWORD_SALT = 'askme'
# use simple crypt in dev mode.
SECURITY_HASHING_SCHEMES = 'des_crypt'
SECURITY_PASSWORD_HASH = 'des_crypt'
SECURITY_DEPRECATED_HASHING_SCHEMES = []
# for token to work
WTF_CSRF_ENABLED = False
