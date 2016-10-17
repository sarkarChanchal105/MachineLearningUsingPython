def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


print(spin_words("I love you"))


sentence ='I love you'

for x in sentence.split(" "):
    print(x[::-1])
