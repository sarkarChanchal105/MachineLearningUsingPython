#### Classidy using Adaptive Linear Neuron ####
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap
import sys


class AdalineGD(object):

    def __init__(self,eta,n_iter=10):
        self.eta=eta
        self.n_iter=n_iter

    def fit(self,x,y):

        self.w_=np.zeros(1+x.shape[1])
        self.cost_=[]
        for i in range(self.n_iter):
           output = self.net_input(x)
           errors=(y - output)
           #self.w_[1:] +=self.eta * x.T.dot(errors)
           self.w_[1:] +=self.eta * np.dot(x.T,errors)
           self.w_[0] += self.eta * errors.sum()
           cost= (errors ** 2)/2
           self.cost_=cost
        return self

    def net_input(self,x):
        return np.dot(x,self.w_[1:])+self.w_[0]


    def activation(self,x):
        return self.net_input(x)


    def predict(self,x):
        return np.where(self.activation(x)>= 0.0,1,-1)




def main():

    df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None )

    #df.to_csv('iris.csv')

    #sys.exit()
    y=df.iloc[0:100,4].values

    y=np.where(y =='Iris-setosa',-1,1)

    x=df.iloc[0:100,[0,1]].values

    fig,ax=plt.subplots(nrows=1,ncols=3,figsize=(8,4))
    ada1= AdalineGD(n_iter=10,eta=0.01).fit(x,y)

    ax[0].plot( range(1,len(ada1.cost_)+1), np.log10(ada1.cost_),marker='x' )
    ax[0].set_xlabel('Epoches')
    ax[0].set_ylabel('log(sum-squared)')
    ax[0].set_title('Adaline - Learning Rate 0.01')

    ada2= AdalineGD(n_iter=10,eta=0.0001).fit(x,y)
    ax[1].plot( range(1,len(ada2.cost_)+1),np.log10(ada2.cost_),marker='x' )
    ax[1].set_xlabel('Epoches')
    ax[1].set_ylabel('log(sum-squared)')
    ax[1].set_title('Adaline - Learning Rate 0.0001')
    x_std=np.copy(x)
    #print (x_std)
    #print (x_std[:,0])
    #sys.exit()
    x_std[:,0]= (x_std[:,0] - x_std[:,0].mean())/x_std[:,0].std()
    x_std[:,1]= (x_std[:,1] - x_std[:,1].mean())/x_std[:,1].std()

    ada3= AdalineGD(n_iter=15,eta=0.01).fit(x_std,y)
    ax[2].plot( range(1,len(ada3.cost_)+1),np.log10(ada3.cost_),marker='x' )
    ax[2].set_xlabel('Epoches')
    ax[2].set_ylabel('log(sum-squared)')
    ax[2].set_title('Adaline - Learning Rate 0.01')
    plt.show()


if __name__ == '__main__':
     main()



