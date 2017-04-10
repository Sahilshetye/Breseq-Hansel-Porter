# -*- coding: utf-8 -*-

import re
s=""
def getGeneDetailsfromSoup(s,n):
    matchob= re.search(u"(.*) (.{1}) / (.{1}) (.*?)$",s)

    if matchob:
         #print(matchob.group(1))
         #print(matchob.group(2))
         #print(matchob.group(3))
         #print(matchob.group(4))
         #return(matchob.group(2))
         return matchob.group(n)
    matchob= re.search(u"(.*) (.{1})$",s)

    if matchob:
        return(matchob.group(n))
    else:
        return s


def getGeneDetailsType(s):
    if re.search(u"(.*) (.{1}) / (.{1}) (.*?)$",s):
        return 1

    if re.search(u"(.*) (.{1})$",s):
        return 2

    else:
        return 3


def getGeneDetailsfromSoupFullName(s):
    return s
