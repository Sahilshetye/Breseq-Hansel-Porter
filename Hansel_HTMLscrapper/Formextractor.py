print 'formext'

import os
import sys, getopt
import RunMeta as rm
import re
import BiocontrolConnector as bc
import FormSubmition as fs
import datetime as dt


try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["ifile=", "ofile="])
except getopt.GetoptError:
    print ('''Formextractor.py -i <index.html folder path> -o <output options>  
    
             out[ut option: 1. Normal  Skokie file with  runID and Sample Id
                            2. Sekisui  Sample
                            3. Skokie Stock Type
                            4. Other  file inputs.
                            ''')

    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print ('Formextractor.py -i <index.html folder path> -o <output folder name>')
        sys.exit()
    elif opt in ("-i", "--ifile"):
        folder = str(arg)
    elif opt in ("-o", "--ofile"):
       folderopts = int(arg)


pattern= os.path.relpath(folder,'/model_systems/variant-analysis-v1/variants/')

f= rm.Runmeta()

# Add all the pattern here to match all the files types here

if (folderopts==1):

    matchobj= re.search(u"([0-9]{3,5})-([0-9]{5,6})-(.*)",pattern)
    if matchobj:
        # s=matchobj.group(1)
        f.BRunId= matchobj.group(1)
        f.RunId= matchobj.group(1)
        f.BiocontrolSampId= matchobj.group(2)
        f.FileName=matchobj.group(3)

    else:
        print 'not found'
        exit()

    biodata=bc.getRunMetaFromBiocontrol(f.BRunId,f.BiocontrolSampId)
    if(biodata[0]=="N"):
        print "Not Found IN bIOCONTROL cHECK THE CODE"
        exit()
    else:
        f.Task= biodata[4]
        f.Experiment=biodata[3]
        f.CorpObj= biodata[8]
        f.Milestone=biodata[7]
        f.RunDescription=biodata[1]
        f.SampledOn= biodata[9]
        f.InnoculatedFrom= biodata[10]
        f.Customer=biodata[6]
        f.Labbook=biodata[2]
        f.CreatedBy=biodata[11]

elif (folderopts==2):
    # matchobj = re.search(u"([A-Z]{1,3}[0-9]*)-RUN([0-9]{1,3})-D([0-9]{1,2})-(.*)", pattern)

    matchobj = re.search(u"([A-Z0-9]{1,3})-RUN([0-9]{1,3})-D([0-9]{1,2})(.*)", pattern)
    #DayRun=0 # here the  day number comes  so the in future I add that number to the  innoculated from and the SampledOn date.

    if matchobj:
        # s=matchobj.group(1)
        # DayRun=matchobj.group(3)
        f.BRunId = matchobj.group(1)+"-"+matchobj.group(2)
        f.RunId = matchobj.group(1)+"-"+ matchobj.group(2)
        f.BiocontrolSampId = "D"+matchobj.group(3)
        f.FileName = pattern
        f.RunDescription = matchobj.group(1)
        f.InnoculatedFrom = dt.datetime.today()
        f.SampledOn = (dt.datetime.today() + dt.timedelta(days=int(matchobj.group(3))))
        # print (f.SampledOn-f.InnoculatedFrom).days
        # exit()
    else:
        print 'not found'
        exit()


    f.Task = "Standard Sekisui Sample"
    f.Experiment = "Sekisui Experiment data will be inserted here."
    f.CorpObj = "Sekisui"
    f.Milestone = ""



    # here the  days  will be added.

    f.Customer = "Sekisui"
    f.Labbook = "Non Standard Labbook coming from outside  of the  Skokie Lab"
    f.CreatedBy = "Sekisui" # Adding this to  make sure the place holder for the  search type shows up with Sekisui Samples.



print 'uploading all the  Sample and Evidence files now'
# print f.BRunId,f.BiocontrolSampId,f.FileName,f.Task,f.Milestone,f.CorpObj,f.Experiment,f.RunDescription,f.CorpObj,f.SampledOn,(f.SampledOn-f.InnoculatedFrom).days
url2='http://10.10.33.20:9000/samplefiles/{fileid}/evidences'
url1='http://10.10.33.20:9000/samplefiles/uploads'
s=fs.postFileFunction(url1,folder,f)
if s!='Null':
    url=url2.replace("{fileid}",s)
    s1=fs.postEvidenceFileFunction(url,folder,f)
    print s1

else:
    c = open(folder + "/Evidence Not uploaded.txt", "w")
    c.write(" since fileid not found in the  Sample  dunction  Evidence is not uploaded.")
    c.close()


print "Done the  Entire sequece for "+f.BiocontrolSampId