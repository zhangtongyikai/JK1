#!/usr/bin/python

import sys, getopt, math
import mybasic

def main(inNFileName, inTFileName, outFileName):

	inNFile = open(inNFileName)
	inTFile = open(inTFileName)
	outFile = open(outFileName,'w')
	
	outFile.write('chrom\tloc.start\tvalue\taf\n')

	dataH = {}

	for line in inNFile:

		dataL = line[:-1].split('\t')

		chr = dataL[0]
		start = dataL[1]
		ref = dataL[2]
		obs = dataL[3]

		nr1 = int(dataL[4])
		nr2 = int(dataL[5])

		minF = min(float(nr1)/float(nr1+nr2), float(nr2)/float(nr1+nr2))

		# heterozygous
		if minF < 0.4:
			continue

		if nr1+nr2 < 10:
			continue
	
		Naf = float(nr2)/float(nr1+nr2)
		
		dataH['%s:%s' % (chr,start)] = Naf
	
	for line in inTFile:

		dataL = line[:-1].split('\t')

		chr = dataL[0]
		start = dataL[1]

		try:
			Naf = dataH['%s:%s' % (chr,start)]
		except:
			continue

		ref = dataL[2]
		obs = dataL[3]

		tr1 = int(dataL[4])
		tr2 = int(dataL[5])
		
		if tr1+tr2 < 10:
			continue

		Taf = float(tr2)/float(tr1+tr2)

		#delta = math.fabs(Taf-0.5)
		delta = math.fabs(Taf-Naf)

		if Taf >= 0.5:
			af = Taf
		else:
			af = 1-Taf

		outFile.write('%s\t%s\t%.4f\t%.4f\n' %(chr[3:],start,delta,af))

optL, argL = getopt.getopt(sys.argv[1:],'i:t:o:',[])

optH = mybasic.parseParam(optL)

if '-i' in optH and '-o' in optH:
	main(optH['-i'],optH['-t'],optH['-o'])

