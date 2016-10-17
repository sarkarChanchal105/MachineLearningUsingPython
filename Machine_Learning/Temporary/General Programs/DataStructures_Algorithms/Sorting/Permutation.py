




#permutation()


def permutations(string, index=0):


    if index==len(string):
        print ("".join(string))


    for i in range(index,len(string)):

        string_copy = [e for e in string]
        string_copy[index],string_copy[i]= string_copy[i],string_copy[index]

        permutations(string_copy,index+1)

string ='123'
#permutations(string)


def stringPermutations(s):
    if len(s) < 2:
        yield s
        return
    for pos in range(0, len(s)):
        char = s[pos]
        permForRemaining = list(stringPermutations(s[0:pos] + s[pos+1:]))
        for perm in permForRemaining:
            yield char + perm

#
# for s in stringPermutations(string):
#     print(s)




