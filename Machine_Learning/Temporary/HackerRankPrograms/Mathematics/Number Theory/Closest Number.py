from math import  log10,pow,log
T=int(input())
for _ in range (T):
    a,b,x=map(int,str(input()).split())
    N=0
    print(a,b,x)
    print(((b*log(a,10))-log(x,10)))
    #c= pow(10,((b*log10(a))-log10(x)))
    #print(c)
