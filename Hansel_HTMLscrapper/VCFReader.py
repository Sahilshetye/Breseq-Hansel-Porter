import vcf
import subprocess
import os.path
import operator

def pathprocessorvcf(path):
    if os.path.isfile(path + '.gz') and os.path.isfile(path + '.gz.tbi'):
        if os.path.isfile(path):
             #log ths to log path
            # print "found path at " + path + " and processing the the details"
        else:
            # log error
            print "error"
            # skip the creation
            # subprocess.call(['touch',path+'.testsahil.log'])
    else:

        subprocess.call(['cp', path , path+ '.bck'])
        command = subprocess.call(['bgzip', path])
        command = subprocess.call(['tabix', '-p', 'vcf', path + '.gz'])
        subprocess.call(['cp',path + '.bck',path])
    return path+'.gz'



#file= '/data1/Test folder/data/output.vcf'

#file=pathprocessorvcf(file)
#d= vcf.Reader(open(file))
#for ds in d.fetch('LTMG3',0,4329881):
#    print ds,ds.is_snp,ds.is_indel, ds.is_transition, ds.is_deletion,ds.is_sv, ds.var_subtype, ds.affected_start,ds.affected_end,ds.POS,ds.REF,ds.is_
#    #d.fetch('LTMG3',4329880,4329886)


def getREF(dir,posi,seqid):
    try:
        file = pathprocessorvcf(dir+'/data/output.vcf')
        records = vcf.Reader(open(file))
        for ds in records.fetch(seqid, posi-1, posi):
            return str(ds.REF)
    except Exception:
        return "VCFReader error" #This is mostly because It will because of ValueError: could not create iterator for region 'loxedcatP:1-1'

def getALT(dir,posi=None,seqid='LTMG3'):
    try:
        file = pathprocessorvcf(dir+'/data/output.vcf')
        records = vcf.Reader(open(file))
        for ds in records.fetch(seqid,posi-1,posi):
            return str(reduce(operator.add, ds.ALT))
    except Exception:
        raise ValueError("VCFReader error: This is mostly because It will because of ValueError: could not create iterator for region e.g.'loxedcatP:1-1'")  #

#print((getALT('/data1/Test folder/',1,"loxed-catP")))