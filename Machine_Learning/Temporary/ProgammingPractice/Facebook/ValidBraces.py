# def validBraces(string):
#     #print (string)
#     n=len(string)
#     if n%2 !=0:
#         return False
#     dict_compliment = {'(':')','{':'}','[':']'}
#     opening=['(','{','[']; closing=[dict_compliment[x] for x in opening ]
#     i=0
#     array=[x for x in string]
#     result=False
#     while(n>0 and i<n):
#         if array[i] in opening:
#             i+=1
#         else:
#           if array[i]==dict_compliment[array[i-1]]:
#               result=True
#               array.remove(array[i])
#               array.remove(array[i-1])
#               i=0
#           else:
#               result=False
#               return result
#         n=len(array)
#     return result


def validBraces(s, previous = ''):
  while s != previous:
      previous, s = s, s.replace('[]','').replace('{}','').replace('()','')
  return not s

#print ("{()}".replace('{}',''))

print (validBraces('{}()[]'))
#print (validBraces('([{}])'))

#print(validBraces('(((({{'))

# for s in ['{}()[]','([{}])','([}{])','{}({})[]','(({{[[]]}}))','(((({{']:
#     print (s," ",validBraces(s))
