
A='cde'
B='abc'
count=0
for a in A:
    if a in B:
        count+=1

#   print(count)

print(len(A)+len(B)-2*(count))


A=[1]

print ("A[0:3] ",A[0:3])