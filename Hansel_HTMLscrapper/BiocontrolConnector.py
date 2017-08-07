import pymssql
import yaml
import os

# Loading the config file which has the  parameter list in it
file=open(os.path.dirname(__file__)+"/config.yaml",'r')
with open("config.yaml",'r') as stream:
    try:
        # pyaml.load(stream))
        data=yaml.load(stream)
        # print(dat['password'])
    except yaml.YAMLError as exc:
        print(exc)


def getRunMetaFromBiocontrol(runid,smpid):
    conn= pymssql.connect(data['server'],data['user'],data['password'],"BIOCONTROL")
    cur= conn.cursor()
    cur.execute(""" 
use [BIOCONTROL]
 select top 1 
 r.RunID
 ,r.dsc
 ,lb.Cod
 ,e.Cod
 ,t.Name
 ,p.Name
 ,c.Name
 ,gob.Cod as  Milestone
 ,co.Cod
 ,smp.Dat as Run_From
 ,r.InoculationTime as Run_Inoc
 ,per.PerNam
 
 from Runs r
  inner join person per on per.PerID= r.PerSup
  inner join LabBooks lb on per.PerID=lb.PerID
  --join RunExperiments re on r.ExpID=re.ExpID
  inner join Experiments e on r.ExpID=e.ExpID
  inner join TaskExperiments te on te.ExpID= r.ExpID
  inner join Tasks t on t.TaskID=te.TaskID
  inner join ProjectTasks pt on pt.TaskID= t.TaskID
  inner join Projects p on p.ProjectID= pt.ProjectID
  inner join CustomerProjects cp on cp.ProjectID= p.ProjectID
  inner join Customers c on c.CustomerID=cp.CustomerID
  inner join GroupObjectiveExperiments ge on ge.ExpID=e.ExpID
  inner join GroupObjectives gob on gob.GroupObjectiveID= ge.GroupObjectiveID
  --inner join ProjectGroupObjectives pg on pg.ProjectID=p.ProjectID
  -- inner join GroupObjectives gob on gob.GroupObjectiveID= pg.GroupObjectiveID
  inner join CorpObjectiveProjects cop on cop.ProjectID=p.ProjectID
  inner join CorporateObjectives co on cop.CorpObjectiveID=co.CorporateObjectiveID
  inner join Samples smp on smp.RunId=r.runID

 where r.RunID="""+runid+""" and smp.SmpID="""+smpid)
    correct= cur.rownumber
    for row in cur:
        sqldata=row
    conn.close()
    final= cur.rowcount
    if(correct==0):
        return
    # print((sqldata))
    return sqldata




# coutn=getRunMetaFromBiocontrol(23314)
# if(coutn[0]=="N"):
#     print "Not Found"
# else:
#     print coutn[1]