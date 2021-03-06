#!/usr/bin/python

import sys, os, re, getopt
import mybasic, mysetting

def cgh2seg(inDir, outDir, pbs=False):

	inFileNL = os.listdir(inDir)
	inFileNL = filter(lambda x: re.match('.*\.corr\.ngCGH', x), inFileNL)

	print 'Files: %s' % inFileNL

	sampNL = list(set([re.match('(.*)\.corr\.ngCGH', inFileN).group(1) for inFileN in inFileNL]))
	sampNL.sort()

	print 'Samples: %s' % sampNL, len(sampNL)

	for sampN in sampNL:

		print sampN

		iprefix = '%s/%s' % (inDir,sampN)
		oprefix = '%s/%s' % (outDir,sampN)
		cmd = 'Rscript %s/NGS/copynumber/cgh2seg.R %s.corr.ngCGH' % (mysetting.SRC_HOME, iprefix)
		log = '%s.corr.seg.qlog' % (oprefix)
		print cmd
		if pbs:
			os.system('echo "%s" | qsub -N %s -o %s -j oe' % (cmd, sampN, log))

		else:
			os.system('(%s) &> %s' % (cmd, log))		


if __name__ == '__main__':
	pass
#	optL, argL = getopt.getopt(sys.argv[1:],'i:o:p',[])
#
#	optH = mybasic.parseParam(optL)
#
#	main('/EQL1/NSL/exome_bam/purity/test/copynumber','/EQL1/NSL/exome_bam/purity/test/copynumber', False)
