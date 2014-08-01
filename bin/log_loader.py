#!/usr/bin/env python

import re


"""
Reading from the apache logs if finds downloads from  /links/*
stores in a database time, ip using as a key the uuid in the file name
"""

DATABASE = 'jaguar'
LOG =  '/var/log/apache2/access.log'

#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'
#regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)"'
#regex = '([(\d\.)]+) - - \[(.*?)\] "GET /links/(.*?)"'
regex = '([(\d\.)]+) - - \[(.*?)\] "GET /links/(.*?) HTTP'

f = open(LOG)


for line in f:

     m = re.match(regex, line)
     if m:
         print line
         print m.groups()
         print "-----"
     ##else:
     #    print "---"
     #print "========================="

f.close()


print "works"
