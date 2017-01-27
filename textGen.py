#!/usr/bin/python

import os, time

def startSession():

	dt = time.strftime("%d-%m-%y")

	tm = time.strftime("%H-%M")

	path = "./" + dt
	if not os.path.exists(path): os.makedirs(path)
	
	return (path, dt, tm)

def docMother(sN):


	n = open("docnames.txt", "r")

	print n.readline()

	namedoc = "MetaDoc"

	path =  sN[0] + "/" + namedoc +".txt" 
	f = open( path ,"w")

	f.write("Esto es una prueba" + path + "Y esta es la de ahora: "+ sN[1] + sN[2])



	f.close
	n.close


sessionNames = startSession()

docMother(sessionNames)

