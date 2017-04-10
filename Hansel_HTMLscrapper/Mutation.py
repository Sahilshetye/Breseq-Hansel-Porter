# -*- coding: utf-8 -*-
import re

def getMutationDetailsfromSoup(s):
    return s

def getMutationTypeDetailsfromSoup(s):
    matchobj = re.search(u"evidence/([A-Z]{3})_([0-9]+).html",s)

    if matchobj:
        return matchobj.group(1)
    else:
        return "No type found"
