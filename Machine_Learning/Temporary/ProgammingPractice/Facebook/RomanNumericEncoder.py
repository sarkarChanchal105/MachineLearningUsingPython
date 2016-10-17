def solution(n):
    # TODO convert int to roman string
    roman_dick={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    r_roman_dick={v:k for k,v in roman_dick.items()}
    print (r_roman_dick.items())
    keys= sorted([i for i in r_roman_dick.keys()])
    print (keys)
    found=False;i=0;greatest_divider=''

    if n==1:
        result=

    while (not found):
        if n/keys[::-1][i]>=1:
            found=True
            greatest_divider=keys[::-1][i]
        i+=1




    #print (g)


solution(10)
