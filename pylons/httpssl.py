#!/usr/bin/python
class a:
 def __init__(self):
   import httplib
   HOSTNAME = 'www.allianzlife.com'
   conn = httplib.HTTPSConnection(HOSTNAME)
   conn.putrequest('GET', '/')
   conn.endheaders()
   response = conn.getresponse()
   print response.read()

#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset: 3 -*-

import urllib2 as __urllib2
import base64 as __base64


#--------------------------------------------------------------
def download_file(url, webuser = None, webpass = None):
   """
   Datei aus dem Internet herunterladen
   """

   request =  __urllib2.Request(url)

   if webuser:
      base64string = __base64.encodestring('%s:%s' % (webuser, webpass))[:-1]
      request.add_header("Authorization", "Basic %s" % base64string)

   htmlFile = __urllib2.urlopen(request)
   htmlData = htmlFile.read()
   htmlFile.close()

   return htmlData


#--------------------------------------------------------------
if __name__ == "__main__":

   # Test
   #*****************************
   __url = "http://www.allianzlife.com"
   __webuser = "ervinchristen"
   __webpass = "ervin1"
   print download_file(__url, __webuser, __webpass)
   #print download_file(__url)
   #***************************** 




