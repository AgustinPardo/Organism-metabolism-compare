#!/usr/bin/env python2.7

import matplotlib
import matplotlib.pyplot as plt
import venn

import matchingName

#Diagrama
def Draw(PGDB,PGDB_dict,out_name):	
	labels_aux=[]
	for elemnt in PGDB:
		pathways=PGDB_dict[elemnt]
		labels_aux.append(pathways)
	labels = venn.get_labels(
	    labels_aux
        , fill=['number', 'logic'])        
	matplotlib.use('TkAgg')		
		
	fn = getattr(venn,"venn" + str(len(PGDB)))
	fig, ax = fn(labels, names=PGDB)	
	fig.savefig(out_name, bbox_inches='tight')
	plt.close()	

	return(0)
	
def OutFile(PGDB,PGDB_dict,out_name):
    return (0)
