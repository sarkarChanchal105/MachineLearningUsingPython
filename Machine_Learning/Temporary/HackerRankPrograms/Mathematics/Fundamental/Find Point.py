# https://www.hackerrank.com/challenges/find-point

n=int(input())
while(n>=1):
    points=str(input()).split()
    Px=int(points[0])
    Py=int(points[1])
    Qx=int(points[2])
    Qy=int(points[3])

    s1,s2=Qx+(Qx-Px),Qy+(Qy-Py)

    print(s1,s2)
    n-=1