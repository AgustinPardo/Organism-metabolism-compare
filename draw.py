#!/usr/bin/env python2.7

import matplotlib
import matplotlib.pyplot as plt
import venn

#Diagrama Pathways
def Draw(PGDB_name1,PGDB_name2,out_name,labels):
	matplotlib.use('TkAgg')
	fig, ax = venn.venn2(labels, names=[PGDB_name1, PGDB_name2])
	fig.savefig(out_name, bbox_inches='tight')
	plt.close()
