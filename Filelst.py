#!/usr/bin/python
import os,sys
class gettitle:
    def __init__(self,id):
        return None
    def u(self,id):
        return id*-1
class a:
	def __init__(self):
		print sys.argv[1] , self.addSN(sys.argv[2:])
	def addSN(self,array):
		a=0.0
		for x in array:
			a+=float(x)
		return a
if __name__=="__main__":
	a()
