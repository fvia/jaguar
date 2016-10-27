#!/usr/bin/env python

"""
Loading django
"""
import os

# django 1.6.5
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jaguarsite.settings")
# django 1.7
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jaguarsite.settings")
# django.setup()

import re
import datetime

from jaguar.models import Link, LinkHistory

# Date of latest log added
try:
    last_link = LinkHistory.objects.latest('when')
    when_was_added_last_log = last_link.when
except:
    when_was_added_last_log = datetime.datetime(2000, 1, 1)


# print "Last log added: {} ".format( when_was_added_last_log)

"""
Reading from the apache logs if finds downloads from  /links/*
stores in a database time, ip using as a key the uuid in the file name
"""
LOG = '/var/log/apache2/access.log'
#LOG = '/var/log/apache2/other_vhosts_access.log'

# regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'
# regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)"'
# regex = '([(\d\.)]+) - - \[(.*?)\] "GET /links/(.*?)"'

# regex = '([(\d\.)]+) - - \[(.*?)\] "GET /links/(.*?) HTTP'
# ('127.0.0.1', '01/Aug/2014:10:14:01 +0100',
#     'lotdd-code.2a0f4cdb-813a-44d3-b29f-19d0a71b5e9b.zip')
# no volem nom del fitxer ni extensio nomes uuid

# regex = '([(\d\.)]+) - - \[(.*?)\] "GET /links/(.*?)\.(.*?)\.(.*?) HTTP'
# ('127.0.0.1', '01/Aug/2014:10:14:01 +0100', 'lotdd-code',
#     '2a0f4cdb-813a-44d3-b29f-19d0a71b5e9b', 'zip')
# fails with points in the file name

regex = '([(\d\.)]+) - - \[(.*?)\] "GET /links/' \
    '.*?(........-....-....-....-............).*? HTTP'


f = open(LOG)
for line in f:

    m = re.match(regex, line)
    if m:


	print "MATCH " + line
        strdate_no_utc = m.group(2).split()[0]
        # m.group(2) '31/Jul/2014:16:16:12 +0100'
        # UTC offset gives problems
        date_no_utc = datetime.datetime.strptime(
            strdate_no_utc, "%d/%b/%Y:%H:%M:%S"
        )   # '31/Jul/2014:16:16:12 +0100'

        if when_was_added_last_log < date_no_utc:
            try:
                tmplink = Link.objects.get(uuid=m.group(3))
                lh = LinkHistory()
                print tmplink
                lh.link = tmplink
                lh.when = date_no_utc
                lh.ip = m.group(1)   # "66.66.66.66"
                lh.save()
            except:
                print "except"

f.close()
