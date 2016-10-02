#
#
#
#
# def  StairCase(n):
#     str=''
#     j=0
#
#     for i in range(n+1):
#         for j in range (n-i):
#           str=str+' '
#         j=0
#         for j in range(i):
#            str=str+'#'
#         j=0
#         if str.lstrip().rstrip():
#             print(str)
#         str=''
#
# StairCase(10)
#
# A=[1,2,3,4]
#
# print(sum(A))

# s=input()
# print(s)





# import sys
# N = int(input().strip())
#
# if N%2 !=0:
#     print ('Weird')
#
# else:
#     if N>=2 and N<=5:
#         print ('Not Weird')
#     if N>=6 and N<=20:
#         print('Weird')
#     if N >20:
#         print('Not Weird')
#

#
# import sys
# N=int(input())
# array=[]
# for i in range(N):
#     sys.stdout.write(str(i))
# #print(i for i in range(N))


# n=int(input())
# list=[]
# while(n>=1):
#     todo=str(input())
#     try:
#         operation,i,e=todo.split(' ')
#         i=int(i )
#         e=int(e)
#     except:
#         try:
#             operation,e=todo.split(' ')
#             e=int(e)
#         except:
#             operation=todo.lstrip().rstrip()
#
#
#     #print("Operation ",operation)
#     if operation=='insert':
#         list.insert(i,e)
#     if operation=='print':
#         print(list)
#
#     if operation=='append':
#         list.append(e)
#
#     if operation=='sort':
#         list=sorted(list)
#
#     if operation=='remove':
#         list.remove(e)
#     if operation=='pop':
#         list.pop(len(list)-1)
#     if operation=='reverse':
#         list.reverse()
#
#     n-=1


#
# import sys
# N=int(input())
# array=[]
# for i in range(N):
#     sys.stdout.write(str(i))
#
#
# k=tuple([1,2,3])
#
# print (k)



