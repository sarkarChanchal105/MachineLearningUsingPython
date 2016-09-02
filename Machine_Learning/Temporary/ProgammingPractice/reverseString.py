



def reverseString(A):
    list1=list(A)

    print ("Before: {}".format(A))
    #for i in range (int(len(list1)/2)-1):
    for i in range (int(len(list1)/2)):
        k1=list1[i]
        k2=list1[len(list1)-i-1]
        if k1!=k2:
            list1[len(list1)-i-1]=k1
            list1[i]=k2

    #print (list1)

    A=0; A=''.join(list1)
    print ("after :",A)
    return (A)

if reverseString("abuttuba")=='abuttuba':
    print ("Yes")

