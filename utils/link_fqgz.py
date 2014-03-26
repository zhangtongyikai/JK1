#!/usr/bin/python

import sys, os, re

def link_fq(dirName, outDirName, filePatternL, prefix='IRCR.GBM', sid='', tag='', dType='T', sType='SS'):
	inputFilePL = os.popen('find %s -maxdepth 1 -name "*.fastq.gz"' % dirName, 'r')
	for fileP in inputFilePL:
		fileP = fileP[:-1]
		fileN = fileP.split('/')[-1]
		for filePattern in filePatternL:
			ro = re.match(filePattern, fileN)
			fileP = fileP.replace('(','\(').replace(')','\)').replace(' ','\ ')
			if ro:
				if sid == '':
					sid = ro.group(1)
				for i in range(3-len(sid)):
					sid = '0'+sid
				idx = ro.group(2).replace('(','\(').replace(')','\)')
				tail = tag
				if dType == 'S': #single-cell
					tail = tag + ro.group(1)
				outName = '%s_%s_%s%s_%s' % (prefix, sid, dType, tail, sType)
				os.system('ln -s %s %s/%s.%s.fq.gz' % (fileP, outDirName, outName, idx))


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
				if RSQ:
					os.system('ln -s %s %s/S%s_RSq.%s.fq.gz' % (fileP, outDirName,ro.group(1),ro.group(2).replace('(','\(').replace(')','\)')))
				else:
					sid = ro.group(1)
					idx = ro.group(2).replace('(','\(').replace(')','\)')
					if sid in normalL:
						os.system('ln -s %s %s/S%s_B_SS.%s.fq.gz' % (fileP, outDirName,sid,idx))
					else:
						print 'S%s_T_SS' % sid
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
#link_l('/EQL2/SGI_20131119/WXS/fastq','/EQL2/SGI_20131119/WXS/fastq/link',['([0-9]{1,2}[ABC])_[ACGT]{6}_R([12]).*.fastq.gz','.*([0-9]{3}).*_[ACGT]{6}_R([12]).fastq.gz'], normalL=['14C','8C','5C'])
##SGI 20131212 samples
#link_l('/EQL2/SGI_20131212/WXS/fastq', '/EQL2/SGI_20131212/WXS/fastq/link',['([0-9]{1,2}[ABC])_[ACGT]{6}_R([12]).*.fastq.gz','.*([0-9]{3}).*_[ACGT]{6}_R([12]).fastq.gz'], normalL=['4C','6C','208'])
#link_l('/EQL2/SGI_20131212/RNASeq/fastq', '/EQL2/SGI_20131212/RNASeq/fastq/link', ['NS[0-9]{2}([0-9]{3}).*_[ACGT]{6}_R([12]).fastq.gz','GBM[0-9]{2}([0-9]{3}).*_[ACGT]{6}_R([12]).fastq.gz'], RSQ=True)
#link_l('/EQL2/SGI_20131216/WXS/fastq','/EQL2/SGI_20131216/WXS/fastq/link',['.*([0-9]{3}).*[ACGT]{6}_R([12]).fastq.gz'])
#link_l('/EQL2/SGI_20131226/RNASeq/fastq','/EQL2/SGI_20131226/RNASeq/fastq/link',['([0-9][AB]).*_[ACGT]{6}_R([12]).fastq.gz','IRCR_GBM[0-9]{2}_([0-9]{3}).*_[ACGT]{6}_R([12]).fastq.gz','NS[0-9]{2}_([0-9]{3}).*_[ACGT]{6}_R([12]).fastq.gz'],RSQ=True)
#link_l('/EQL2/SGI_20140103/WXS/fastq','/EQL2/SGI_20140103/WXS/fastq/link',['NS[0-9]{2}_([0-9]{3}).*_[ACGT]{6}_R([12]).*.fastq.gz'])
#link_l('/EQL2/SGI_20140103/WXS/fastq','/EQL2/SGI_20140103/WXS/fastq/link',['NS[0-9]{2}_B_([0-9]{3}).*_[ACGT]{6}_R([12]).*.fastq.gz'], normalL=['796'])
#link_fq('/EQL6/SGI_20140104_singlecell/RNASeq/fastq', '/EQL6/SGI_20140104_singlecell/RNASeq/fastq/link',['GBM1_(.*)_[ACGT]{8}-[ACGT]{8}_R([12]).fastq.gz'], prefix='IRCR.GBM', sid='352', tag='1_', dType='S', sType='RSq')
#link_fq('/EQL6/SGI_20140104_singlecell/RNASeq/fastq', '/EQL6/SGI_20140104_singlecell/RNASeq/fastq/link',['GBM2_(.*)_[ACGT]{8}-[ACGT]{8}_R([12]).fastq.gz'], prefix='IRCR.GBM', sid='352', tag='2_', dType='S', sType='RSq')
#link_l('/EQL2/SGI_20140128/WXS/fastq','/EQL2/SGI_20140128/WXS/fastq/link',['.*_([0-9]{3}).*_[ACGT]{6}_R([12]).fastq.gz'], normalL=['015','386','676','723'])
#link_fq('/EQL6/SGI_20140203_singlecell/RNASeq/fastq', '/EQL6/SGI_20140203_singlecell/RNASeq/fastq/link', ['GBM363_T1_(.*)_[ACGT]{8}-[ACGT]{8}_R([12]).fastq.gz'], prefix='IRCR.GBM', sid='363', tag='M_', dType='S', sType='RSq')
#link_fq('/EQL6/SGI_20140203_singlecell/RNASeq/fastq', '/EQL6/SGI_20140203_singlecell/RNASeq/fastq/link', ['GBM363_T2_(.*)_[ACGT]{8}-[ACGT]{8}_R([12]).fastq.gz'], prefix='IRCR.GBM', sid='363', tag='D_', dType='S', sType='RSq')
#link_l('/EQL2/SGI_20140204/RNASeq/fastq', '/EQL2/SGI_20140204/RNASeq/fastq/link', ['NS04_(.*)_[ACGT]{6}_R([12])_.*.fastq.gz'], RSQ=True) ## 079
#link_fq('/EQL2/SGI_20140204/RNASeq/fastq', '/EQL2/SGI_20140204/RNASeq/fastq/link', ['NS07_(.*)T_.*_R([12])_.*.fastq.gz'], prefix='NS_GBM', tag='01', dType='C', sType='RSq')
#link_fq('/EQL2/SGI_20140204/RNASeq/fastq', '/EQL2/SGI_20140204/RNASeq/fastq/link', ['NS01_(.*)T_.*_R([12])_.*.fastq.gz'], prefix='NS_GBM', tag='01', dType='C', sType='RSq')
#link_fq('/EQL2/SGI_20140204/RNASeq/fastq', '/EQL2/SGI_20140204/RNASeq/fastq/link', ['NS08_(.*)T_.*_R([12])_.*.fastq.gz'], prefix='NS_GBM', tag='01', dType='C', sType='RSq') #559
#link_fq('/EQL2/SGI_20140204/RNASeq/fastq', '/EQL2/SGI_20140204/RNASeq/fastq/link', ['IRCR.*_(.*)T1_.*_R([12]).fastq.gz'], prefix='IRCR_GBM', tag='L', dType='T', sType='RSq') #352
#link_fq('/EQL2/SGI_20140204/RNASeq/fastq', '/EQL2/SGI_20140204/RNASeq/fastq/link', ['IRCR.*_(.*)T2_.*_R([12]).fastq.gz'], prefix='IRCR_GBM', tag='R', dType='T', sType='RSq') #352
#link_fq('/EQL2/SGI_20140204/WXS/fastq', '/EQL2/SGI_20140204/WXS/fastq/link', ['IRCR_GBM.*_(.*)T1_.*_R([12]).fastq.gz'], prefix='IRCR_GBM', tag='L', dType='T', sType='SS')
#link_fq('/EQL2/SGI_20140204/WXS/fastq', '/EQL2/SGI_20140204/WXS/fastq/link', ['IRCR_GBM.*_(.*)T2_.*_R([12]).fastq.gz'], prefix='IRCR_GBM', tag='R', dType='T', sType='SS')
#link_l('/EQL2/SGI_20140204/WXS/fastq', '/EQL2/SGI_20140204/WXS/fastq/link', ['IRCR_B_GBM.*_(.*)_[ACGT]{6}_R([12]).fastq.gz'], normalL=['352'])
#link_l('/EQL2/SGI_20140210/WXS/fastq', '/EQL2/SGI_20140210/WXS/fastq/link', ['(.{2})_[ACGT]{6}_R([12]).fastq.gz','B_NS.{2}_(.*)T_[ACGT]{6}_R([12]).fastq.gz','IRCR_B_GBM.{2}_(.*)T_[ACGT]{6}_R([12]).fastq.gz'], normalL=['320','388','470','585','783','334','335'])
#link_l('/EQL2/SGI_20140219/RNASeq/fastq','/EQL2/SGI_20140219/RNASeq/fastq/link', ['.*_([0-9]{3})[TAB]+_[ACGT]{6}_R([12]).fastq.gz'], RSQ=True)
#link_l('/EQL2/SGI_20140219/WXS/fastq','/EQL2/SGI_20140219/WXS/fastq/link', ['B_.+_(.*)T_.*_R([12]).fastq.gz'], normalL=['503','633','750'])
#link_l('/EQL2/SGI_20140219/WXS/fastq','/EQL2/SGI_20140219/WXS/fastq/link',['IRCR_GBM13_(.*)T_[ACGT]{6}_R([12]).fastq.gz','NS0._([0-9]{3}).*_[ACGT]{6}_R([12]).fastq.gz'])
#link_fq('/EQL6/RC85_LC195/fastq/SCS_RM', '/EQL6/RC85_LC195/fastq/SCS_RM/link', ['RM1(.*)_[ACGT]{8}-[ACGT]{8}_R([12]).fastq.gz'], prefix='LC', sid='195', tag='1', dType='S', sType='RSq')
#link_fq('/EQL6/RC85_LC195/fastq/SCS_RM', '/EQL6/RC85_LC195/fastq/SCS_RM/link', ['RM2(.*)_[ACGT]{8}-[ACGT]{8}_R([12]).fastq.gz'], prefix='LC', sid='195', tag='2', dType='S', sType='RSq')
#link_fq('/EQL6/RC85_LC195/fastq/SCS_RMX', '/EQL6/RC85_LC195/fastq/SCS_RMX/link', ['RMX_(.*)_[ACGT]{8}-[ACGT]{8}_R([12]).fastq.gz'], prefix='LC', sid='195', tag='X_', dType='S', sType='RSq')
link_fq('/EQL6/RC85_LC195/fastq/SCS_RX', '/EQL6/RC85_LC195/fastq/SCS_RX/link', ['RX_(.*)_[ACGT]{8}-[ACGT]{8}_R([12]).fastq.gz'], prefix='RCC', sid='085', tag='X_', dType='S', sType='RSq')
