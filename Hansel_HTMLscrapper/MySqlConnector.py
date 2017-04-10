import mysql.connector

def getMySQLconnection():
    # This is the local DB on my PC. Dont get any funny ideas regarding it.
    cnx = mysql.connector.connect(user='sahilshetye', password='sahilshetye',
                                  host='',
                                  database='info_dev', )
    return cnx

def getAnnotationType(s):

    try:
        cnx= getMySQLconnection()
        crsr = cnx.cursor()
        query = ("select AnnotationTypeID from annotation_type where AnnotationName=\'{}\' limit 1".format(s))
        crsr.execute(query)

        i= int(crsr.fetchone()[0])
        crsr.close()
        cnx.close()
        return i
    except Exception:
        return 0





def getEvidenceTypeID(s):

    try:
        cnx= getMySQLconnection()
        crsr = cnx.cursor()
        query = ("select EvTypeID from evidence_type where EvName=\'{}\' limit 1".format(s))
        crsr.execute(query)

        i= int(crsr.fetchone()[0])
        crsr.close()
        cnx.close()
        return i
    except Exception:
        return 0
