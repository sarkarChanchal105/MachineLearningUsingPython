array=[200,1,2,4,5,78,67,890,0,12]

####### Avg and Worst O(nlogn)
def quicksort(array):
    less=[]
    equl=[]
    greater=[]

    if len(array)>1:
        pivot=array[0]
        for x in array:
            #print (x)
            if x<pivot:
                less.append(x)
            if x==pivot:
                equl.append(x)
            if x>pivot:
                greater.append(x)
        return quicksort(greater)+equl+quicksort(less)
    else:
        return array

print ("Ouput of Quick Sort {}".format(quicksort(array)))


####### Avg and Worst O(n**2)
def bubble_sort():
   swapped=False
   for i in range(len(array)-1):
       if array[i]>array[i+1]:
           small=array[i+1]
           large=array[i]
           array[i+1]=large
           array[i]=small
           swapped=True
   if swapped==True:
    return bubble_sort()
   else:
       print (array)

bubble_sort()

#print ("Qutput of bubble Sort {}".format(array))



# ####### Avg and Worst O(n**2)
# def insertion_sort(array):
#     sorted_sublist=[]
#     sorted_sublist.append(array[0])
#     for i in range(len(array)-1):
#         next_element=array[i+1]
#         for j in range(len(sorted_sublist)-1):
#             if next_element<sorted_sublist[j]:
#                 position=j
#
#
#
# def insert_next_element(sorted_sublist,next_element):
#     for i in range(len(sorted_sublist)):
#         if next_element<sorted_sublist[i]:


###### Merge Sort ##########

def msort3(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = msort3(x[:mid])
    z = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    return result

#print (msort3([1,2,4,5,78,67,890,0,12]))