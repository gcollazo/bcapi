import os, sys
from pymongo.uri_parser import parse_uri

# App Settings
if os.environ.has_key('PRODUCTION'):
    DEBUG = False
else:
    DEBUG = True
SECRET_KEY = 'vwuVh1sQ9/QbT_kj SOR!*;44m%@&U%~kGY'

# Database Settings
DB_URI = 'mongodb://localhost:27017/bcapi'
DB_NAME = parse_uri(DB_URI)['database']

try:
    if os.environ.has_key('MONGOHQ_URL'):
        DB_URI = os.environ['MONGOHQ_URL']
        DB_NAME = parse_uri(DB_URI)['database']

except:
    print "Unexpected error:", sys.exc_info()