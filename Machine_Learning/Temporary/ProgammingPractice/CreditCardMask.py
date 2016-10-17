# return masked string
def maskify(cc):
    if len(cc)<=4:
        return cc
    else:
       result= "".join('#' for i in range(len(cc)-4 ))
       print (result)
       return result+(cc[len(cc)-4:])

print(maskify("4556364607935616"))