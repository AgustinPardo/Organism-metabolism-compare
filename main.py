#!/usr/bin/env python2.7

import sys

import queries
import draw
import exportFile

lista_PGDB=sys.argv[1:]

# Calculo las pathways
PGDB_pathways={}
for PGDB in lista_PGDB:
	PGDB_pathways[PGDB]=queries.All_pathways(queries.PGDB_select(PGDB))
# Diagrama Pathways
draw.Draw(lista_PGDB,PGDB_pathways,"vennPathways.png")

elements_dict_pathways=draw.Elements(lista_PGDB,PGDB_pathways)
# Exportar a un archivo externo
exportFile.ExportFile(elements_dict_pathways,"pathways_groups.txt")

# Calculo las Reactions
PGDB_reactions={}
for PGDB in lista_PGDB:
	PGDB_reactions[PGDB]=queries.All_reactions(queries.PGDB_select(PGDB))
# Diagrama Reactions
draw.Draw(lista_PGDB,PGDB_reactions,"vennReactions.png")

elements_dict_reactions=draw.Elements(lista_PGDB,PGDB_reactions)
# Exportar a un archivo externo
exportFile.ExportFile(elements_dict_reactions,"reactions_groups.txt")

