#!/usr/bin/python
from colprint import colprint 
def download_file(url, webuser = None, webpass = None):
   request =  __urllib2.Request(url)
   if webuser:
      base64string = __base64.encodestring('%s:%s' % (webuser, webpass))[:-1]
      request.add_header("Authorization", "Basic %s" % base64string)
   htmlFile = __urllib2.urlopen(request)
   htmlData = htmlFile.read()
   htmlFile.close()
   return htmlData

def edits1(word):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	n = len(word)
	return set([word[0:i]+word[i+1:] for i in range(n)] + # deletion
	[word[0:i]+word[i+1]+word[i]+word[i+2:] for i in range(n-1)] + # transposition
	[word[0:i]+c+word[i+1:] for i in range(n) for c in alphabet] + # alteration
	[word[0:i]+c+word[i:] for i in range(n+1) for c in alphabet]) # insertion



if __name__ == "__main__":
   colprint(edits1('shawncresante'),10)