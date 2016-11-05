def pig_it(text):
    print (text)
    #return " ".join( [x[1:]+x[0]+'ay'  for x in text.split(" ") ])
    return " ".join(map(lambda x:x[1:]+x[0]+'ay' if x not in ('!','?') else x , [x for x in text.split(" ")]))