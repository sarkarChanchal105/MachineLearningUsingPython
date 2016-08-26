#### Perceptron using Step Function ####
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap

import sys


class perceptron(object):

    def __init__(self,eta=0.01,n_iter=10):
        self.eta=eta
        self.n_iter=n_iter

    def fit(self,x,y):

        self.w_= np.zeros(1+x.shape[1])
        self.errors_=[]
        print (zip(x,y))

        for _ in range(self.n_iter):
            errors=0
            for xi, target in zip(x,y):
                update=self.eta*(target- self.predict(xi))
                self.w_[1:]+= update * xi
                self.w_[0:]+= update
                errors += int(update!=0.0)
            self.errors_.append(errors)
        return self

    def net_input(self,x):
        return np.dot(x,self.w_[1:])+self.w_[0]

    def predict(self,x):
        return np.where(self.net_input(x)>=0.0,1,-1)

    def plot_decision_region(self,x,y,classifier,resolution=0.02):
        markers=('s','x','o','^','v')
        colors=('red','blue','lightgreen','gray','cyan')
        cmap=ListedColormap(colors[len(np.unique(y))])
        #plotting the decesion surface
        x1_min,x1_max =x[:,0].min() -1,x[:,0].max()+1
        x2_min,x2_max = x[:1].min() -1,x[:,1].max()+1
        xx1,xx2 =np.meshgrid(np.arange(x1_min,x1_max,resolution),np.arange(x2_min,x2_max,resolution))
        z=classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
        z=z.reshape(xx1.shape)
        plt.contourf(xx1,xx2,z,alpha=0.4,cmap=cmap)
        plt.xlim(xx1.min(),xx1.max())
        plt.ylim(xx2.min(),xx2.max())

        # for idx,c1 in enumerate(np.unique(y)):
        #     plt.scatter(x=x[y == c1,0],y=x[y==c1,1],alpha=0.8,c=cmap(idx),makers=markers[idx], label=c1 )
        # #plt.show()


def main():
    df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None )
    print ("Shape ",df.shape)
    #print df
    print ('\n'+"printing head "+'\n',df.head())
    print ('\n'+"printing tail "+'\n', df.tail())

    y=df.iloc[0:100,4].values
    print (y)

    y=np.where(y =='Iris-setosa',-1,1)
    print (y)

    x=df.iloc[0:100,[0,2]].values
    plt.scatter(x[:50,0],x[:50,1],color='red',marker='o',label='setosa')
    plt.scatter(x[50:100,0],x[50:100,1],color='blue',marker='x',label='versicolor')
    plt.xlabel('Sepal length')
    plt.ylabel('Petal length')
    plt.legend(loc='upper left')
    plt.show()
    ppn = perceptron(eta=0.01,n_iter=10)
    ppn.fit(x,y)

    plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker='o')
    plt.show()
    plt.xlabel('epoch')
    plt.ylabel('Misclassification')
    ppn.plot_decision_region(x,y,classifier=ppn)

    #plt.show()

if __name__ == '__main__':
    main()

