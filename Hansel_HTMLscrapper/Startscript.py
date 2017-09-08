# -*- coding: utf-8 -*-

import bs4 as bs
import csv
import codecs
import Description as de
import Gene as gen
import Annotation as ann
import Frequency as fre
import Position as pos
import Mutation as mut
import Sequence as seq
import Evidence as ev
import sys
import HanselCSV as hm
import VCFReader as vr
import sys, getopt
import subprocess

# file= str(raw_input("Enter the path for Directory : "))
#/data1/Test folder/
#/data1/Test folder/S215658-Kahutis-1-1-11-3/
# directory='/data1/Test folder/S215658-Kahutis-1-1-11-3'
# sauce= open('/data1/Test folder/S215658-Kahutis-1-1-11-3/output/index.html','r')
try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["ifile=", "pboolean="])
except getopt.GetoptError:
    print ('Indexscript.py -i <index.html file path> -p <Post boolean to Biocontrol>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print ('Indexscript.py -i <index.html folder path> -p <post boolean>')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        file = str(arg)
    elif opt in ("-p", "--pboolean"):
        foldername = bool(arg)


######################################################## Setting Section for the File  configuration #########################################################
# File will be always set otherwise it will ext the code
directory=file

sauce= open(file+"/output/index.html",'r')

#  Count for limiting oly first 500  rows.
count=0

# Name of the  CSV File is set here
name="Hansel"

#  Delimiter Setting
delimiter=","





soup = bs.BeautifulSoup(sauce,'lxml')

# skipping first table since the breseq first table has meta data in it.
tabl= soup.find_all('table')[1]


# Converting everthing else except in
soup= bs.BeautifulSoup(str(tabl),'lxml')

tabl=None;

#  Getting list of all the Row element in the
tabl1 = soup.find_all('tr')


otp="EvtypeidFk,Evurl1,Evurl2,Ltname,Pos,MuttypeidFk,Mobj,Msub,Mutation,Coverage,AnnotationtypeidFk,Annotationcodon1,Annotationcodon2,Annotationposition," \
    "Annotationbracket1,Annotationbracket2,Annotation,Geneparameter1,Geneparameter2,Gene,Description\n"




for tabs in tabl1:

    # New Hansel Mutation instance ins created.
    m = hm.HanselMutation()


    trs = bs.BeautifulSoup(str(tabs), 'lxml')
    rows=trs.find_all('td')
    collen= rows.__len__()
    #print((rows))

    # Limiting to 500 Rows
    if rows.__len__()!=0 and count <500:
        #This one extract desription
        soup = bs.BeautifulSoup(str(rows.pop()), 'lxml')


        m.Description= de.getDescriptionDetailsfromSoup(soup.text).replace(',',';')

####################################################################################################

        #This one extract gene
        # AMke sure that this  Gene does not generate an error Exception
        soup = bs.BeautifulSoup(unicode(rows.pop()), 'lxml')
        m.Gene= gen.getGeneDetailsfromSoupFullName(soup.text)
        type=gen.getGeneDetailsType(soup.text)
        if type ==1:
            m.GeneParameter1= gen.getGeneDetailsfromSoup(soup.text,1)
            m.GeneParameter2= gen.getGeneDetailsfromSoup(soup.text,4)
        elif type ==2:
            m.GeneParameter1= gen.getGeneDetailsfromSoup(soup.text,1)
            m.GeneParameter2= ""
        else:
            m.GeneParameter1=""
            m.GeneParameter2=""
        #print(gene)

########################################################################################################################

        #This one extract annotation
        soup = bs.BeautifulSoup(str(rows.pop()), 'lxml')
        s1=soup.text.replace(u"Â","").replace(u"â","")
        m.AnnotationTypeID=ann.getAnnotationType(soup.text.replace(u"Â",""))
        print m.AnnotationTypeID, s1
        m.Annotation= soup.text    # Lets see if needed or not
        if m.AnnotationTypeID==1:
           m.AnnotationCodon1=""
           m.AnnotationCodon2=""
           m.AnnotationBracket1=ann.getAnnotationDetailsfromSoup(s1,1)
           m.AnnotationBracket2=ann.getAnnotationDetailsfromSoup(s1,2)
        elif m.AnnotationTypeID==2:
           m.AnnotationCodon1=""
           m.AnnotationCodon2=""
           m.AnnotationBracket1=ann.getAnnotationDetailsfromSoup(s1,1)
           m.AnnotationBracket2=ann.getAnnotationDetailsfromSoup(s1,2)
        elif m.AnnotationTypeID==3:
           m.AnnotationCodon1=ann.getAnnotationDetailsfromSoup(s1,1)
           m.AnnotationCodon2=ann.getAnnotationDetailsfromSoup(s1,3)
           m.AnnotationCodonPosition=ann.getAnnotationDetailsfromSoup(s1,2)
           m.AnnotationBracket1=ann.getAnnotationDetailsfromSoup(s1,4)
           m.AnnotationBracket2=ann.getAnnotationDetailsfromSoup(s1,5)
        else:
           m.AnnotationCodon1=""
           m.AnnotationCodon2=""
           m.AnnotationBracket1=""
           m.AnnotationBracket2=""


        #print annotation

########################################################################################################################

        if(collen==8):
            #This one extract freq
            soup = bs.BeautifulSoup(unicode(rows.pop()), 'lxml')
            m.Coverage = fre.getFrequencyDetailsfromSoup(soup.text)
            #print(freq)
        else:
            m.Coverage=100
########################################################################################################################

        #This one extract mutation(Only TEXT)
        soup = bs.BeautifulSoup(unicode(rows.pop()), 'lxml')
        m.Mutation=soup.text.replace(',','')
        # print m.Mutation
        #print unicode(rows.pop())

########################################################################################################################


        #This one extract position
        soup = bs.BeautifulSoup(unicode(rows.pop()), 'lxml')
        m.Pos= pos.getPositionDetailsfromSoup(soup.text)
        #print position

########################################################################################################################




        #This one extract seqid
        soup = bs.BeautifulSoup(unicode(rows.pop()), 'lxml')
        m.SeqId=seq.getSeqidDetailsfromSoup(soup.text)
        #print seqid

########################################################################################################################

        #This one extract evidence
        soup = bs.BeautifulSoup(unicode(rows.pop()), 'lxml')

        if(soup.findAll('a').__len__()==2):
            #m.EvTypeID = ev.getEvidenceDetailsfromSoup(soup.select('a')[0].text+" "+soup.select('a')[1].text,)
            m.EvUrl1=soup.select('a')[0].get('href')
            m.EvUrl2=soup.select('a')[0].get('href')
            m.EvTypeID = ev.getEvidenceDetailsfromSoup(soup.select('a')[0].text + " " + soup.select('a')[1].text,m.EvUrl1,m.EvUrl2)
        else:
            m.EvTypeID= ev.getEvidenceDetailsfromSoup(soup.text,soup.a['href'])
            m.EvUrl1 = soup.a['href']
            m.EvUrl2=""


        #This is where Mutation Extra Details will be extracted
        m.MtypeID=mut.getMutationTypeIDDetailsfromSoup(m.EvUrl1)
        # print m.SeqId.encode("utf8")
        try:
            m.MSub=vr.getREF(directory,m.Pos,m.SeqId.replace(u'\u2011',""))
            m.MObj=vr.getALT(directory,m.Pos,m.SeqId)
        except ValueError:
            m.MSub=0
            m.MObj=0
        #print evidence
        # print str(m.GeneType)
        #Evidence URL



        #print soup.findAll('a')[]


        #otp+=str(m.EvTypeID)+u","+str(+m.EvUrl1)+u","+str(m.EvUrl2)+u","+m.SeqId+u","+str(m.Pos)+u","+str(m.MtypeID)+u","+str(m.MObj)+u","+str(m.MSub)+u","+str(m.Mutation)+u","+str(m.Coverage)+u","+str(m.AnnotationTypeID)+u","+str(m.AnnotationCodon1)+u","+str(m.AnnotationCodon2)+","+str(m.AnnotationCodonPosition)+u","+str(m.AnnotationBracket1)+","+str(m.AnnotationBracket2)+","+str(m.Annotation)+","+str(m.GeneParameter1)+","+str(m.GeneParameter2)+","+str(m.Gene)+","+str(m.Description)+",\n"
        #
        otp += str(m.EvTypeID) + u","
        otp += m.EvUrl1 + u","
        otp += m.EvUrl2 + u","
        otp +=m.SeqId + u","
        otp +=str(m.Pos) + u","
        otp +=str(m.MtypeID) + u","
        otp +=str(m.MObj) + u","
        otp +=str(m.MSub) + u","
        otp +=m.Mutation+u","
        otp +=str(m.Coverage)+u","
        otp +=str(m.AnnotationTypeID)+u","
        otp +=m.AnnotationCodon1+u","
        otp +=m.AnnotationCodon2+u","
        otp +=str(m.AnnotationCodonPosition)+u","
        otp +=m.AnnotationBracket1+u","
        otp +=m.AnnotationBracket2+u","
        otp +=m.Annotation+u","
        otp +=m.GeneParameter1+u","
        otp +=m.GeneParameter2+u","
        otp +=m.Gene+u","
        otp +=m.Description+u"\n"
        #= mut.getMutationTypeDetailsfromSoup(soup.a['href'])
        #print m.MSub,m.MtypeID
        count+=1
    '''
    for row in rows:

        #print('End of row <<<<<<<<<'Om

        soup= bs.BeautifulSoup(str(row),'lxml')
        if (row.a != None):
            otp += row.a['href']
            otp += str('    ')


        otp+=soup.td.text.replace(",","")
        otp+=str('  ')
        count+=1
    otp+=  str('\n')'''


#temp=otp.encode('utf8')
c = open(directory+"/"+name+".csv", "w")
print(otp.encode("utf8").replace('Â','').replace('â',''))


c.write((otp).replace(u'\u2011',u' ').encode("utf8").replace('Â','').replace('â',''))
c.close()



# print" Starting the Form extractation script"
# cmd= 'python2.7 /data1/PycharmProjects/Hansel_extractor/Hansel_HTMLscrapper/Formextractor.py -i '+file
#
# p= subprocess.Popen(cmd,stdout=subprocess.PIPE, shell= True)
# out, error= p.communicate()
# print out



