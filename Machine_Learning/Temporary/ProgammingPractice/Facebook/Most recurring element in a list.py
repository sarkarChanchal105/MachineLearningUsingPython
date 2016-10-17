A=[1,2,100,400,3,4,4,4,5,6,7,101,101,101]

A=sorted(A)
dict={}

#print (max(A))

for a in A:
    #print(a)
    if a in dict.keys():
        value=dict[a]
        dict[a]=value+1
    else:
        dict[a]=1


max_key=max(dict,key=lambda k: dict[k])

print (max_key)
#print(max(dict.values()))

#print(dict)

# inv_map = {v:k for k,v in dict.items()}
#
# #print (dict.items())
#
# for k,v in dict.items():
#     print (k,v)
#     inv_map.
# #print (inv_map)
#
# #print(inv_map[max(dict.values())])