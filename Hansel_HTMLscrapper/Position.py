# -*- coding: utf-8 -*-

import re

def getPositionDetailsfromSoup(s):
    matchobj= re.search(u"(.*):([0-9]*)",s)
    if matchobj:
        s=matchobj.group(1)
    return int(s.replace(",",""))