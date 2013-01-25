import urllib
import urllib2
import cookielib
import HTMLParser

#Class used to parse HTML to be scraped.
class MyParser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.data_type = ""
	def handle_data(self, data):
		if not self.data_type:
			if data.lower() == "point balance":
				self.data_type = "balance"
			elif data.lower() == "points available to redeem":
				self.data_type = "points available to redeem"
			elif data.lower() == "pending points":
				self.data_type = "pending points"
		else:
			print "%s: %s" % (self.data_type, data)
			self.data_type = ""

#Set up email and password.
email = "yourmail@yourserver"
password = "your-password"
			
#Create empty cookie jar.
cj = cookielib.LWPCookieJar()
#Install cookie handler for urllib2.
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

#Create initial request -- This is like when you first browse to the page.  Since the cookie jar was empty, it will
#be like you initially cleared them from your browser.
#Cookies may set at this point.
request = urllib2.Request("http://www.mypoints.com", None)
f = urllib2.urlopen(request)
f.close()

#Now you have to make a request like you submitted the form on the page.  
#Notice that two hidden fields plus the email and password fields are sent to the form processing page.
data = urllib.urlencode({"action": "login", "email": email, "password" : password, "proceed" : "Sign In"})
request = urllib2.Request("https://www.mypoints.com/emp/u/login.do", data)
f = urllib2.urlopen(request)

#Read the page.
html = f.read()
f.close()

#Parse the html here (html contains the page markup). 
parser = MyParser()
parser.feed(html)
