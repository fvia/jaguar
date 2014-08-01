#!/usr/bin/env python

"""
Loading django
"""
import os
import django

#django 1.6.5
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jaguarsite.settings")
from django.conf import settings

"""
# django 1.7
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.py")
django.setup()
"""


import re
import datetime

""" Testing django is working
"""

from jaguar.models import Archive, Link, LinkHistory

print Archive.objects.all()

"""
Reading from the apache logs if finds downloads from  /links/*
stores in a database time, ip using as a key the uuid in the file name
"""

DATABASE = 'jaguar'
LOG =  '/var/log/apache2/access.log'

#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'
#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)"'
#regex = '([(\d\.)]+) - - \[(.*?)\] "GET /links/(.*?)"'

#regex = '([(\d\.)]+) - - \[(.*?)\] "GET /links/(.*?) HTTP'
#('127.0.0.1', '01/Aug/2014:10:14:01 +0100', 'lotdd-code.2a0f4cdb-813a-44d3-b29f-19d0a71b5e9b.zip')
#no volem nom del fitxer ni extensio nomes uuid

regex = '([(\d\.)]+) - - \[(.*?)\] "GET /links/(.*?)\.(.*?)\.(.*?) HTTP'
#('127.0.0.1', '01/Aug/2014:10:14:01 +0100', 'lotdd-code', '2a0f4cdb-813a-44d3-b29f-19d0a71b5e9b', 'zip')


f = open(LOG)
for line in f:

     m = re.match(regex, line)
     if m:
         print line
         print m.groups()
         print "-----"

         lh = LinkHistory()
         lh.link = Link.objects.all()[0]
         lh.when = datetime.datetime.now()
         lh.ip = m.group(1)  #"66.66.66.66"
         lh.save()

     ##else:
     #    print "---"
     #print "========================="

f.close()


print "works"
