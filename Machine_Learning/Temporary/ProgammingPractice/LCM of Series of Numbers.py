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

def LCM (x,y):
    return (x*y)/gcd(x,y)

#k=LCM(array[0],array[1])
k=1
for i in range(1,20):
    k=LCM(k,array[i])

print (k)


# def argsLCM (*args):
#     return lambda a,b:
#
#print (lcm(10,22))





