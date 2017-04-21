# -*- coding: utf-8 -*-
import re
import MySqlConnector as ms
def getMutationDetailsfromSoup(s):
    return s

def getMutationTypeDetailsfromSoup(s):
    matchobj = re.search(u"evidence/([A-Z]{3})_([0-9]+).html",s)

    if matchobj:
        return matchobj.group(1)
    else:
        return "0"


def getMutationTypeIDDetailsfromSoup(s):
    matchobj = re.search(u"evidence/([A-Z]{3})_([0-9]+).html", s)
    m=getMutationTypeDetailsfromSoup(s)

    if  m!="0":
        type=ms.getMutationTypeID(str(matchobj.group(1)))
        return type

    else:                   # Extra side case incase  patternis not matched
        return 0


#print getMutationTypeIDDetailsfromSoup("evidence/DEL_1.html")