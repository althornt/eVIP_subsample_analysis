import os
import random
from multiprocessing import Pool

list = ["20150602-117-RNF43-1-MG1956_S4_R1.fastq.gz", "20150602-117-RNF43-2-MG1956_S8_R1.fastq.gz","20150602-117-RNF43-3-MG1956_S12_R1.fastq.gz", "20150602-117-RNF43-4-MG1956_S16_R1.fastq.gz", "20150602-659-RNF43-1-MG1956_S3_R1.fastq.gz", "20150602-659-RNF43-2-MG1956_S7_R1.fastq.gz", "20150602-659-RNF43-3-MG1956_S11_R1.fastq.gz", "20150602-659-RNF43-4-MG1956_S15_R1.fastq.gz", "20150602-GFP-1-MG1956_S1_R1.fastq.gz","20150602-GFP-2-MG1956_S5_R1.fastq.gz", "20150602-GFP-3-MG1956_S9_R1.fastq.gz","20150602-GFP-4-MG1956_S13_R1.fastq.gz", "20150602-WT-RNF43-1-MG1956_S2_R1.fastq.gz","20150602-WT-RNF43-2-MG1956_S6_R1.fastq.gz", "20150602-WT-RNF43-3-MG1956_S10_R1.fastq.gz","20150602-WT-RNF43-4-MG1956_S14_R1.fastq.gz"]

for i in range(100):
	mkdir_cmd = "mkdir /pod/pstore/groups/brookslab/althornt/RNF43/fastq/subsample_5mil/"+str(i)
	os.system(mkdir_cmd)


def run(fastq):
	for i in range(100):
		cmd = "/pod/pstore/groups/brookslab/althornt/apps/seqtk/seqtk sample -s"+str(random.randint(0,500))+" "+fastq+" 10000000 > /scratch/althornt/seqtk_10mil/"+str(i)+"/"+fastq
	       	os.system(cmd)
		print "i:"
		print i
		print "fastq:"
		print fastq
	return fastq


if __name__ == '__main__':
	p = Pool(16)
	print(p.map(run, list))
