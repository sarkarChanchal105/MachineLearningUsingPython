A='ChanchalSarkar'

B=[e for e in A]
print (B)
C=[]
N=len(B)-1
print (N)

for i in range(0,N+1):
    print (i)
    C.append(B[N-i])

