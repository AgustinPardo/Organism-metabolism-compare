#!/usr/bin/env python2.7

import matplotlib
import matplotlib.pyplot as plt
import venn

import matchingName

def Draw(lista_PGDB,PGDB_dict,out_name,legend):	
	labels_aux=[]

	for elemnt in lista_PGDB:
		pathways=PGDB_dict[elemnt]
		labels_aux.append(pathways)
		
	labels, elements_dict= venn.get_labels(labels_aux, fill=['number', 'logic'])
	
	matplotlib.use('TkAgg')				
	fn = getattr(venn,"venn" + str(len(lista_PGDB)))
	fig, ax = fn(labels, names=lista_PGDB,legend_check=legend)	
	fig.savefig(out_name, bbox_inches='tight')
	plt.close()	
	return(0)

def Elements(lista_PGDB,PGDB_dict):	
	labels_aux=[]
	for elemnt in lista_PGDB:
		pathways=PGDB_dict[elemnt]
		labels_aux.append(pathways)		
	labels, elements_dict = venn.get_labels(labels_aux, fill=['number', 'logic'])
	return(elements_dict)
