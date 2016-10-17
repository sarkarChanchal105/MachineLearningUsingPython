A =[2,0,3,1,0,4,45,0,6,7,0,90,90,0,100,34,45,0,565]


def sort():
    for a in A:
        if a==0:
            A.remove(a)
            A.append(a)
    return A


print(sort())


