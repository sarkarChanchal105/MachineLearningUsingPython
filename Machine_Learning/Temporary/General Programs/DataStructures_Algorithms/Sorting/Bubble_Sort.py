# https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm

## For every pair of two elements check which one is greater. if First is greater than seconds then swap position.
# At least one value moves to the end in each iteration.
## the complexity of the program is O(n**2)

A=[100,2,4,5,-1,5,1000,10,90,50,90,-100,500,56]



def bubble():
    for j in range(len(A)):
        swapped=False
        for i in range(len(A)-j-1):
            if A[i]>A[i+1]:
                 f=A[i]
                 A[i]=A[i+1]
                 A[i+1]=f
                 swapped=True
        print(A,swapped)


def r_bubble(j):
    swapped=False
    for i in range(len(A)-j-1):
            if A[i]>A[i+1]:
                 f=A[i]
                 s=A[i+1]
                 A[i]=s
                 A[i+1]=f
                 swapped=True
    print(A, swapped)
    j=j+1
    if  swapped:
        return r_bubble(j)
    else:
        print(A)

#bubble()

print ("#############")
r_bubble(0)

A=[100,2,4,5,-1,5,1000,10,90,50,90,-100,500,56]
print ("#############")
bubble()
