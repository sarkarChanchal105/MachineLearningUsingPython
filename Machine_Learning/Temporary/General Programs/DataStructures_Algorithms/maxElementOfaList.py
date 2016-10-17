# A =[1,4,5,6,76,100,-567,90]
#
# print(max(A))
# median=-9999
#
# A= sorted(A)
# print (A)
# if len(A)%2 ==0:
#     first=int(len(A)/2)
#     second=first+1
#     median= (A[first-1]+A[second-1])/2
#
# else:
#     first=int(len(A)/2)
#     median=(A[first-1])
#
# print (median)
#
#
# #### First non recurring element
#
# A=[1,1,1,5,2,1,5,9,10,11,90,100,2,100]
# previous=''
# array=[]
#
# for i in range(len(A)):
#
#     if A[i] not in list(set(A[0:i-1])| set(A[i+1:])):
#         print(A[i])

#### most recurring element in list

A=[1,1,1,5,2,1,5,9,10,11,90,100,2,100]
sorted_A= sorted(A)
dict={}
j=0
count=0
previous_c=0
position=0
i=0
last_max_count=0
recurring=''
while position<len(A):

    i=position
    count=0
    for j in range(len(A[position:])):
        a=A[position+j]
        if (a==A[position+i]):
            count+=1
        i+=1

    if last_max_count < count:
        last_max_count=count
        recurring=A[position]

    position=position+count

print ("Hello ",recurring,last_max_count)