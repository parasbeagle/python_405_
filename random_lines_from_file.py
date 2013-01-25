#!/usr/bin/python

from random import randint
from sys import argv

class randline:
	def __init__(self, fname, numlines):
		f = open(fname)
		lines = f.readlines()
		f.close()
		randoms=[]
		sizefile=len(lines)
		for q in range(0,numlines):
			r = randint(0,sizefile-1)
			randoms.append(lines[r])
		for l in randoms: print l.strip()
if __name__=="__main__": randline(argv[1],int(argv[2]))
