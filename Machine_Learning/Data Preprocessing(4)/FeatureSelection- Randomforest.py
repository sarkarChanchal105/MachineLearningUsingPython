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

feat_labels= df_wine.columns[1:] ## Get thr column headers of the dataset.
forest = RandomForestClassifier(n_estimators=10000000,random_state=0,n_jobs=1) ## Create a Random Forest Classifier object
forest.fit(x_train,y_train) ## Fit the data into the model
importances=forest.feature_importances_ ## get the feature importance
# print("Original ",np.argsort(importances))
indices = np.argsort(importances)[::-1]
# print (" importances ",importances)
# print (" indices ",indices)

for f in range(x_train.shape[1]):
    print("%2d) %-*s %f" % (f+1,30,feat_labels[indices[f]],
                                    importances[indices[f]]))

# for f in range(x_train.shape[1]):
#     print(feat_labels[indices[f-1]],importances[indices[f-1]])

## Plot the feature importance in the bar chart.
plt.title("Feature Importance")
plt.bar(range(x_train.shape[1]),importances[indices],color='lightblue',align='center')
plt.xticks(range(x_train.shape[1]),feat_labels[indices],rotation=90)
plt.xlim([-1,x_train.shape[1]])
plt.tight_layout()
plt.show()

##
x_selected =forest.transform(x_train,threshold=0.15)
print (x_selected.shape)





