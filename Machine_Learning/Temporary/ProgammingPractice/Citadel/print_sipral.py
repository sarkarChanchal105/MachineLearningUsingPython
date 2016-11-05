import itertools

arr = [[1,2,3,4],
       [12,13,14,5],
       [11,16,15,6],
       [10,9,8,7]]
print (len(arr))
m=4;n=4
T=0 ## topmost row of the un traversed array
B=m-1 ## bottom most of the untraversed array
L=0 ## Left most column of the untraversed array
R=n-1 ## Right most column of the untraversed array
dir=0  ## direction

while (T<=B and L<=R):

    ### Move Right
    if (dir==0):
        print ("Moving Right")
        for i in range (L,R+1):
            print(arr[T][i])
        T+=1
        dir=1
    ### Move down
    if (dir==1):
        print ("Moving Down")
        for i in range(T,B+1):
            print(arr[i][R])
        R-=1
        dir=2
    ### Move left
    if (dir==2):
        print ("Moving left")
        for i in range(R,L-1,-1):
            print(arr[B][i])
        B-=1
        dir=3
    else:
        ### Move up
        if (dir==3):
            print ("Moving Up")
            for i in range(B,T-1,-1):
                print(arr[i][L])
            L+=1
            dir=0





