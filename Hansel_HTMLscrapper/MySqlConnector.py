import mysql.connector

def getMySQLconnection():
    # This is the local DB on my PC. Dont get any funny ideas regarding it.
    cnx = mysql.connector.connect(user='sahilshetye', password='sahilshetye',
                                  host='10.10.56.12',                                  database='info-dev', )
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
    except Exception as ex:
        return  ex





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



def getMutationTypeID(s):

    try:
        cnx= getMySQLconnection()
        crsr = cnx.cursor()
        query = ("select MutTypeID from mutation_type where MutName=\'{}\' limit 1".format(s))
        crsr.execute(query)

        i= int(crsr.fetchone()[0])
        crsr.close()
        cnx.close()
        return i
    except Exception:
        return 0

