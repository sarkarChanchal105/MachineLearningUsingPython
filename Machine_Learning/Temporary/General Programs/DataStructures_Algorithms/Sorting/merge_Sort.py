"""
Merge sort is a sorting technique based on divide and conquer technique. With worst-case time complexity being Ο(n log n), it is one of the most respected algorithms.

Merge sort first divides the array into equal halves and then combines them in a sorted manner.

"""

A=[100,2,4,5,-1,5,1000,10,90,50,90,-100,500,56,3000,-90000000000000000]
#A=[100,2,4,5]

def merge_sort(A):
    n=len(A)
    even=True
    if n%2!=0: ## if the number of elements n is odd, make it even by n-1
        n=n-1
        even=False
    swap_pair_elements(A,n)  ## Sort the consecutive pairs of elements
    if len(A)==0:
        print ("input array is empty")
        return
    if len(A)==1:
        print (A)
    if len(A)==2:
        swap_pair_elements(A,n)
        print(A)
    if len(A)>=3:  ## run the
        i=0
        B=A[:2] ## firt two elements of the array
        while (i<=n-4):
              C=A[i+2:i+4]
              B=merge_two_sorted_list(B,C)
              i=i+2
        if even==False:  ## if the number of elements is odd merge the last element of the array
            B=merge_two_sorted_list(B,A[n:])
        print(B)

### swap the pairs of numbers in the array.
### for example, [5,2,10,0,91,78] =[2,5,0,10,78,91]
def swap_pair_elements(A,n):
    i=0
    while(n>i):
        if A[i]>A[i+1]:
            f=A[i]
            A[i]=A[i+1]
            A[i+1]=f
        i+=2


def merge_two_sorted_list(A,B):
    merged=[]
    ## compare the first elements of the array A and B and merge them.
    while len(A)>0 and len(B)>0:
        if(A[0]<=B[0]):
            merged.append(A[0])
            A.pop(0)
        elif (A[0]>B[0]):
            merged.append(B[0])
            B.pop(0)
    rest=''
    ### merge the last elements of the array
    if len(A)==0:
        rest=B
    if len(B) ==0:
        rest=A
    for a in rest:
        merged.append(a)
    return (merged)

merge_sort(A)

