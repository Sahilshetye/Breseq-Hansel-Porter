# -*- coding: utf-8 -*-

import re
import MySqlConnector as mc

def getEvidenceDetailsfromSoup(s,a="Nothing Passed",b="Nothing Passed"):

    type=mc.getEvidenceTypeID(s)
    if type==0:
        return 0
    else:
        return type


# print type(getEvidenceDetailsfromSoup("RAR","Not imp"))
# print (getEvidenceDetailsfromSoup("RAR","Not imp"))