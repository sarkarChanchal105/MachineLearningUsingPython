from sklearn.grid_search import GridSearchCV
from sklearn.svm import  SVC
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.learning_curve import learning_curve, validation_curve
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
import Machine_Learning.CommonFunctions.commonvariables as common
from sklearn.cross_validation import train_test_split,StratifiedKFold,cross_val_score
import numpy as np
from scipy import interp
from sklearn.metrics import roc_curve, auc , roc_auc_score, accuracy_score

x=common.x_breast
y=common.y_breast



## create a pipiline to exuete the Data Preporocessing and classification model
pipeline_lr = Pipeline([('scl',StandardScaler()),('pca',PCA(n_components=2)),(('clf',LogisticRegression(penalty='l2', random_state=0,C=10))) ])


## partiion the data into traning and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

x_train_2=x_train[:,[4,14]]

## Cross Validation
cv=StratifiedKFold(y_train,n_folds=3,random_state=1)

## Create a figure
fig = plt.figure(figsize=(7,5))


mean_tpr=0
mean_fpr=np.linspace(0,1,100)
all_tpr=[]

for i, (train,test) in enumerate(cv):
        print ("i= {} max_train= {} max_test {}".format(i,max(train),max(test)))
        #print ("train {} test{}".format(train,test))
        print (x_train[train])
        import sys; sys.exit()

## for each fold excute the train and test  and calculate true positive, false postive rate.
for i, (train,test) in enumerate(cv):
    probas = pipeline_lr.fit(x_train_2[train],y_train[train]).predict_proba(x_train_2[test])
    try:
        fpr,tpr,threshold = roc_curve(y_train[test],probas[:,1],pos_label=1)
    except Exception:
        pass
    mean_tpr+=interp(mean_fpr,fpr,tpr)
    mean_tpr[0]=0.0
    roc_auc=auc(fpr,tpr)
    plt.plot(fpr, tpr,lw=1,label='ROC fold %d (area = %0.2f)' % (i+1,roc_auc))

plt.plot([0,1],[0,1],linestyle='--',color=(0.6,0.6,0.6,0.6),label='Random Guessing')
mean_tpr /= len(cv)
mean_tpr[-1]=1.0
mean_auc = auc(mean_fpr,mean_tpr)
plt.plot(mean_fpr,mean_tpr,'k--',label='mean ROC (area =%0.2f)' % mean_auc, lw=2 )
plt.plot([0,0,1],[0,1,1],lw=2,linestyle=':',color='black',label='perfect performance')
plt.xlim([-0.05,1.05])
plt.ylim([-0.05,1.05])
plt.xlabel('false postive rate')
plt.ylabel('true postive rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()


pipeline_lr =pipeline_lr.fit(x_train_2,y_train)

y_pred2 = pipeline_lr.predict(x_test[:,[4,14]])

print('ROC AUC : %.3f' % roc_auc_score(y_true=y_test,y_score=y_pred2))
print ('Accuracy : %0.3f' % accuracy_score(y_true=y_test,y_pred=y_pred2))
