#!/usr/bin/env python2.7

import sys

import queries
import compare
import draw

lista_PGDB=sys.argv[1:]
#~ entrada_ficti_2=["ECOLI","KP13"]
#~ entrada_ficti_3=["ECOLI","KP13","PA01"]

# Calculo las pathways
PGDB_pathways={}
for PGDB in lista_PGDB:
	PGDB_pathways[PGDB]=queries.All_pathways(queries.PGDB_select(PGDB))
# Diagrama Pathways
draw.Draw(lista_PGDB,PGDB_pathways,"vennPathways.png")
#
elements_dict=draw.Elements(lista_PGDB,PGDB_pathways)
# Exportar a un archivo externo


# Calculo las Reactions
PGDB_reactions={}
for PGDB in lista_PGDB:
	PGDB_reactions[PGDB]=queries.All_reactions(queries.PGDB_select(PGDB))
# Diagrama Reactions
draw.Draw(lista_PGDB,PGDB_reactions,"vennReactions.png")
