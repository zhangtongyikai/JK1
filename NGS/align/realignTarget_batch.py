#!/usr/bin/python

import sys, os, re, getopt
import mybasic


def main(inputDirN, outputDirN, pbs=False):

	inputFileNL = os.listdir(inputDirN)
	inputFileNL = filter(lambda x: re.match('(.*)\.dedup.bam', x),inputFileNL)
	
	print 'Files: %s' % inputFileNL

	sampNL = list(set([re.match('(.*)\.dedup.bam',inputFileN).group(1) for inputFileN in inputFileNL]))

	sampNL.sort()

	print 'Samples: %s' % sampNL, len(sampNL)

	for sampN in sampNL:

#		if sampN not in ['047T_N','047T','464T','464T_N','626T','626T_N']:
#			continue

		if pbs:

			print sampN

			os.system('echo "java -Xmx8g -jar /home/tools/GATK/GenomeAnalysisTK.jar -T RealignerTargetCreator -R /data1/Sequence/ucsc_hg19/hg19.fa -I %s/%s.RG.bam -o %s/%s_realigner_ft.intervals -known /data1/Sequence/ucsc_hg19/annot/dbsnp_135.hg19.sort.vcf" | \
				qsub -N %s -o %s/%s.qlog -j oe' % \
				(inputDirN,sampN, inputDirN,sampN, outputDirN,sampN, sampN, outputDirN,sampN))

		else:

			print sampN

			os.system('(java -Xmx8g -jar /home/tools/GATK/GenomeAnalysisTK.jar -T RealignerTargetCreator -R /data1/Sequence/ucsc_hg19/hg19.fa -I %s/%s.RG.bam -o %s/%s_realigner_ft.intervals -known /data1/Sequence/ucsc_hg19/annot/dbsnp_135.hg19.sort.vcf) 2> %s/%s.qlog' % \
				(inputDirN,sampN, inputDirN,sampN, outputDirN,sampN, outputDirN,sampN))

optL, argL = getopt.getopt(sys.argv[1:],'i:o:p:',[])

optH = mybasic.parseParam(optL)

main('/Z/NSL/RNASeq/align/splice/gatk_test', '/Z/NSL/RNASeq/align/splice/gatk_test', True)
