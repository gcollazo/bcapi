import os, sys
from pymongo.uri_parser import parse_uri


# App Settings
if os.environ.has_key('PRODUCTION') and os.environ['PUSHER_URL'] == True:
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


# Pusher settings
PUSHER_APP_ID = '16040'
PUSHER_KEY = '876e906b6f97c7b5a246'
PUSHER_SECRET = '6de5712d3026ecf037be'

try:
    if os.environ.has_key('PUSHER_URL'):
        url = urlparse.urlparse(os.environ['PUSHER_URL'])
        PUSHER_APP_ID = url.path.split('/')[-1]
        PUSHER_KEY = url.username
        PUSHER_SECRET = url.password
        print PUSHER_APP_ID
        print PUSHER_KEY
        print PUSHER_SECRET
except:
    print "Unexpected error:", sys.exc_info()
