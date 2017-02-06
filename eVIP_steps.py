import os

list = ["5mil","10mil", "20mil", "30mil", "40mil", "50mil"]

for depth in list:
	for i in range(100):
		cmd = "python /pod/pstore/groups/brookslab/althornt/apps/eVIP/eVIP_corr.py -i /scratch/althornt/kallisto_out_"+str(depth)+"/"+str(i)+"/RNF43_eVIP_geneExp_filtered.txt --z_out /scratch/althornt/eVIP/eVIP_"+str(depth)+"/"+str(i)+"/zscore_out --sp_out /scratch/althornt/eVIP/eVIP_"+str(depth)+"/"+str(i)+"/RNF43_eVIP_spearman_rank_corr"
		os.system(cmd)
		print "corr"
		print i
		rename_some = "python /pod/pstore/groups/brookslab/althornt/RNF43/depth_test/eVIP_RNF43_rename_replicates.py"
		os.system(rename_some)

		cmd2 = "python /pod/pstore/groups/brookslab/althornt/apps/eVIP/eVIP_predict.py --sig_info /scratch/althornt/eVIP/RNF43_sig.info --ie_col 293_ie --allele_col allele -c /scratch/althornt/eVIP/controls.grp -r /scratch/althornt/eVIP/comparisons.tsv --num_reps 4 --gctx /scratch/althornt/eVIP/eVIP_"+str(depth)+"/"+str(i)+"/RNF43_eVIP_spearman_rank_corr_renamed.gct -o /scratch/althornt/eVIP/eVIP_"+str(depth)+"/"+str(i)+"/RNF43_eVIP_predict_0.05.txt --conn_thresh 0.05 --mut_wt_rep_thresh 0.05 --disting_thresh 0.05 --mut_wt_rep_rank_diff 0 --conn_null_med 0.05"
		os.system(cmd2)
		print "predict"
		print depth
		print i
