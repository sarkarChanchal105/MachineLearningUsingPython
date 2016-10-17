"""
https://www.tutorialspoint.com/data_structures_algorithms/insertion_sort_algorithm.htm
complexity O(n**2)

"""

A=[100,2,4,5,-1,5,1000,10,90,50,90,-100,500,56]

A=[100,2,4]

print(len(A))


def insertion_sort():
    for i in range (len(A)):
        # select value to be inserted
        valueToInsert= A[i]
        holePosition=i

        #locate hole position for the element to be inserted
        while holePosition>0 and  A[holePosition-1] >valueToInsert:
            A[holePosition]=A[holePosition-1]
            holePosition=holePosition-1

        # insert the number at hole position
        A[holePosition]=valueToInsert

    print(A)

insertion_sort()