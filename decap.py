#!/usr/bin/python
import re, os
#still not working proper
prefix = 'wsj-data'	
re1 = re.compile(prefix+'-(\d)-(\d)-.*')
re2 = re.compile(prefix+'-(\d)-(\d+).*')
re3 = re.compile(prefix+'-(\d+)-(\d)-.*')
for fname in os.listdir(os.getcwd()):
    newname=fname.lower()
    newname2 = re1.search(newname)
    newname3 = re2.search(newname)
    newname4 = re3.search(newname)
    if newname2: 
     newname2= prefix+'-0'+newname2.group(1)+'-0'+newname2.group(2)+'-07.csv'
    elif newname3: newname2= prefix+'-0'+newname3.group(1)+'-'+newname3.group(2)+'-07.csv'
    elif newname4: newname2= prefix+'-'+newname4.group(1)+'-0'+newname4.group(2)+'-07.csv'
    print fname, '->',newname2
    if newname2: os.rename(fname, newname2)
#     allowed_name = re.compile(rxin).match
#     if allowed_name(fname):
#         # newfname = string.lower(re.sub(foo,
#                                    # '', fname))
#         # b = (newname + str(a))
#         a += 1
#         c = os.path.splitext(fname)
#         b = (newname + str(a) + c[1])
#         os.rename(fname, b)