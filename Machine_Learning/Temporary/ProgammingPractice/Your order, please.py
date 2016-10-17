def order(sentence):
  # code here
  dict={}
  array=sentence.split()
  for word in array:
    dict[int(get_index(word))]=word
  return " ".join([dict[i] for i in range(1,len(dict)+1) ])


def get_index(word):
    for e in word:
        if e.isdigit():
            return e



print (order('"is2 Thi1s T4est 3a'))