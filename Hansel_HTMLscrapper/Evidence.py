# -*- coding: utf-8 -*-

import re
import MySqlConnector as mc

def getEvidenceDetailsfromSoup(s,a):
    type=mc.getEvidenceTypeID(s)
    if type==0:
        return 0
    else:
        return type


#print type(getEvidenceDetailsfromSoup("RA","Not imp"))