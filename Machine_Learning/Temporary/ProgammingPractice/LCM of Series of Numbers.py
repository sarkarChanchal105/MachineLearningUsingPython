# n=1
#
# while 1 :
#
#     for i in range(2,10):
#         if n % i != 0 :
#             n +=1
#             break
#     if i==10:
#         print (n)
#         exit(0)

array = [i for i in range(1,21)]
def gcd (x,y):
    while y!=0:
        x,y = y,x%y
    return x

def gcd1 (x,y):
    if y!=0:
        x,y = y,x%y
        return gcd1(x,y)
    else:
        return x

print ("GCD 1",gcd1(10,20))

def LCM (x,y):
    return (x*y)/gcd(x,y)

#k=LCM(array[0],array[1])
k=1
for i in range(1,3):
    k=LCM(k,array[i])

print (k)
from functools import reduce
print ("After reduction ",reduce(LCM, array) )

# def argsLCM (*args):
#     return lambda a,b:
#
#print (lcm(10,22))




## Calculate sume of 100

C = [39.2, 36.5, 37.3, 38, 37.8]
F= list(map((lambda x: x**2),C))
print (F)
F= list((map((lambda x: x**2),C)))





#reduce()




