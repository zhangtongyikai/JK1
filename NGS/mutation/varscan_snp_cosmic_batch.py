#!/usr/bin/python

import sys, os, re, getopt
import mybasic


def main(inDirName):

	inputFileNL = os.listdir(inDirName)
	inputFileNL = filter(lambda x: re.match('(.*)_noheader\.snp', x),inputFileNL)

	print 'Files: %s' % inputFileNL, len(inputFileNL)

	sampNL = list(set([re.match('(.*)_noheader\.snp',inputFileN).group(1) for inputFileN in inputFileNL]))
	sampNL.sort()

	print 'samples: %s' % sampNL

	for sampN in sampNL:

		print sampN

		os.system('python varscan_snp_cosmic.py -d %s -i %s_noheader.snp -o %s_snp_cosmic.dat -s %s' % \
			(inDirName, sampN, sampN, sampN))

optL, argL = getopt.getopt(sys.argv[1:],'i:',[])

optH = mybasic.parseParam(optL)

main('/data1/IRCR/exome_bam/mutation')