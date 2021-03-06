#!/usr/bin/python

import sys, getopt, re
import mybasic


def main(inGctFileName,minNPos,sampNamePat=('(.*)',''),geneList=[], outFileN=''):

	inFile = open(inGctFileName)
	outFile = sys.stdout
	if outFileN != '':
		outFile = open(outFileN, 'w')

	headerL = inFile.readline()[:-1].split('\t')

	for line in inFile:

		d = line[:-1].split('\t')

		if not geneList or set(d[7].split(';')+d[8].split(';')).intersection(geneList):

			(sampN,loc1,loc2,geneN1,geneN2,ftype,exon1,exon2,frame,nReads,nPos) = (d[0],d[3],d[4],d[7],d[8],d[1],d[5],d[6],d[9],d[-3],d[-1])

			if int(nPos) < minNPos:
				continue

			sampN = re.search(sampNamePat[0],sampN).group(1).replace('.','_').replace('-','_')
			
			geneN1 = ','.join(set(geneN1.split(';'))-set(['']))
			geneN2 = ','.join(set(geneN2.split(';'))-set(['']))

			outFile.write('%s%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (sampNamePat[1],sampN,loc1,loc2,geneN1,geneN2,ftype,exon1,exon2,frame,nReads,nPos))
	outFile.flush()
	outFile.close()

if __name__ == '__main__':
	optL, argL = getopt.getopt(sys.argv[1:],'i:o:',[])

	optH = mybasic.parseParam(optL)

	#if '-i' in optH and '-o' in optH:
	#	main(optH['-i'], optH['-o'])

	#main('/EQL1/NSL/RNASeq/alignment/splice_fusion_NSL36.txt',1,('[^L]?([0-9]{3})','S'))
	#main('/EQL3/TCGA/GBM/RNASeq/alignment/splice_fusion_170.txt',1,('.*(TCGA-..-....).*',''))
	#main('/EQL1/NSL/RNASeq/results/fusion/splice_fusion_NSL45.txt',1,('([0-9]{3})','S'))
	#main('/EQL2/SGI_20131031/RNASeq/results/fusion/splice_fusion_30.txt',1,('([0-9]{3}|[0-9]{1,2}[AB])','S'))
	#main('/EQL1/NSL/RNASeq/results/fusion/splice_fusion_SGI20131119_6.txt',1,('([0-9]{3}|[0-9]{1,2}[AB])','S'))
	main('/EQL1/NSL/RNASeq/results/fusion/splice_fusion_SGI20131212_6.txt',1,('([0-9]{3}|[0-9]{1,2}[AB])','S'))
