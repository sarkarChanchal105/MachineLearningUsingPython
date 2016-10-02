#https://www.hackerrank.com/challenges/fibonacci-finding-easy


def Matrix_Multi(A,B):
    result=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j]=result[i][j]+A[i][k]*B[k][j]

    return (result)


T = int(input())



for a0 in range(T):
    result=[[1,0],[0,1]]
    D=[[0,1],[1,1]] ## Initialize the Matrix.
    A,B,N = map(int,input().split())
    while N:
        if (N%2)==1:
            result=Matrix_Multi(result,D)
        D=Matrix_Multi(D,D)
        N//=2

    print((result[0][0]*A+result[0][1]*B) % 1000000007)



