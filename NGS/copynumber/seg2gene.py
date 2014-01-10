#!/usr/bin/python

import sys, getopt, math
import mybasic, mygenome

def main(inSegFileName, inRefFlatFileName, outFileName, geneNameL, assembly='hg19'):

	
	if geneNameL == []:
		geneNameL = list(set([line.split('\t')[0] for line in open(inRefFlatFileName)]))
		geneNameL.sort()

	inSegFileMem = [line[:-1].split('\t') for line in open(inSegFileName) if line[:-1].split('\t')[0] != 'ID']

	sIdL = list(set([tokL[0] for tokL in inSegFileMem]))
	sIdL.sort()

	outFile = open(outFileName, 'w')
	
	for geneName in geneNameL:
		
		print geneName

		try:
			trans = mygenome.transcript(geneName,inRefFlatFileName,assembly)
		except:
			continue

		h = {}

		for sId in sIdL:
			h[sId] = 0.

		for tokL in inSegFileMem:

			(sId,chrNum,chrSta,chrEnd,numMarker,value) = tokL

			if chrNum != trans.chrNum or value in ('NA','null','NULL'):
				continue

			overlap = trans.cdsOverlap((chrNum,int(chrSta),int(chrEnd)))

			if overlap > 0:
				h[sId] += overlap/float(trans.cdsLen) * float(value)

		outFile.write('%s' % geneName)
		
		for sId in sIdL:
			outFile.write('\t%s' % h[sId])

		outFile.write('\n')


optL, argL = getopt.getopt(sys.argv[1:],'i:r:o:g:a:',[])

optH = mybasic.parseParam(optL)

if '-i' in optH and '-o' in optH:

	if '-g' in optH:
		geneNameL = geneNames.split(',')
	else:
		geneNameL = [] 

	main(optH['-i'],optH['-r'],optH['-o'],geneNameL,optH['-a'])
