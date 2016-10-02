#https://www.hackerrank.com/challenges/handshake?h_r=next-challenge&h_v=legacy
def factorial(N):
    if N in (0,1):
        return 1
    else:
        return N*factorial(N-1)

def comb(N,K):
    val=1
    if N==1:
        return 0
    if N<K:
        return 1
    else:
        for i in range(0,K):
            val=val*(N-i)
            #print (N-i)
    #print (val)
    return int(val/(factorial(K)))

T = int(input().strip())
for a0 in range(T):
    N = int(input().strip())
    print (comb(N,2))


