#!/usr/bin/python
import os
import sys


class filelister():
	filelist=[]
	def __init__(self,whichdir='.'):
		for path, dirs, files in os.walk(whichdir):
			for f in files:
				if f.find('wma')!=-1:
					self.filelist.append(path+'/'+f)
	def getfilesindir(self,whichdir):
		dirlist = os.listdir(whichdir)
		return dirlist


class wmaconverter():
	def __init__(self):
		print 'hello!',filelist

#wmaconverter(wmafilelist)
