#!/usr/bin/env python2.7

def Interseccion(li1,li2):
    x=set(li1).intersection(set(li2))
    return list(x)
def Diferencias(li1,li2):
    return list(set(li1) - set(li2))

def compare_number(li1,li2):
    inter=Interseccion(li1,li2)
    inter_largo=len(inter)
    li1_largo=len(li1)-inter_largo
    li2_largo=len(li2)-inter_largo
    return {	'01':li2_largo,
				'10':li1_largo,
				'11':inter_largo
				}	
	
def compare_list(li1,name1,li2,name2):
	inter=Interseccion(li1,li2)
	li1_only=Diferencias(li1,li2)
	li2_only=Diferencias(li2,li1)
	return { name1: li1_only,
			  'Interection': inter,
			  name2: li2_only
			  }
	

