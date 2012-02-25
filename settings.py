import os, sys, urlparse

# App Settings
DEBUG = True
SECRET_KEY = 'vwuVh1sQ9/QbT_kj SOR!*;44m%@&U%~kGY'

# Database Settings
DB_HOST = 'localhost'
DB_PORT = 27017
DB_NAME = 'bcapi'

try:
    if os.environ.has_key('MONGOHQ_URL'):
        url = urlparse.urlparse(os.environ['MONGOHQ_URL'])
        print url.path.split('/')[-1]
        print url.username
        print url.password
except:
    print "Unexpected error:", sys.exc_info()