import numpy as np
import matplotlib.pyplot as plt


def ginni(p):
  pass

def entrpy(p):
    return -p*np.log2(p) -(1-p)*np.log2(1-p)


x=np.arange(0.0,1.0,0.01)
#print (x)
_entrpy = [entrpy(p) if p!=0 else None for p in x]
print (_entrpy)

plt.plot(x,_entrpy)

plt.show()

