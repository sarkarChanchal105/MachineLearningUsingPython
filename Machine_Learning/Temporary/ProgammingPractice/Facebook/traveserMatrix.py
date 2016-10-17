A=[
 [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]


]

n=4
row=0
col=4
revised_array=[]

def right(n,row):
    i=0
    while(i<n-row):
        revised_array.append(A[row][i])
        i+=1


def down(row,col):
    i=0
    print ("row =",row)
    while(i<=n-row):
        revised_array.append(A[i][col-1])
        i+=1


def left():
    pass

def up():
    pass


def traverse(row,col):
    right(n,row)
    print (revised_array)
    row=row+1

    down(row,col)
    print (revised_array)


traverse(row,col)