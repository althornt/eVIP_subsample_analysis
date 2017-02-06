dict = {str('20150602-117-RNF43-1-MG1956_S4_R1.fastq.gz'): str('RNF43_117fs_1'),
        str('20150602-117-RNF43-2-MG1956_S8_R1.fastq.gz'): str('RNF43_117fs_2'),
        str('20150602-117-RNF43-3-MG1956_S12_R1.fastq.gz'): str('RNF43_117fs_3'),
        str('20150602-117-RNF43-4-MG1956_S16_R1.fastq.gz'): str('RNF43_117fs_4'),
        str('20150602-659-RNF43-1-MG1956_S3_R1.fastq.gz'): str('RNF43_659fs_1'),
        str('20150602-659-RNF43-2-MG1956_S7_R1.fastq.gz'): str('RNF43_659fs_2'),
        str('20150602-659-RNF43-3-MG1956_S11_R1.fastq.gz'): str('RNF43_659fs_3'),
        str('20150602-659-RNF43-4-MG1956_S15_R1.fastq.gz'): str('RNF43_659fs_4'),
        str('20150602-GFP-1-MG1956_S1_R1.fastq.gz'):str('GFP_1'),
        str('20150602-GFP-2-MG1956_S5_R1.fastq.gz'):str('GFP_2'),
        str('20150602-GFP-3-MG1956_S9_R1.fastq.gz'):str('GFP_3'),
        str('20150602-GFP-4-MG1956_S13_R1.fastq.gz'): str('GFP_4'),
        str('20150602-WT-RNF43-1-MG1956_S2_R1.fastq.gz'):str('RNF43_WT_1'),
        str('20150602-WT-RNF43-2-MG1956_S6_R1.fastq.gz'):str('RNF43_WT_2'),
        str('20150602-WT-RNF43-3-MG1956_S10_R1.fastq.gz'):str('RNF43_WT_3'),
        str('20150602-WT-RNF43-4-MG1956_S14_R1.fastq.gz'):str('RNF43_WT_4') }


list = ["5mil","10mil","20mil","30mil","40mil","50mil"]

for depth in list:
    for i in range(100):
        f1 = open("/scratch/althornt/eVIP/eVIP_"+str(depth)+"/"+str(i)+"/RNF43_eVIP_spearman_rank_corr.gct", 'r')
        f2 = open("/scratch/althornt/eVIP/eVIP_"+str(depth)+"/"+str(i)+"/RNF43_eVIP_spearman_rank_corr_renamed.gct", 'w')
        header_list= ["id","RNF43_117fs_1","RNF43_117fs_2","RNF43_117fs_3","RNF43_117fs_4","RNF43_659fs_1","RNF43_659fs_2","RNF43_659fs_3","RNF43_659fs_4","GFP_1","GFP_2","GFP_3","GFP_4","RNF43_WT_1","RNF43_WT_2","RNF43_WT_3","RNF43_WT_4"]
        f2.write("#1.3" + "\n" + "16" + "\t" + "16" + "\t" + "0" + "\t" + "0" + "\n" + "\t".join(header_list) + "\n")
        offset = 0
        for line in f1:
            if offset > 2:
                x = line.split()[0]
                y =  dict[line.split("\t")[0]]
                this_line= line.rstrip().split("\t")
                this_line[0]= dict[this_line[0]]
                print this_line
                f2.write(("\t".join(this_line)+"\n"))
            offset += 1

        f1.close()
        f2.close()
