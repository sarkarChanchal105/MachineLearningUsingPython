def permutation_1(s):
   if len(s) == 1:
     return [s]
   n=len(s)
   perm_list = [] # resulting list
   i=0;j=0
   remaining_elements=[]
   for i in range(n):
        remaining_elements=[]
        for j in range(n) :
            if i!=j:
                remaining_elements.append(s[j])
        z =permutation_1(remaining_elements) # permutations of sublist


        for t in z:
             perm_list.append([s[j]] + t)

   return perm_list


# def permutations(s):
#     perm_list=permutation_1(s)
#     if len(perm_list)==1:
#         return perm_list
#     f_perm_list=[]
#     str=''
#     for b in perm_list:
#         str="".join([x for x in b])
#         #print (str)
#         print (str)
#         if str not in f_perm_list:
#             f_perm_list.append(str)
#     return f_perm_list

print(permutations('ab'))