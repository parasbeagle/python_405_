
	def get_scorecard(self):
		url="http://online.wsj.com/fund/page/fund_scorecards.html"
		values = {'classification':'3',
			'returnTime':'Daily_Tr_1M~best',
			'submit.x':'Get Scorecard'}
		data = urllib.urlencode(values)
		req = urllib2.Request(url,data)
		print url,data
		print req.get_method()
		print req.has_data()
		response = urllib2.urlopen(req)
		the_page = response.read()
		filename = "get.html"
		f = open(filename,'w')
		f.write(the_page)
		f.close()

	def cli(self):
		req= urllib2.Request("http://localhost/origin.html")
		res= urllib2.urlopen(req)
		forms= ClientForm.ParseResponse(res)	
		res.close()
		form = forms[0]
		print form
		form.find_control("classification").get("3").selected = True
		form.find_control("returnTime").get("Daily_Tr_1M~best").selected = True
		request2 = form.click()  # urllib2.Request object
		try:
		    response2 = urllib2.urlopen(request2)
		except urllib2.HTTPError, response2:
		    pass
		f = open('get.html','w')
		for line in response2.readlines():
			f.write(line)
		response2.close()
		f.close()
