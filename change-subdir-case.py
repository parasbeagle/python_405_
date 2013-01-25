#! /usr/bin/python

import os
import sys
from time import sleep

def testUpper(s):
# print "testing " + s
 for x in s:
  if x.isupper() == True:
   return True
 return False

def doRename(D):
  print DIR
  print " >> will be renamed to << "
  print DIR.lower()
  print " "
  os.rename(DIR,DIR.lower())
  sleep(3)

top = sys.argv[1]
print "working on \""+top+"\" directory"
n=0
z=-1
for root, dirs, files in os.walk(top):
# for name in files:
#  print os.path.join(root,name)
 for name in dirs:
  n += 1
  DIR = os.path.join(root,name)
  if testUpper(DIR) == True: 
   doRename(DIR)
  if n == z : break
 if n == z : break

