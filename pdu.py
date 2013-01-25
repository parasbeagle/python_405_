from mydict import parser, dictofFunds, fundDict
class fundDict(dict):
	fulldata = []
	def __init__(self, d): 
		self.fulldata = d
		self['name']=d
		self['thing']=self.split()
	def split(self):
		s = self.fulldata
		return s

class halloween(dict):
	newfdict = dictofFunds()
	file1 = ''
	def __init__(self): 
		f = open('durep','r')
		self.file1=f.readlines()
		f.close()
		
	def qulur(self):
		for line in self.file1:
			funDurep=fundDict(line)	
			self.newfdict.addNew(funDurep)
			print self.newfdict
