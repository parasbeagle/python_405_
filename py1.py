
class do:
    def __init__(self):
        w=48;l=3;c=0
        o=[]            
        while c<l:
            c+=1
            d=0
            while d<w:    
                o.append(d)
                print o
                d+=1
        o.reverse(); print o

if __name__=='__main__': do()

class eo:
    def __init__(self):
            self.a()
            self.b()
            pass

    def b(self):
        cnt=0;n=5;
        while n>cnt:
            self.a(20)
            cnt+=1
    def a(self,w=8):
        l=5;c=0
        o=[]            
        while c<l:
            c+=1
            d=[0,5]
            while d[0]<w:    
                o.append(d[0])
                d[0]+=1
            #print o
        o.reverse(); print o

