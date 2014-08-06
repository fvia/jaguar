#!/usr/bin/env python

""" This scripts fills information about ???

"""


"""
Loading django
"""
import os
import django

# django 1.6.5
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jaguarsite.settings")
from django.conf import settings

"""
# django 1.7
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.py")
django.setup()
"""


import datetime

""" Testing django is working
"""

from jaguar.models import LinkHistory
print LinkHistory.objects.all()


# Date of latest log added
try:
    last_link = LinkHistory.objects.latest('when')
    when_was_added_last_log = last_link.when
except:
    when_was_added_last_log = datetime.datetime(2000, 1, 1)

print "Last log added: {} ".format( when_was_added_last_log)

