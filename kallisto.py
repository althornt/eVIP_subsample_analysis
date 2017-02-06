import os
from multiprocessing import Pool

#must be in the subsample directory

list = ["20150602-117-RNF43-1-MG1956_S4_R1.fastq.gz", "20150602-117-RNF43-2-MG1956_S8_R1.fastq.gz","20150602-117-RNF43-3-MG1956_S12_R1.fastq.gz", "20150602-117-RNF43-4-MG1956_S16_R1.fastq.gz", "20150602-659-RNF43-1-MG1956_S3_R1.fastq.gz", "20150602-659-RNF43-2-MG1956_S7_R1.fastq.gz", "20150602-659-RNF43-3-MG1956_S11_R1.fastq.gz", "20150602-659-RNF43-4-MG1956_S15_R1.fastq.gz", "20150602-GFP-1-MG1956_S1_R1.fastq.gz","20150602-GFP-2-MG1956_S5_R1.fastq.gz", "20150602-GFP-3-MG1956_S9_R1.fastq.gz","20150602-GFP-4-MG1956_S13_R1.fastq.gz", "20150602-WT-RNF43-1-MG1956_S2_R1.fastq.gz","20150602-WT-RNF43-2-MG1956_S6_R1.fastq.gz", "20150602-WT-RNF43-3-MG1956_S10_R1.fastq.gz","20150602-WT-RNF43-4-MG1956_S14_R1.fastq.gz"]
list2 = ["117-RNF43-1", "117-RNF43-2","117-RNF43-3", "117-RNF43-4", "659-RNF43-1", "659-RNF43-2", "659-RNF43-3", "659-RNF43-4", "GFP-1","GFP-2", "GFP-3","GFP-4", "WT-RNF43-1","WT-RNF43-2", "WT-RNF43-3","WT-RNF43-4"]

#Transcript-level quantification with kallisto
def run(fastq):
	for i in range(100):
		cmd1 = "/pod/pstore/groups/brookslab/bin/kallisto/cur/kallisto quant -i /pod/pstore/groups/brookslab/reference_indices/gencode.v24.transcripts.kallisto.idx --single -l 200 -s 20 -t 16 -o /scratch/althornt/kalisto_out_5mil/"+str(i)+"/"+fastq+" /scratch/althornt/seqtk_5mil/"+str(i)+"/"+fastq
		os.system(cmd1)
		print i
	return fastq


#Creating gene-level expression from kallisto output
def run(fastq):
       for i in range(100):
		cmd2 = "python /pod/home/anbrooks/bin/makeGeneTPM.py -i  /scratch/althornt/kalisto_out_5mil/"+str(i)+"/"+fastq+"/abundance.tsv -o  /scratch/althornt/kalisto_out_5mil/"+str(i)+"/"+fastq+"/abundance_gene_level.tsv"
       	os.system(cmd2)
		print i
        #delete the fastq files
		os.system("rm /scratch/althornt/kalisto_out_5mil/"+str(i)+"/"+fastq+"/abundance.h5")
		os.system("rm /scratch/althornt/kalisto_out_5mil/"+str(i)+"/"+fastq+"/run_info.json")
		print "deleted:"
		print i
	return fastq

#Creating a GCT file from individual files

short_list = ["5","6","7"]

for i in list:
	cmd3 = "python /pod/pstore/groups/brookslab/althornt/RNF43/depth_test/createTable_edit.py -s /pod/pstore/groups/brookslab/althornt/RNF43/depth_test/sample_file.tsv --in_dir /scratch/althornt/kallisto_out_5mil/"+str(i)+" --file_suffix abundance_gene_level.tsv --has_header --key_col 1 --val_col 2 --val_type float --output_table /scratch/althornt/kallisto_out_5mil/"+str(i)+"/RNF43_eVIP_geneExp.txt"
      	os.system(cmd3)
	print "gct"
	print i
	#filter + transform
        cmd4 = "python /pod/home/anbrooks/broad_bin/filterGeneExpressionTable.py --in_table /scratch/althornt/kallisto_out_5mil/"+str(i)+"/RNF43_eVIP_geneExp.txt --out_table /scratch/althornt/kallisto_out_5mil/"+str(i)+"/RNF43_eVIP_geneExp_filtered.txt -l --min_fpkm 1 --min_fold_fpkm 1"
        os.system(cmd4)
	print i
	print "filtered"


if __name__ == '__main__':
       p = Pool(16)
       print(p.map(run, list))
