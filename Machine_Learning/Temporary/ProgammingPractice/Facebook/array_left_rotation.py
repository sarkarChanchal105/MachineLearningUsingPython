A=[1,2,3,4,5]
# https://www.hackerrank.com/challenges/ctci-array-left-rotation
def array_left_rotation(a, n, k):
    for i in range(0,k):
        a.append(a.pop(0))
    #print (a)
    return a
#n, k = map(int, input().strip().split(' '))
n, k =5,4
#a = list(map(int, input().strip().split(' ')))
a=A

answer = array_left_rotation(a, n, k)

print (*answer,sep=' ')


