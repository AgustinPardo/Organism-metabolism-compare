#!/usr/bin/env python2.7

import queries

def PGDB_consult():
	All_organism=queries.All_PGDB()
	for organism in All_organism:
		print(organism)
	return(0)

PGDB_consult()
