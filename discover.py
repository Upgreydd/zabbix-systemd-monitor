#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import os
import re

if __name__ == '__main__':
    out = os.popen("systemctl list-units --no-pager --no-legend -t service").readlines()
    print "{\n\t\"data\":["
    for index, line in enumerate(out):
        (unit, load, active, sub, description) = re.sub(' +', ' ', line)[:-1].split(' ', 4)
        print "\t\t{ \"{#UNIT}\":\"" + unit.replace('\\','\\\\') + "\", \"{#DESCR}\":\"" + description + "\" }" + (
            "," if index < (len(out) - 1) else "")
    print "\t]\n}"
