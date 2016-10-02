#g=lambda x:x.isdigit()
file = open('Data','r')
file_t=open('Data2','w')
for line in file:
    for e in line.split(' '):
        if (e.isdigit()):
            print (e)



k=111111111
print (k*k)



