#!/usr/bin/python

import sys, os, re

def link_l(dirName,outDirName,filePatternL,tag='',RSQ=False, normalL=[]):
	inputFilePL = os.popen('find %s -maxdepth 1 -name "*.fastq.gz"' % dirName, 'r')
	for fileP in inputFilePL:
		fileP = fileP[:-1]
		fileN = fileP.split('/')[-1]
		for filePattern in filePatternL:
			ro = re.match(filePattern, fileN)
			fileP = fileP.replace('(','\(').replace(')','\)').replace(' ','\ ')
			print '[%s]' % fileP
			if ro:
				## exceptional case (437,559) in sgi_20131031
#				if ro.group(1) in ['437','559']:
#					os.system('ln -s %s %s/S%s_X_RSq.%s.fq.gz' % (fileP, outDirName,ro.group(1),ro.group(2).replace('(','\(').replace(')','\)')))
#					continue
				## exceptional case (189T1,189T2) in sgi_20131119
				if ro.group(1) in ['189']:
					continue

				if RSQ:
					os.system('ln -s %s %s/S%s_RSq.%s.fq.gz' % (fileP, outDirName,ro.group(1),ro.group(2).replace('(','\(').replace(')','\)')))
				else:
					sid = ro.group(1)
					idx = ro.group(2).replace('(','\(').replace(')','\)')
					if sid in normalL:
						os.system('ln -s %s %s/S%s_B_SS.%s.fq.gz' % (fileP, outDirName,sid,idx))
					else:
						os.system('ln -s %s %s/S%s_T_SS.%s.fq.gz' % (fileP, outDirName,sid,idx))


def link(dirName,outDirName,filePattern,tag='',RSQ=False, normalL=[]):

	inputFilePL = os.popen('find %s -maxdepth 1 -name "*.fastq.gz"' % dirName, 'r')

	for fileP in inputFilePL:

		fileP = fileP[:-1]

		fileN = fileP.split('/')[-1]
		
		ro = re.match(filePattern, fileN)

		fileP = fileP.replace('(','\(').replace(')','\)').replace(' ','\ ')

		print '[%s]' % fileP

		if ro:
			if RSQ:
				os.system('ln -s %s %s/S%s_RSq.%s.fq.gz' % (fileP, outDirName,ro.group(1),ro.group(2).replace('(','\(').replace(')','\)')))
			else:
				sid = ro.group(1)
				idx = ro.group(2).replace('(','\(').replace(')','\)')
				if sid in normalL:
					os.system('ln -s %s %s/S%s_B_SS.%s.fq.gz' % (fileP, outDirName,sid,idx))
				else:
					os.system('ln -s %s %s/S%s_T_SS.%s.fq.gz' % (fileP, outDirName,sid,idx))


#link('/data1/IRCR/CGH/raw/GBM_8paired/CGH', '/data1/IRCR/CGH/fe', '(.*Sep09).*\((.*)\).*\.txt')
#link('/data1/IRCR/CGH/raw/CGH_matched_PrimXeno', '/data1/IRCR/CGH/fe', '(US.*).([0-9]{3}).Prim\.txt')
#link('/data1/IRCR/CGH/raw/CGH_matched_PrimXeno', '/data1/IRCR/CGH/fe', '(US.*).([0-9]{3}).Prim\.txt')
#link('/data1/IRCR/CGH/raw/11th_sector/Array\ CGH/Glioblastoma\ array\ CGH', '/data1/IRCR/CGH/fe', '(.*([0-9]{3}).*).txt')

#link('/EQL1/NSL/CGH/raw/Array_CGH/CGH_SCRI', '/data1/IRCR/CGH/fe/test', '(.*)\(([0-9]{3})\)\.txt')
#link('/EQL1/NSL/CGH/raw/Array_CGH/CGH_SCRI', '/data1/IRCR/CGH/fe/test', '(.*)_([0-9]{3})\.txt')

#link('/EQL1/NSL/RNASeq/fastq', '/EQL1/NSL/RNASeq/fastq/link3', '.*(568|050|047|022|460)T.*R([12])_001\.fastq.gz')
##SGI 20131031 samples
#link_l('/EQL2/SGI_20131031/RNASeq/fastq','/EQL2/SGI_20131031/RNASeq/fastq/link',['([0-9]{1,2}[AB]).*R([12]).fastq.gz', '.*([0-9]{3})T.*R([12]).fastq.gz'], RSQ=True)
#link('/EQL2/SGI_20131031/WXS/fastq','/EQL2/SGI_20131031/WXS/fastq/link','([0-9]{1,2}C).*R([12]).fastq.gz', normalL=['10C','11C','12C','3C','7C','9C'])
##SGI 20131119 samples
#link('/EQL2/SGI_20131119/RNASeq/fastq','/EQL2/SGI_20131119/RNASeq/fastq/link','.*-([0-9]{3}).*_[ACGT]{6}_R([12]).fastq.gz',RSQ=True)
link_l('/EQL2/SGI_20131119/WXS/fastq','/EQL2/SGI_20131119/WXS/fastq/link',['([0-9]{1,2}[ABC])_[ACGT]{6}_R([12]).*.fastq.gz','.*([0-9]{3}).*_[ACGT]{6}_R([12]).fastq.gz'], normalL=['14C','8C','5C'])
