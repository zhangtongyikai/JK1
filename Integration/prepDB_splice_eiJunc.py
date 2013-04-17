#!/usr/bin/python

import sys, getopt, re
import mybasic


def parse(loc,juncInfo):

	rm = re.match('([^:]+):([^:]+)',loc)
	chrom, pos = rm.groups()

	h = {}

	for junc in juncInfo.split(','):

		rm = re.match('([+-])([^:]+):[^:]+:(.*)\/(.*)',junc)
		strand,geneN,exonIdx,exonTot = rm.groups()

		if strand == '+':
			locParsed = '%s%s:%s' % (strand,chrom,pos)
		else:
			locParsed = '%s%s:%s' % (strand,chrom,int(pos)+1)

		mybasic.addHash(h,(locParsed,geneN),junc)

	parseL = []

	for ((locParsed,geneN),juncL) in h.iteritems():

		maxTrans = 0

		for junc in juncL:

			rm = re.match('([+-])([^:]+):[^:]+:(.*)\/(.*)',junc)
			strand,geneN,exonIdx,exonTot = rm.groups()

			if int(exonTot) > maxTrans:
				alias = '%s/%s' % (exonIdx,exonTot)
				maxTrans = int(exonTot)

		parseL.append((locParsed,geneN,alias,','.join(juncL)))
		
	return parseL


def main(minNReads, sampNamePat=('(.*)',''), geneList=[]):

	inFile = sys.stdin

	for line in inFile:

		dataL = line[:-1].split('\t')

		(sampN,loc,juncInfo,nReads) = (dataL[0],dataL[1],dataL[2],dataL[3])

		if int(nReads) < minNReads or '_' in loc:
			continue

		sampN = re.match(sampNamePat[0],sampN).group(1)

		parseL = parse(loc,juncInfo)

		for (locParsed, geneN, alias, juncStr) in parseL:

			if not geneList or geneN in geneList:
				sys.stdout.write('%s%s\t%s\t%s\t%s\t%s\t%s\n' % (sampNamePat[1],sampN, locParsed, geneN, juncStr, alias, nReads))


optL, argL = getopt.getopt(sys.argv[1:],'i:o:',[])

optH = mybasic.parseParam(optL)

#if '-i' in optH and '-o' in optH:
#	main(optH['-i'], optH['-o'])

#main(0,('.*([0-9]{3}).*','S'),[])
main(0,('.*(TCGA-..-....).*',''),[])
