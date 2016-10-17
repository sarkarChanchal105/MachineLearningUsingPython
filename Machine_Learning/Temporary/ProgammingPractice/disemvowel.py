def disemvowel(string):
    vowels = ['a','e','i','o','u']
    array = [e for e in string]
    #print (array)
    for e in vowels:
        while e in array:
            array.remove(e)
    string = "".join([e for e in array])

    print (string)
    return string


disemvowel('This website is for losers LOL!')
