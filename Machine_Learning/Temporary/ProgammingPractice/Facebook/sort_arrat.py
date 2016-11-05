A=[1,3,4,90,10,11,45]
print (A[2:3])

def sort(begin,end):
    B=A[begin:end]
    i=B.index(min(A))
    j=B.index(max(A))
    a=B[i]
    A[i]=A[begin]
    A[begin]=a

    a=A[j]
    A[j]=A[end]
    A[end]=a
    begin+=1
    end-=1
    if begin<end:
        return sort(begin,end,A[begin:end])


n=len(A)-1

print (sort(0,n))

