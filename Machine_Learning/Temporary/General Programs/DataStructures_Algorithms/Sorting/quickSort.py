A=[100,2,4,5,-1,5,1000,10,90,50,90,-100,500,56]
B=[100,2,4,-1,1000,10,90,50,90,-100,500,56]
def quicksort(arr):
    """ Quicksort a list

    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list

    """
    #print (arr)
    #print("!!!!!!!!!!!!")
    if not arr:
        return []

    pivots = [x for x in arr if x == arr[0]]
    lesser = quicksort([x for x in arr if x < arr[0]])
    greater = quicksort([x for x in arr if x > arr[0]])

    print (pivots)
    print(lesser)
    print(greater)
    print ("$$$$$$$$")
    return lesser + pivots + greater

print (quicksort(A))
