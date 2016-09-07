import sys

def find_k(array,  k1):
    sorted_array=sorted(array)
    print (sorted_array)
    i=0
    for i in range(len(sorted_array)-1):
     j=i+1
     k=len(sorted_array)-1
     while(j<k):
        #print (i,j,k)
        sum=sorted_array[i]+sorted_array[j] + sorted_array[k]
        if (sum == k1):
           return  i,j,k,sorted_array[i],sorted_array[j],sorted_array[k]
        elif(sum > k1):
            k-=1
        elif sum< k1:
           j+=1
     return "Unable to find a solution "


array=[10, 3, 7 ,-1, 18, 29, -7, 4, 2]
#print (array)

#print (find_k(array,15))

#print (tuple(range(10)))


array1=[i for i in range (1000)]
print (array1)

