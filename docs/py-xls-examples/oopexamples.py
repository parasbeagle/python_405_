class basic(object):
	data = [] ; date = ''
	def __init__(self):
	 print 'calling basic.init'
	 self.data = [0,1,2]
	 self.date = 'now'
	def getData(self,sel):
	 print 'calling basic.getData'
	 def getdatafromurl():
	  print 'url'
	 def getdatafromfile():
	  print 'file'
	 if sel == 'url' : getdatafromurl()
	 if sel == 'file' : getdatafromfile()
class basicover(basic):
	source = ''
	def __init__(self):
	 print 'calling basicover.init'
	 super(basicover,self).__init__()
	 self.source = 'unknown'
	def getData(self,sel):
	 print 'calling basiccover.getData'
	 super(basicover, self).getData(sel)

class newFund(object):    
        def __setName(self, value):
            print "Set"
            self.__m_the_property = value
            
        def __getName(self):
            print "Get"
            return self.__m_the_property

            
        fundName = property(fget=__getName,
                               fset=__setName,
                               doc="Fund Name")

        def __GetReadOnlyProperty(self):
            return "This is a calculated value."
            
        ReadOnlyProperty = property(fget=__GetReadOnlyProperty)

