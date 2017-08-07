import mysql.connector
import yaml
import os

# file=open("config.yaml",'r')
with open(os.path.dirname(__file__)+"/config.yaml",'r') as stream:
    try:
        # pyaml.load(stream))
        data=yaml.load(stream)
        # print(dat['password'])
    except yaml.YAMLError as exc:
        print(exc)





def getMySQLconnection():
    # This is the local DB on my PC. Dont get any funny ideas regarding it.
    cnx = mysql.connector.connect(user=data['mysqluser'], password=data['mysqlpassword'],
                                  host=data['mysqlserver'], database=data['mysqldb'], )

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

# print getMutationTypeID('SNP')