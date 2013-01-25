#!/usr/bin/python
# demonstrate differences between functional and imperative coding
def G(n): return n+1;
def F(n): return n*n;
source_list = primes(17)

def imperative():
 target=[]
 for item in source_list:
  t1=G(item)
  t2=F(t1)
  target.append(t2)
 print target

def functional():
 compose2 = lambda F, G: lambda x: F(G(x))
 target = map(compose2(F,G), source_list)
 print target

def primes(n):
        if n==2: return [2]
        elif n<2: return []
        s=range(3,n+1,2)
        mroot = n ** 0.5
        half=(n+1)/2-1
        i=0
        m=3
        while m <= mroot:
                if s[i]:
                        j=(m*m-3)/2
                        s[j]=0
                        while j<half:
                                s[j]=0
                                j+=m
                i=i+1
                m=2*i+3
        return [2]+[x for x in s if x]

