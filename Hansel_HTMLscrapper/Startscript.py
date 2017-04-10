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


# file= input("Enter the path for index.html:")
# sauce= open(file,'r')
sauce= open('/data1/Test folder/output/index.html','r')
soup = bs.BeautifulSoup(sauce,'lxml')






tabl= soup.find_all('table')[1]
# skipping first table


soup= bs.BeautifulSoup(str(tabl),'lxml')

tabl1 = soup.find_all('tr')


otp=""

delimiter=";"
for tabs in tabl1:
    m = hm.HanselMutation()
    #print(tabs)
    trs = bs.BeautifulSoup(str(tabs), 'lxml')
    rows=trs.find_all('td')
    #print((rows))
    if rows.__len__()!=0:
        #This one extract desription
        soup = bs.BeautifulSoup(str(rows.pop()), 'lxml')


        m.Description= de.getDescriptionDetailsfromSoup(soup.text)
       # print(description)

####################################################################################################

        #This one extract gene
        soup = bs.BeautifulSoup(unicodej (rows.pop()), 'lxml')
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
        m.AnnotationTypeID=ann.getAnnotationType(soup.text)
        m.Annotation= soup.text    # Lets see if needed or not
        if m.AnnotationTypeID==1:
           m.AnnotationCodon1=ann.getAnnotationDetailsfromSoup(soup.text,)
           m.AnnotationCodon2=ann.getAnnotationDetailsfromSoup(soup.text,)
           m.AnnotationBracket1=ann.getAnnotationDetailsfromSoup(soup.text,1)
           m.AnnotationBracket2=ann.getAnnotationDetailsfromSoup(soup.text,2)
        elif m.AnnotationTypeID==2:
           m.AnnotationCodon1=""
           m.AnnotationCodon2=""
           m.AnnotationBracket1=ann.getAnnotationDetailsfromSoup(soup.text,1)
           m.AnnotationBracket2=ann.getAnnotationDetailsfromSoup(soup.text,2)
        elif m.AnnotationTypeID==3:
           m.AnnotationCodon1=ann.getAnnotationDetailsfromSoup(soup.text,1)
           m.AnnotationCodon2=ann.getAnnotationDetailsfromSoup(soup.text,3)
           m.AnnotationCodonPosition=ann.getAnnotationDetailsfromSoup(soup.text,2)
           m.AnnotationBracket1=ann.getAnnotationDetailsfromSoup(soup.text,4)
           m.AnnotationBracket2=ann.getAnnotationDetailsfromSoup(soup.text,5)
        else:
           m.AnnotationCodon1=""
           m.AnnotationCodon2=""
           m.AnnotationBracket1=""
           m.AnnotationBracket2=""


        #print annotation

########################################################################################################################


        #This one extract freq
        soup = bs.BeautifulSoup(unicode(rows.pop()), 'lxml')
        m.Freq = fre.getFrequencyDetailsfromSoup(soup.text)
        #print(freq)

########################################################################################################################

        #This one extract mutation
        soup = bs.BeautifulSoup(unicode(rows.pop()), 'lxml')
        m.Mutation=soup.text
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
        m.EvTypeID= ev.getEvidenceDetailsfromSoup(soup.text,soup.a['href'])
        #print evidence

        #Evidence URL
        m.EvUrl=soup.a['href']

        otp+=str(m.EvTypeID)+";"+m.Gene+";"+m.SeqId+";"+str(m.Pos)+";"+m.Mutation+";"+m.Freq+";"+str(m.AnnotationCodonPosition)+";\n"

        #= mut.getMutationTypeDetailsfromSoup(soup.a['href'])
    count=0
    '''
    for row in rows:

        #print('End of row <<<<<<<<<')

        soup= bs.BeautifulSoup(str(row),'lxml')
        if (row.a != None):
            otp += row.a['href']
            otp += str('    ')


        otp+=soup.td.text.replace(",","")
        otp+=str('  ')
        count+=1
    otp+=  str('\n')'''


#temp=otp.encode('utf8')
c = open("MYFILE.csv", "w")
print(unicode(otp))


c.write((otp).encode("utf-8"))
c.close()