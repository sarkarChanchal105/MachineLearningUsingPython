from sklearn.ensemble import RandomForestClassifier
import Machine_Learning.CommonFunctions.commonvariables as common
import numpy as np
import matplotlib.pyplot as plt

df_wine=common.df_wine
x_train=common.x_train
x_test=common.x_test
x_train_std=common.x_train_std
x_test_std=common.x_test_std
y_train=common.y_train
y_test=common.y_test

# Build the covariance matrix
cov_mat=np.cov(x_train_std.T)

# get the eigen values and eigen vectors
eigen_vals,eigen_vecs = np.linalg.eig(cov_mat)
#print ("\nEigenvalues \n%s" %eigen_vals)

## Get the cumulative abd individual component's importance
tot = sum(eigen_vals)
var_exp = [i/tot for i in sorted(eigen_vals,reverse=True)] #indiviaul explained variance
cum_var_exp = np.cumsum(var_exp) # Cumulative explained variance

number_of_components=x_train.shape[1]+1
plt.bar(range(1,number_of_components),var_exp, alpha=0.5,align='center', label='Individual explianed variance')
plt.step(range(1,number_of_components),cum_var_exp, where='mid',label='Cumulative explianed variance')

plt.ylabel('Explained variance ratio')
plt.xlabel('Principle Components')
plt.legend(loc='best')
plt.show()

## Sort the eigne values and eigen vectors

#print ("Printing Eigen Vector\n",eigen_vecs)
## Get the eigen value and eigen vector pair
eigen_pairs=[(np.abs(eigen_vals[i]),(eigen_vecs[:,i]))
                for i in range(len(eigen_vals))]

# print ("Before sort" ,eigen_pairs)
#
# eigen_pairs.sort(reverse=True)
#
# print ("after sort" ,eigen_pairs)
# eigen_pairs.sort(reverse=True)



## Select the first two components. This will create a projection matrix with top eigen vectors.

w= np.hstack((eigen_pairs[0][1][:,np.newaxis],
             eigen_pairs[1][1][:,np.newaxis]

             ))
#print ("Printing the projection matrix")
#print (w)


## Transform the training data set by doing do proeuct between projection matrix and training data
x_train_pca = x_train_std.dot(w)
#print ("Shape of PCA \n" ,x_train_pca.shape)
#print ("Shape of train \n",x_train.shape)


#
## lets plot the data in two dimentional scatterplot.
colors =['r','b','g']
markers=['x','x','x']
i=0
for l,c,m in zip(np.unique(y_train),colors,markers):
    #print ("l: {} , c: {}, m: {}".format(l,c,m))
    plt.scatter(x_train_pca[y_train==1,0],x_train_pca[y_train==1,1],c=c,label=l,marker=m)


plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')

plt.show()

