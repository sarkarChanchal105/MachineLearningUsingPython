def autocorrect(input):
    output=" ".join([autocorrect_you(x)  for x in input.split(" ")])
    print (output)
    return output


def autocorrect_you(input,char_to_append=''):
    default_string='your sister'
    if input[0:3]  in ('u','you','You') and len(input)<=3:
        return  default_string+char_to_append

    if input[0:4] in ('Youu','youu'):
        return default_string+char_to_append

    if input[0:4] =='you!' :
        return str(default_string+'!')
    return input

print(autocorrect("I love you you!"))


import re

def autocorrect(input):
    return re.sub(r'(?i)\b(u|you+)\b', "your sister", input)

