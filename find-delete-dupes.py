#!/usr/bin/python
import os,sys

try: frontargs = sys.argv; print frontargs
except: frontargs=''
class sizesum:
	
	def __init__(self, args):
		flat = open('LSLIST','r')
		fs = open('LSLIST2','r')
		f1 = flat.readlines()
		f2 = fs.readlines()
		flat.close();fs.close()
		dupnum = 0 
		for x2 in f2:
			for y1 in f1:
				if x2.find(y1) != -1: 
					print 'dup found: ',x2,'++',y1
					dupnum += 1
		print len(f1),len(f2)	
		print dupnum,' duplicates found'
	def parseargs(self,args):
		cnt=0
		for y in args:
			#print y.find('M'), cnt
			if -1 != y.find('M'): self.add(y)
			cnt += 1
	def add(self,a):
		self.P0 += int( a.strip('M') )
if __name__ == "__main__":  s = sizesum(frontargs)
q1=0
for x in os.listdir('.'):
	if x.find('avi') != -1: 
		mb = os.path.getsize(x)
		q1+=mb
