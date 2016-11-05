array =input().split()

dict={}
elements=[]
for a in array:
    if a in dict.keys():
        value=dict[a]

        dict[a]=value+1
    else:
        dict[a]=1
        elements.append(a)


 #str=''
string = " ".join(str(a)+' '+str(dict[a]) for a in elements)

#for a in elements:

print (string)


## 40 40 40 40 40 50 50 8 8 8 8 8 8 8 8 8 8 8 8 90 90 90 90 90 90 90 99 99 100 100 100

