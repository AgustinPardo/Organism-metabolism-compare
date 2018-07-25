#!/usr/bin/env python2.7

import matplotlib
import matplotlib.pyplot as plt
import venn

import matchingName

#Diagrama Pathways
def Draw(PGDB_name1,PGDB_name2,out_name,labels):
	matplotlib.use('TkAgg')
	fig, ax = venn.venn2(labels, names=[PGDB_name1, PGDB_name2])
	fig.savefig(out_name, bbox_inches='tight')
	plt.close()
	return(0)
	
def OutFile(PGDB_name1,PGDB_name2,out_name,group_dict):	
    real_names_dict=matchingName.NameIDPathwayDict()
    out_file=open(out_name,"w")
    for group in group_dict:
        out_file.write("#"+group+"\n")
        for elem in group_dict[group]:
			try:
				real_name=real_names_dict[elem]
				out_file.write(elem+"\t"+real_name+"\n")
			except:
				out_file.write(elem+"\t"+"\n")
    out_file.close()
    return (0)
