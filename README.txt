eVIP Subsampling Analysis

I created a pipeline that evaluates eVIP at different simulated depths of sequencing.
At 5 different depths, I subsampled fastq files 100 different times, generated expression data with kallisto,
filtered + normalized the data, ran through the eVIP pipeline (eVIP_corr.py & eVIP_predict.py),and 
counted the final prediction call of each 100 repetitions.

Steps:

Each step performs 100 repetitions at 5 different subsampling depths

Step 1: Subsampling
  seqtk.py = subsample reads from the fastq files

Step 2: Running kallisto
  kallisto.py
    - Transcript-level quantification with kallisto
    - Creating gene-level expression from kallisto output
    - Creating a GCT file that combines individual files
    - filter + transform the data

Step 3: eVIP
  eVIP_steps.py
    - eVIP_corr.py = takes the gct file and calculates spearman rank correlation
    - eVIP_predict.py = uses algorithm to characterize mutations (LOF/GOF/COF/neutral)

Step 4: counting the results
  depth_test_counter.py = combines the 100 predictions for each mutation into one file
