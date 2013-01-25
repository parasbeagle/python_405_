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
  try:
    print D, " >> will be renamed to << ", D.lower()
    os.rename(os.path.join(root, D), os.path.join(root, D.lower()))
  except OSError, cm:
    if cm[0]==17:
        print D, " >> will be renamed to << ", D.lower()+'_'
        os.rename(os.path.join(root, D), os.path.join(root, D.lower())+'_')

top = sys.argv[1]
print "working on \""+top+"\" directory"

for root, dirs, files in os.walk(top, topdown=False):
 for filename in files:
  if testUpper(filename):
   doRename(filename)
 for dirname in dirs:
  if testUpper(dirname):
   doRename(dirname)
