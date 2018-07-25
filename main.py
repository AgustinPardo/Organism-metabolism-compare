#!/usr/bin/env python2.7

import sys

import queries
import compare
import draw

# Selecciono los PGDB's
PGDB_1=queries.PGDB_select("ECOLI")
PGDB_2=queries.PGDB_select("KP13_BIA_PABLO")

# Calculo las pathways
PGDB_1_pathways=queries.All_pathways(PGDB_1)
PGDB_2_pathways=queries.All_pathways(PGDB_2)

# Calculo las reacciones
PGDB_1_reactions=queries.All_reactions(PGDB_1)
PGDB_2_reactions=queries.All_reactions(PGDB_2)

# Comparo pathways
pathways_labels=compare.compare_number(PGDB_1_pathways,PGDB_2_pathways)
#Diagrama Pathways
draw.Draw("ECOLI","KP13","vennPathways.png",pathways_labels)

# Comparo Reacciones
reactions_labels=compare.compare_number(PGDB_1_reactions,PGDB_2_reactions)
draw.Draw("ECOLI","KP13","vennReactionss.png",reactions_labels)



