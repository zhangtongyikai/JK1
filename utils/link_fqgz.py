#!/usr/bin/python

import sys, os, re


def link(dirName,outDirName,filePattern,tag=''):

	inputFilePL = os.popen('find %s -maxdepth 1 -name "*.fastq.gz"' % dirName, 'r')

	for fileP in inputFilePL:

		fileP = fileP[:-1]

		fileN = fileP.split('/')[-1]
		
		ro = re.match(filePattern, fileN)

		fileP = fileP.replace('(','\(').replace(')','\)').replace(' ','\ ')

		print '[%s]' % fileP

		if ro:
	#		print 'ln -s %s %s/S%s.%s.fq.gz' % (fileP, outDirName,ro.group(1),ro.group(2).replace('(','\(').replace(')','\)'))
			os.system('ln -s %s %s/S%s.%s.fq.gz' % (fileP, outDirName,ro.group(1),ro.group(2).replace('(','\(').replace(')','\)')))


#link('/data1/IRCR/CGH/raw/GBM_8paired/CGH', '/data1/IRCR/CGH/fe', '(.*Sep09).*\((.*)\).*\.txt')
#link('/data1/IRCR/CGH/raw/CGH_matched_PrimXeno', '/data1/IRCR/CGH/fe', '(US.*).([0-9]{3}).Prim\.txt')
#link('/data1/IRCR/CGH/raw/CGH_matched_PrimXeno', '/data1/IRCR/CGH/fe', '(US.*).([0-9]{3}).Prim\.txt')
#link('/data1/IRCR/CGH/raw/11th_sector/Array\ CGH/Glioblastoma\ array\ CGH', '/data1/IRCR/CGH/fe', '(.*([0-9]{3}).*).txt')

#link('/EQL1/NSL/CGH/raw/Array_CGH/CGH_SCRI', '/data1/IRCR/CGH/fe/test', '(.*)\(([0-9]{3})\)\.txt')
#link('/EQL1/NSL/CGH/raw/Array_CGH/CGH_SCRI', '/data1/IRCR/CGH/fe/test', '(.*)_([0-9]{3})\.txt')

link('/EQL1/NSL/RNASeq/fastq', '/EQL1/NSL/RNASeq/fastq/link3', '.*(568|050|047|022|460)T.*R([12])_001\.fastq.gz')
