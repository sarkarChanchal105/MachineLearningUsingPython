def nbr_of_laps(x, y):
    lcm=LCM(x,y)
    return [lcm/x, lcm/y]


def LCM(x,y):

    return ((x*y)/GCF(x,y))

def GCF(x,y):

    if y!=0:
        x,y=y,x%y
        return GCF(x,y)

    else:
        return x



A=[1,2,3,4,5,6]

B=1

for a in A:
    B=LCM(B,a)

print ("B = ",B)


#reduce(LCM,A)