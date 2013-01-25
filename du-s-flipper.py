#!/usr/bin/python
#flip the columns in a file with two columns sepd by \t
filename = 'sum1'
newfile = 'newsumr'
delim = '\t'
newdelim = ':'

def linspl(aline):
 l=aline.strip().split(delim)
 return l[1]+newdelim+l[0]

f=open(filename,'r')
filelines = f.readlines()
f.close()

f=open(newfile,'w')
for l in filelines:
 f.write(linspl(l)+'\n')
f.close()

