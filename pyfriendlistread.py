#!/usr/bin/python
f=open('friends')
filelines = f.readlines()
f.close()

prevcatch="View Friends"
forwcatch="Add to list"
friends=[]
ind=0
for line in filelines:
    if line.find(prevcatch) != -1:
        friends.append(' '+filelines[ind-1].strip())
    if line.find(forwcatch) != -1: 
        friends.append(' '+filelines[ind+1].strip())
    ind+=1
    
print ','.join(friends)