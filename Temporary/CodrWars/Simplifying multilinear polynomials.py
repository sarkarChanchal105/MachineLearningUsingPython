import re
text ='xyz+223xyz'

dict_count={}

dict_operation={}

for a in re.split("[, \-!?:+]+",text):
    print (a)
    #dict_count[a]=1
    items = re.findall("[0-9]", a)
    a=re.split("[0-9]",a)[-1]
    print ("A =",a)

    if len(items)>0:
        multiplier=1
        sum=1
        for k in items[::-1]:
            sum=sum+ int(k)*multiplier
            multiplier=multiplier*10
        dict_count[a]=sum

    print (dict_count)