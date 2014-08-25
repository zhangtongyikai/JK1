#!/usr/bin/python

import sys, os, re, getopt
import mybasic, mypipe, mysetting
from glob import glob

## SYSTEM CONFIGURATION

def main(inputFilePathL, projectN, clean=False, pbs=False, server='smc1', genome='hg19'):
	storageBase = os.path.dirname(mypipe.prepare_baseDir(projectN, mkdir=False)) + '/'
	apacheBase = storageBase

	if glob(storageBase+projectN):
		print ('File directory: already exists')
	else:
		os.system('mkdir %s/%s; \
			chmod a+w %s/%s' % (storageBase,projectN, storageBase,projectN))
		print('File directory: created')
	
	if glob(apacheBase+projectN):
		print ('Log directory: already exists')
	else:
		os.system('mkdir %s/%s; \
			chmod a+w %s/%s' % (apacheBase,projectN, apacheBase,projectN))
		print('Log directory: created')



	for inputFileP in inputFilePathL:

#		inputLogFileP = inputFileP.split('/')[:-1]
#
#		prosampNameL = list(set([re.match('.*/(.*).gsnap.qlog:Processed.*',line).group(1) for line in os.popen('grep Processed %s/*.qlog' % '/'.join(inputLogFileP))]))
		
		inputFileP2 = inputFileP[:-7] + '\*.fq.gz'
		inputFileN = inputFileP.split('/')[-1]
		sampN = inputFileN.split('.')[0]
		
#		if sampN[:8] not in prosampNameL:
#		if sampN not in ['IRCR_GBM14_436_RSq','IRCR_GBM10_038_RSq','IRCR_GBM14_410_RSq','IRCR_GBM13_210_RSq','IRCR_GBM13_287_RSq','IRCR_GBM13_292_RSq']:
		if sampN not in ['IRCR_GBM14_504_T03_RSq']:
			continue

		print sampN
		cmd = '/usr/bin/python %s/NGS/pipeline/pipe_s_rsq2mut.py -i %s -n %s -p %s -c %s -s %s -g %s' % (mysetting.SRC_HOME, inputFileP2, sampN, projectN, False, server, genome)
		if pbs:
			log = '%s/%s.Rsq_mut.qlog' % (storageBase+projectN+'/'+sampN,sampN)
			os.system('echo "%s" | qsub -N %s -o %s -j oe' % (cmd, sampN, log))
		else:
			log = '%s/%s.Rsq_mut.qlog' % (storageBase+projectN,sampN)
			os.system('(%s) 2> %s' % (cmd, log))


#main(glob('/EQL6/NSL/HW/fastq/*.1.fq.gz'), projectN='HW_MBT_047T_rsq2mut', clean=False, pbs=False, server='smc1', genome='hg19')
#main(glob('/home/ihlee/test_data/test_rsq.1.fq.gz'), projectN='test_ini_rsq2mut', clean=False, pbs=False, server='smc1', genome='hg19')
#main(glob('/EQL2/SGI_20131031/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20131031_rsq2mut', clean=False, pbs=True)
#main(glob('/home/heejin/practice/gatk/pipe_test/*.bam'), projectN='rsq_pipe_test2', clean=False, pbs=True)
#main(glob('/EQL1/NSL/RNASeq/align/splice_bam/*.bam'), projectN='RNAseq_17', clean=False, pbs=True)
#main(glob('/EQL2/SGI_20131212/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20131212_rsq2mut', clean=False, pbs=True, server='smc1', genome='hg19')
#main(glob('/EQL2/SGI_20131226/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20131226_rsq2mut', clean=False, pbs=True, server='smc1', genome='hg19')
#main(glob('/EQL2/SGI_20131212/RNASeq/fastq/link/S783*.1.fq.gz'), projectN='SGI20131212_rsq2mut', clean=False, pbs=True, server='smc1', genome='hg19')
#main(glob('/EQL2/SGI_20140204/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140204_rsq2mut', clean=False, pbs=True, server='smc1', genome='hg19')
#main(glob('/EQL2/SGI_20140219/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140219_rsq2mut', clean=False, pbs=True, server='smc1', genome='hg19')
#main(glob('/EQL6/RC85_LC195/fastq/Bulk_RSq/link/*.1.fq.gz'), projectN='JKM20140314_bulk_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
#main(glob('/EQL6/RC85_LC195/fastq/SCS_RM/link/*.1.fq.gz'), projectN='JKM20140314_SCS_RM_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
#main(glob('/EQL6/RC85_LC195/fastq/SCS_RMX/link/*.1.fq.gz'), projectN='JKM20140314_SCS_RMX_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
#main(glob('/EQL6/RC85_LC195/fastq/SCS_RX/link/*.1.fq.gz'), projectN='JKM20140314_SCS_RX_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
#main(glob('/EQL6/RC85_LC195/fastq/Bulk_RSq/link/*.1.fq.gz'), projectN='JKM20140314_bulk_mm10_rsq2mut', clean=False, pbs=True, server='smc1', genome='mm10')
#main(glob('/EQL2/SGI_20140331/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140331_rsq2mut', clean=False, pbs=True, server='smc1', genome='hg19')
#main(glob('/EQL6/SGI_20140422_singlecell/RNASeq/fastq/link/*.1.fq.gz'), projectN='SCS20140422_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
#main(glob('/EQL2/SGI_20140526/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140526_rsq2mut', clean=False, pbs=True, server='smc1', genome='hg19')
#main(glob('/EQL2/SGI_20140520/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140520_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
#main(glob('/EQL2/SGI_20140602/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140602_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
#main(glob('/EQL2/SGI_20140620/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140620_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
#main(glob('/EQL2/SGI_20140702/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140702_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
#main(glob('/EQL2/SGI_20140710/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140710_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
#main(glob('/EQL2/SGI_20140716/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140716_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
main(glob('/EQL2/SGI_20140723/RNASeq/fastq/link/*.1.fq.gz'), projectN='SGI20140723_rsq2mut', clean=False, pbs=True, server='smc2', genome='hg19')
