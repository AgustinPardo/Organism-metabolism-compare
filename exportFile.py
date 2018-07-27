#!/usr/bin/env python2.7

import matchingName

def ExportFile (dictionary,outfile_name):
	
	name_checker=False
	if outfile_name=="pathways_groups.txt":
		name_checker=True
		match_dic=matchingName.NameIDPathwayDict()
	
	out_file=open(outfile_name,"w")
	for element1 in dictionary:
		out_file.write("#"+element1+"\n")
		out_list=list(dictionary[element1])
		for element2 in out_list:
			if name_checker == True:				
				try:
					out_file.write(element2+"\t")
					names=match_dic[element2]
					out_file.write(names+"\n")
				except:
					out_file.write(element2+"\n")
			else:
				out_file.write(element2+"\n")
