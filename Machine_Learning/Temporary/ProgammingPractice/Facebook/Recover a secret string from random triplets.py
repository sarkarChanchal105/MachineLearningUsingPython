import numpy as np
def recoverSecret(triplets):
  'triplets is a list of triplets from the secrent string. Return the string.'


secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

#print (triplets[1])
#print(np.insert(triplets[0], ))

#print ( np.intersect1d(triplets[0],triplets[1]) )

#for i in triplets.shape():

#print (len())

nparray = np.array(triplets)

#nparray.

print(nparray.shape)
pivot=nparray[0]
array_pivot=triplets[0]
print (pivot)
for i in range(nparray.shape[0]-1):
    #print ("Hello ",np.intersect1d(pivot,nparray[i+1])[0] )
    intersect=np.intersect1d(pivot,nparray[i+1])
    if len(intersect)>0  :
        for e in intersect:
            array_pivot.append(e)
            pivot=np.array(array_pivot)
            print ("pivot =",array_pivot)

    else:
        for e in nparray[i+1]:
            array_pivot.append(e)
            pivot=np.array(array_pivot)
            print ("pivot =",array_pivot)