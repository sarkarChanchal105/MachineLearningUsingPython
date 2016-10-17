A=[4, 9, 1, 32, 13]

A=sorted(A)

minDiff=A[1]-A[0]

for i in range(len(A)-1):
    minDiff=min(minDiff,A[i+1]-A[i])

print(minDiff)


def max_element(A):
    A=sorted(A)
    A=A[::-1]
    print(A[0])

max_element(A)