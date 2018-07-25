#!/usr/bin/env python2.7

import sys

import queries
import compare
import draw


entrada_ficti_2=["ECOLI","KP13"]
entrada_ficti_3=["ECOLI","KP13","PA01"]


# Selecciono los PGDB's
#~ PGDB_1=queries.PGDB_select("ECOLI")
#~ PGDB_2=queries.PGDB_select("KP13")

# Calculo las pathways
PGDB_pathways={}
for entrada in entrada_ficti_2:
	PGDB_pathways[entrada]=queries.All_pathways(queries.PGDB_select(entrada))

# Diagrama Pathways
draw.Draw(entrada_ficti_2,PGDB_pathways,"vennPathways2.png")

# Creo archivo con las pathways que se corresponden con el diagrama
draw.OutFile(entrada_ficti_2,PGDB_pathways,"group_pathways.txt")

