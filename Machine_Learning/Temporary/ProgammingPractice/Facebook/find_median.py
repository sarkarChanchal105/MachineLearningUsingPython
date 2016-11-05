A=[1,100,200,400,500]
B=[5,6,7,50,3000,50000,5000000]

def sort():
    pivot_A=0; pivot_B=0
    n_A=len(A);n_B=len(B)
    result=[]
    while(pivot_A<len(A) and pivot_B<len(B)):
        a=A[pivot_A]
        b=B[pivot_B]
        if a<b:
            result.append(a)
            #A.pop(pivot_A)
            pivot_A+=1
        else:
            result.append(b)
            #B.pop(pivot_B)
            pivot_B+=1
    print ("Pivot_A :{} Pivot_B: {}".format(pivot_A,pivot_B))

    rest=[]
    if n_A> n_B:
       rest=A[pivot_A:]
    else:
        rest=B[pivot_B:]
    print (" Rest :{}".format(rest))
    for x in rest:
        result.append(x)

    return result

print(sort())
