def duplicate_count(text):
    # Your code goes here
    print (text)
    array = [e for e in text.upper()]
    final_count=0
    visited=[]
    for i in range(len(array)):
        e=array[i]
        count=0;j=0

        while j <len(array) and e not in visited :
            if e==array[j]:
                count+=1
            j+=1
        if count>1:
            final_count+=1
        visited.append(e)
    return final_count


print (duplicate_count('abcdeaB'))