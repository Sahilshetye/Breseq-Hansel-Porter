# -*- coding: utf-8 -*-
import re

import MySqlConnector as ms

def getAnnotationDetailsfromSoup(s,n):

    matchobj = re.search(u"intergenic \((.+)/(.+)\)$",s)

    if matchobj:
        return matchobj.group(n)

    matchobj = re.search(u"coding \((.+)/(.+) nt\)$",s)
    if matchobj:
        return matchobj.group(n)
    #else:
        #return s

    matchobj = re.search(u"([A-Z\*])([0-9]+)([A-Z\*]) \(([A-Z]{3})→([A-Z]{3})\) $",s)
    if matchobj:
        return matchobj.group(n)
    else:
        return s


def getAnnotationType(s):
    query=""
    if re.search(u"intergenic \((.+)/(.+)\)$",s):
        query="intergenic"
    elif re.search(u"coding \((.+)/(.+) nt\)$",s):
        query="coding"
    elif re.search(u"([A-Z\*])([0-9]+)([A-Z\*]) \(([A-Z]{3})→([A-Z]{3})\) $",s):
        query= "generic"
    else:
        query="fault"   ####Throw error here


    type= ms.getAnnotationType(query)
    return type
