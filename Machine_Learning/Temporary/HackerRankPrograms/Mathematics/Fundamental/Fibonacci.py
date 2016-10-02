A=[[1,1],[1,0]]
B=[[1,0],[0,1]]

def Matrix_Multi(A,B):
   #print (A,B)
    result=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j]=result[i][j]+A[i][k]*B[k][j]
                #print ("{},{},{},{}".format(i,j,k,result[i][j]))
    return (result)

#print(Matrix_Multi(A,B))


def Matrix_exp(A,p):
    result=[[1,0],[0,1]]
    if p ==1:
        return A

    for i in range(int(p/2)+1):
        result=Matrix_Multi(result,A)

    if p%2==1:
        result=Matrix_Multi(result,A)
    print (result[0][0])


t=str(input())
a,b,n=t