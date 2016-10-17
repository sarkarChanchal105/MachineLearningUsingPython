array=[1, 7, 3, 4,0]
result=[]


def multi(array):
    K=1
    for a in array:
        K=K*a
    return K

for a in array:
    b_array=[a for a in array]
    b_array.remove(a)
    result.append(multi(b_array))

print (result)
