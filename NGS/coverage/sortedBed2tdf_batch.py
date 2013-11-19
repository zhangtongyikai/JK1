#!/usr/bin/python

import sys, os, re, getopt
import mybasic


def main(inputDirN,outputDirN,pbs=False,chromsize='/data1/Sequence/ucsc_hg19/chromsizes_hg19.txt',genome='hg19'):

	inputFileNL = os.listdir(inputDirN)
	inputFileNL = filter(lambda x: re.match('.*\.sorted.bed', x),inputFileNL)
	sampNameS = set([re.match('(.*)\.sorted.bed',inputFileN).group(1) for inputFileN in inputFileNL])

#	excSampNameS = set([re.match('.*/(.*).qlog:100\.0.*',line).group(1) for line in os.popen('grep -H 100.0 %s/*.qlog' % outputDirN)])
#	sampNameS = sampNameS.difference(excSampNameS)

	sampNameL = list(sampNameS)
	sampNameL.sort()

	print 'Samples: %s (%s)' % (sampNameL,len(sampNameL))

	for sampN in sampNameL:

#		if sampN not in ['C484.TCGA-06-5411-01A-01D-1696-08.2_30nt','C484.TCGA-19-2619-01A-01D-1495-08.4_30nt']:
#			continue

		if pbs:

			os.system('echo "genomeCoverageBed -bg -i %s/%s.sorted.bed -g %s > %s/%s.bedgraph; \
				igvtools toTDF -z 3 %s/%s.bedgraph %s/%s.tdf %s" | qsub -N %s -o %s/%s.tdf.qlog -j oe' % \
				(inputDirN,sampN, chromsize, outputDirN,sampN, outputDirN,sampN, outputDirN,sampN, genome, sampN, outputDirN,sampN))

		else:

			print sampN

			os.system('(genomeCoverageBed -bg -i %s/%s.sorted.bed -g %s > %s/%s.bedgraph; \
				igvtools toTDF -z 3 %s/%s.bedgraph %s/%s.tdf %s) &> %s/%s.tdf.qlog' % \
				(inputDirN,sampN, chromsize, outputDirN,sampN, outputDirN,sampN, outputDirN,sampN, genome, outputDirN,sampN))


if __name__ == '__main__':
#	optL, argL = getopt.getopt(sys.argv[1:],'i:o:p',[])
#
#	optH = mybasic.parseParam(optL)
#
#	inputDirN = optH['-i']
#
#	if '-o' in optH:
#		outputDirN = optH['-o']
#	else:
#		outputDirN = inputDirN
#
	main(inputDirN,outputDirN,'-p' in optH)
