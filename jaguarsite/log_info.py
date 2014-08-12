#!/usr/bin/env python

""" from the IP in LinkHistory,
     we update 'dns'  with reverse dns name
     and 'country' and 'city' from Geoip database
"""

# we only update LinkHistory in the last MINUTES_BACK
MINUTES_BACK = 60 * 24 * 7  # last week
# MINUTES_BACK = 60 * 24 * 2

import os
import socket
import datetime


"""
Loading django
"""
# import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jaguarsite.settings")
# django 1.6.5
from django.conf import settings
# django 1.7
# django.setup()

from django.contrib.gis.geoip import GeoIP
from jaguar.models import LinkHistory


now = datetime.datetime.now()
time_from = now - datetime.timedelta(minutes=MINUTES_BACK)
items = LinkHistory.objects.filter(when__gt=time_from)

geoip = GeoIP(path=settings.GEOIP_PATH,
              country='GeoIP.dat',
              city='GeoLiteCity.dat'
              )

for i in items:
    if not i.dns:
        i.dns = socket.gethostbyaddr(i.ip)[0]
    if not i.city:
        info = geoip.city(i.ip)
        if info and info.get("city"):
            i.city = info.get("city")
    if not i.country:
        info = geoip.city(i.ip)
        if info and info.get("country_name"):
            i.country = info.get("country_name")
    i.save()
