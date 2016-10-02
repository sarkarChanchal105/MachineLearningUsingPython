import sys
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
import numpy as np
from matplotlib.colors import  ListedColormap
import matplotlib.pyplot as plt

iris=datasets.load_iris()
df=iris.data

x= iris.data[:,[2,3]]
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
sc=StandardScaler()
sc.fit(x_train)
x_train_std=sc.transform(x_train)
x_test_std=sc.transform(x_test)
ppn = Perceptron(n_iter=40,eta0=0.1,random_state=0)
ppn.fit(x_train_std,y_train)
y_pred = ppn.predict(x_test_std)
print ("Misclassified samples : %d" %(y_test!=y_pred).sum() )

x_combined=np.vstack((x_train_std,x_test_std))
y_combined=np.vstack((y_train,y_test))



def plot_decision_regions(x,y,classifier,test_idx=None,resolution=0.02):
    markers=('s','x','o','^','v')
    colors=('red','blue','lightgreen','gray','cyan')
    cmap=ListedColormap(colors[:len(np.unique(y))])

    x1_min,x1_max=x[:,0].min()-1,x[:0].max()+1
    x2_min,x2_max=x[:,1].min()-1,x[:1].max()+1

    xx1,xx2 = np.meshgrid(np.arange(x1_min,x1_max,resolution),np.arange(x2_min,x2_max,resolution))
    z=classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    z=z.reshape(xx1.shape)
    plt.contourf(xx1,xx2,z,alpha=0.4,cmap=cmap)
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())

    for idx,c1 in enumerate(np.unique(y)):
        plt.scatter(x=x[y == c1,0], y=x[y ==c1,1],alpha=0.8,c=cmap(idx),marker=markers[idx],label=c1)


#plot_decision_regions(x_combined,y,classifier=ppn,test_idx=(105,150))

#plt.show()
#plt.xlabel()