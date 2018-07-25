#!/usr/bin/env python2.7

import sys

import queries
import compare
import draw

name1="ECOLI"
name2="KP13"

# Selecciono los PGDB's
PGDB_1=queries.PGDB_select(name1)
PGDB_2=queries.PGDB_select(name2)

# Calculo las pathways
PGDB_1_pathways=queries.All_pathways(PGDB_1)
PGDB_2_pathways=queries.All_pathways(PGDB_2)

# Calculo las reacciones
PGDB_1_reactions=queries.All_reactions(PGDB_1)
PGDB_2_reactions=queries.All_reactions(PGDB_2)

# Comparo pathways
pathways_labels=compare.compare_number(PGDB_1_pathways,PGDB_2_pathways)
# Diagrama Pathways
draw.Draw(name1,name2,"vennPathways.png",pathways_labels)
# Creo archivo con las pathways que se corresponden con el diagrama
text_dict=compare.compare_list(PGDB_1_pathways,name1,PGDB_2_pathways,name2)
draw.OutFile(PGDB_1_pathways,PGDB_2_pathways,"group_pathways.txt",text_dict)


#~ # Comparo Reacciones
#~ reactions_labels=compare.compare_number(PGDB_1_reactions,PGDB_2_reactions)
#~ # Diagrama Reacciones
#~ draw.Draw(name1,name2,"vennReactionss.png",reactions_labels)


