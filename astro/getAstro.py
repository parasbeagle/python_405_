#!/usr/bin/python

import BeautifulSoup
class astroParse:
	city="Cleveland"
	state="OH"
	d=[]
	printableD=[]	
	def __init__(self):
		d=self.getpage(self.city,self.state)
		m = BeautifulSoup.BeautifulSoup(''.join(d))
		for tag in m.findAll('div'):
			if tag.get('id') == 'astro_contain': self.d=tag
		f=open("out.html",'w')
		#f.write('<html><body>')
		f.write(self.d.renderContents())
		#f.write('</body></html>')
		f.close()
		self.combinewithindex()
		
	def combinewithindex(self,indexfile="index.html"):
		f = open(indexfile,'r')
		sourcelines=f.read()
		qstart=sourcelines.find('<!--')
		qstop=sourcelines.find('<!>')
		print qstart,qstop
		sec=sourcelines.split('<!--')
		print len(sec)
		b=self.d.renderContents()#+"</tbody></table>"
		print b[0:40]
		return sec
	def getpage(self,c,s):
		return self.download("http://www.wunderground.com/US/"+s+"/"+c+".html?MR=0&extendedsun=sunon")
	def download(self,someurl,suppress=True):
		from urllib2 import Request, urlopen, URLError
		req = Request(someurl)
		try:
			response = urlopen(req)
		except URLError, e:
			if hasattr(e, 'reason'):
				print 'We failed to reach a server.'
				print 'Reason: ', e.reason
				return -1
			elif hasattr(e, 'code'):
				print 'The server couldn\'t fulfill the request.'
				print 'Error code: ', e.code
				return -1
		retstr = response.readlines() #obviously, return webpage
		if not suppress: print 'downloading from '+someurl+ '('+str(len(retstr))+')'
		return retstr
q=astroParse()