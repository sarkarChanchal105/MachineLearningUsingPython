###oss_env_dckr_folder: "{{ mgmt_node.log_root }}/{{ mgmt_node.host_prefix }}" ### Refer to the file role: mgmt-nodes->tasks->mgmt-node.yml
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from  Machine_Learning.CommonFunctions import  PlotDecisionRegion
import matplotlib.pyplot as plt
import numpy as np
import sys

np.random.seed(0)

x_xor = np.random.randn(200,2)

#print (x_xor)
#print ("***************")
# print (x_xor[:,0])
#
# print (x_xor[:,1])
# print ("***************")
# print (x_xor[:,])
# print ("***************")
# print (x_xor[1:,])

y_xor = np.logical_xor( x_xor[:,0] > 0 , x_xor[:,1]>0)

#print (y_xor)

#sys.exit()

y_xor=np.where(y_xor,1,-1)

#print (y_xor)
#print (x_xor)
print (y_xor)
print ([y_xor==1,0])
print (x_xor[y_xor==1,0])
print (x_xor)


#print (x_xor[y_xor==1,1])

#sys.exit()

plt.scatter(x_xor[y_xor==1,0],x_xor[y_xor==1,1],c='b',marker='x',label='1')

plt.scatter(x_xor[y_xor==-1,0],x_xor[y_xor==-1,1],c='r',marker='s',label='-1')

plt.ylim(-3.0)

plt.legend()

plt.show()


svm =SVC(kernel ='rbf',random_state=0,gamma=0.10,C=100.0)
svm.fit(x_xor,y_xor)

PlotDecisionRegion.plot_decision_regions(x_xor,y_xor,classifier=svm)
plt.legend(loc='upper left')
plt.show()

y_pred =svm.predict(x_xor)

print ("Number of misclassified samples is %d " %(y_pred!=y_xor).sum())


#print ("Miss Classified in Test Samples %d" %(y_pred!=y_test).sum() )