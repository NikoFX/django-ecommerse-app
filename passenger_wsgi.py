# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1302134/data/www/denteca.az/denteca')
sys.path.insert(1, '/var/www/u1302134/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'denteca.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()