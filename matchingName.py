#!/usr/bin/env python2.7

def NameIDPathwayDict():
	entrada=open("pathway-links.dat","r")	
	lines=entrada.readlines()[3:]	
	entrada.close()
	out_dict={}
	for line in lines:
		line_splited=line.split("\t")
		line_splited_key=line_splited[0]
		line_splited_values=line_splited[1:]
		if line_splited_values[-1]=="\n":
			line_splited_values=line_splited_values[:-1]			
		line_splited_values_join=";".join(line_splited_values).rstrip("\n")
		out_dict[line_splited_key]=line_splited_values_join
	return (out_dict)
