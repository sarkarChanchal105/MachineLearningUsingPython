import sys
import numpy as np
from numpy.random import seed
import pandas as pd
import matplotlib.pyplot as plt
class AdalineSGD(object):

    def __init__(self,eta=0.01,n_iter=10,shuffle=True,random_state=None):
        self.eta=eta
        self.n_iter=n_iter
        self.shuffle=shuffle
        self.random_state=random_state

        if random_state:
            seed(random_state)

    def fit(self,x,y):
        self._initialize_weights(x.shape[1])
        self.cost_=[]

        for i in range(self.n_iter):
            if self.shuffle:
                x,y=self._shuffle(x,y)
                #print ("x= ",x)
                #print ("y= ",y)
                #sys.exit()
            cost=[]
            for xi, target in zip(x,y):

                cost.append(self._update_weights(xi,target))

            avg_cost=sum(cost)/len(y)
            self.cost_.append(avg_cost)
        return self

    def partial_fit(self,x,y):

        if not self.w_initialized:
            self._initialize_weights(x.shape[1])

        if y.ravel().shape[0]>1:
            for xi,target in zip(x,y):
                self._update_weights(xi,target)
        else:
            self._update_weights(x,y)
        return self



    def _update_weights(self,xi,target):

        output = self.net_input(xi)
        error =(target-output)
        self.w_[1:]+=self.eta*xi.dot(error)
        self.w_[0]+=self.eta*error
        cost=0.5*error**2
        print("xi =",xi, " target = ", target,"errors = ",error, "output =",output)
        return cost

    def net_input(self,xi):
        return np.dot(xi,self.w_[1:])+self.w_[0]


    def _initialize_weights(self,m):
        print ("m =", m)
        self.w_=np.zeros(1+m)
        self.w_initialized=True
        print ("Initiazed Weights ",self.w_)
        #sys.exit()

    def _shuffle(self,x,y):
        r=np.random.permutation(len(y))
        return x[r],y[r]

def main():


    df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None )
    y=df.iloc[0:100,4].values
    y=np.where(y =='Iris-setosa',-1,1)
    x=df.iloc[0:100,[0,1]].values


    #print (x)
    x_std=np.copy(x)

    x_std[:,0] = (x_std[:,0] - x_std[:,0].mean())/x_std[:,0].std()
    x_std[:,1] = (x_std[:,1] - x_std[:,1].mean())/x_std[:,1].std()

    ada= AdalineSGD(n_iter=15,eta=0.01,random_state=1)
    ada.fit(x_std,y)
    #ada.fit(x,y)
    plt.plot(range(1,len(ada.cost_)+1),ada.cost_,marker='o')

    plt.xlabel("Epoches")
    plt.ylabel("Avg Cost")
    plt.show()
if __name__ == '__main__':
    main()


