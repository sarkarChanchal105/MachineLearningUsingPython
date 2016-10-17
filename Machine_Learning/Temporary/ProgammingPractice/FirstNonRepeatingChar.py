array ='aaaarrrrrfffggglllllkkk333T'


def first_non_repeating(array):
    seen=[]
    unseen=[]
    for x in array:
        if x in seen:
            continue
        elif x in unseen:
            seen.append(x)
            unseen.remove(x)
        else:
            unseen.append(x)
    print (unseen[0])
    #return unseen[0]


first_non_repeating(array)


s_array=[a for a in array]

print (s_array)

dict={}

