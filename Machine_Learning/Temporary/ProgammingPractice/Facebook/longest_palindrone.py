def longest_palindrome (s):
    long_pal=''
    count=0
    string=''
    length=len(s)
    # for x,y in enumerate(s):
    #     print ("x =" ,x,"y =",y)

    if length<1:
        return length
    for x,y in enumerate(s):
       t=x
       for i in range(x):
           string = s[i:t+1]
           if string ==string[::-1]:
              long_pal=len(string)
    return long_pal

longest_palindrome("baablkj12345432133d")


def pal(text):
    """
    param text: given string or test
    return: returns index of longest palindrome and a list of detected palindromes stored in temp
    """
    lst = {}
    index = (0, 0)
    length = len(text)
    if length <= 1:
        return index
    word = text.lower()  # Trying to make the whole string lower case
    temp = str()
    for x, y in enumerate(word):
        # Try to enumerate over the word
        t = x
        for i in range(x):
            if i != t+1:
                string = word[i:t+1]
                if string == string[::-1]:
                    temp = text[i:t+1]
                    index = (i, t+1)
                    lst[temp] = index
    tat = lst.keys()
    longest = max(tat, key=len)
    #print longest
    return lst[longest], temp

#print(pal("baablkj12345432133d"))
#print(pal("baa"))

