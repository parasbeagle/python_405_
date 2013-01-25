#!/usr/bin/python

infile=[]
f = open('/proc/partitions','r')
infile = f.read().split('\n')
f.close()
def total():
    SUM=0
    for line in infile:
        l = line.split(' ')
        name = l[-1]
        if name.isalpha() and name != 'name':
            size = l[-2]
            SUM += int(size)/1024
    print str(SUM), 'MB', str(SUM/1024), 'GB'
    return None

if __name__ == '__main__':
    total()
