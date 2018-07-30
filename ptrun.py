#!/usr/bin/env python2.7

# pythoncyc corre en python 2
# Para ejecutar este script debe estar abierto el Pathway-tools de la siguiente manera: ./pathway-tools -lisp -python
#"-lisp": the connection can be monitored and debugged
#"-python": conecta python con pathway-tools

import os
import sys

import threading

def pathwayTools_service(input_path):
	bashCommand  = input_path+" -lisp -python"
	os.system(bashCommand)

def worker():
	print('############################################################')

w = threading.Thread(target=worker, name='Trabajo')   
t = threading.Thread(target=pathwayTools_service("/home/agustin/pathway-tools/pathway-tools"), name='Servicio')

t.start()
w.start()


