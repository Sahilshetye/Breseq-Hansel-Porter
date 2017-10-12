import json
import requests
from requests_toolbelt import MultipartEncoder
import RunMeta as rm
import copy
import datetime as dt
import os



def postFileFunction(url, datafile,runmeta):

    f= copy.copy(runmeta)

    formsubmit= MultipartEncoder({
                                 'tabletest_bundle_api_upload_type[Filetable][filename]' : f.FileName
                                ,'tabletest_bundle_api_upload_type[Filetable][toolid][toolname]' : f.Toolname
                                ,'tabletest_bundle_api_upload_type[Filetable][seqrun]' : '1'
                                ,'tabletest_bundle_api_upload_type[Filetable][smpid]' : f.BiocontrolSampId
                                ,'tabletest_bundle_api_upload_type[Filetable][runid]' : f.BRunId
                                ,'tabletest_bundle_api_upload_type[Filetable][day]' : str((f.SampledOn-f.InnoculatedFrom).days)
                                ,'tabletest_bundle_api_upload_type[Filetable][gnmid][gnmname]': f.Genomename
                                ,'tabletest_bundle_api_upload_type[Filetable][glocoverage]': f.GloCoverage
                                ,'tabletest_bundle_api_upload_type[Filetable][expid]' : f.Experiment  #Can be removed  from here.
                                ,'tabletest_bundle_api_upload_type[RunMeta][runid]' : f.RunId
                                ,'tabletest_bundle_api_upload_type[RunMeta][rundescription]': f.RunDescription
                                ,'tabletest_bundle_api_upload_type[RunMeta][runfrom][year]': str(f.SampledOn.year)
                                ,'tabletest_bundle_api_upload_type[RunMeta][innoculatedfrom][month]' : str(f.InnoculatedFrom.month)
                                ,'tabletest_bundle_api_upload_type[RunMeta][innoculatedfrom][day]' : str(f.InnoculatedFrom.day)
                                ,'tabletest_bundle_api_upload_type[RunMeta][innoculatedfrom][year]' : str(f.InnoculatedFrom.year)
                                ,'tabletest_bundle_api_upload_type[RunMeta][runfrom][month]' : str(f.SampledOn.month)
                                ,'tabletest_bundle_api_upload_type[RunMeta][runfrom][day]' : str(f.SampledOn.day)
                                ,'tabletest_bundle_api_upload_type[RunMeta][cust]' : f.Customer
                                ,'tabletest_bundle_api_upload_type[RunMeta][corpobj]' : f.CorpObj
                                ,'tabletest_bundle_api_upload_type[RunMeta][createdby]': f.CreatedBy
                                ,'tabletest_bundle_api_upload_type[RunMeta][labbook]': f.Labbook
                                ,'tabletest_bundle_api_upload_type[RunMeta][task]' : f.Task
                                ,'tabletest_bundle_api_upload_type[RunMeta][milestone]' : f.Milestone
                                ,'tabletest_bundle_api_upload_type[RunMeta][experiment]' : f.Experiment
                                ,'tabletest_bundle_api_upload_type[Filetable][uploadFile]' :  ('filename',open(datafile+'/Hansel.csv','r'),'text/csv')

                        })

    # exit()
    r = requests.post(url,data=formsubmit,headers={'Content-Type' : formsubmit.content_type})
    # print(r.status_code)
    # print r.json()[u'data']
    if r.status_code==200 and r.json()['data']!='Null':
         return str(r.json()['data'])
    else:
        return  'Null'





def postEvidenceFileFunction(url, datafile,f):
    # exit()
    for filename in os.listdir(datafile+"/output/evidence"):
        # print filename, url
        formsubmit=MultipartEncoder({'tabletest_bundle_api_evidence_file_type[evidenceFileUpload]': (filename,open(datafile+"/output/evidence/"+filename,'r'),'application/octet-stream')})
        r = requests.post(url, data=formsubmit, headers={'Content-Type': formsubmit.content_type})
        # print(r.status_code)
        # print r.json()[u'data']
        if r.status_code == 200:
            print 'data uploaded for :'+ str(r.json()['data']['evidenceid'])
        else:
            print 'Not uploaded'




# payload=MultipartEncoder(
#     fields={ 'tabletest_bundle_api_upload_type[Filetable][filename]':'replaceparameter1',
#           'tabletest_bundle_api_upload_type[Filetable][toolid][toolname]':'replaceparameter2'
#     ,'tabletest_bundle_api_upload_type[Filetable][smpid]':'replaceparameter3'
#     ,'tabletest_bundle_api_upload_type[Filetable][runid]':'replaceparameter4'
#     ,'tabletest_bundle_api_upload_type[Filetable][day]':'replaceparameter5'
#     ,'tabletest_bundle_api_upload_type[Filetable][gnmid][gnmname]':'replaceparameter6'
#     ,'tabletest_bundle_api_upload_type[Filetable][glocoverage]':'replaceparameter7'
#     ,'tabletest_bundle_api_upload_type[RunMeta][runid]':'replaceparameter8'
#     ,'tabletest_bundle_api_upload_type[RunMeta][rundescription]':'replaceparameter9'
#     ,'tabletest_bundle_api_upload_type[RunMeta][runfrom][year]':'replaceparameter10'
#     ,'tabletest_bundle_api_upload_type[RunMeta][innoculatedfrom][month]':'replaceparameter11'
#     ,'tabletest_bundle_api_upload_type[RunMeta][innoculatedfrom][day]':'replaceparameter12'
#     ,'tabletest_bundle_api_upload_type[RunMeta][innoculatedfrom][year]':'replaceparameter13'
#     ,'tabletest_bundle_api_upload_type[RunMeta][runfrom][month]':'replaceparameter14'
#     ,'tabletest_bundle_api_upload_type[RunMeta][runfrom][day]':'replaceparameter15'
#     ,'tabletest_bundle_api_upload_type[Filetable][toolid][tooldesc]':'replaceparameter16'
#              })
#  url='http://10.10.33.20:9000/samplefiles/uploads'
# url='http://10.10.33.20:9000/samplefiles/516/evidences'
# datafile='/model_systems/variant-analysis-v1/variants/18162-262670-PureBigAngus-1'
# postEvidenceFileFunction(url,datafile,'DEL_4.html')
# reference  for the  payload

# postFunction(url,payload,temp)


