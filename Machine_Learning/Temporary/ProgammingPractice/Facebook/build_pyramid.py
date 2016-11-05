
string=''

for i in range(1,10):
    string=''
    for j in range(10-i):
        string+=' '
    string+=str(len(string))
    for k in range (i*2):
        string+='*'
    print ("{}{}".format(string,len(string)))


# for i in range(2,10):
#     print (i)

# for i in range(11,2,-1):
#     print (i)