## https://jamesmccaffrey.wordpress.com/2013/11/05/why-you-should-use-cross-entropy-error-instead-of-classification-error-or-mean-squared-error-for-neural-network-classifier-training/

import tensorflow as tf
import numpy as np
import math

try:
    from tqdm import tqdm
except ImportError:
    def tqdm (x, *args, **kwrgs):
        return x

np.random.seed(0)

file='C:\Chanchal\Cisco\Chanchal\MachineLearningUsingPython\large-data-files\data_with_labels.npz'

data = np.load(file)
train = data['arr_0']/255.
labels = data['arr_1']

print (train[0].shape)
print (labels[0])

import matplotlib.pyplot as plt

#plt.ion()

plt.figure(figsize=(6,6))
f,plts =plt.subplots(5, sharex=True)
c=100


for i in range(5):
    plts[i].pcolor(train[c+i*558],cmap=plt.cm.gray_r)

def to_onehot(labels,nclasses=5):
    outlabels = np.zeros((len(labels),nclasses))
    for i, l in enumerate(labels):
        outlabels[i,l]=1
    return outlabels

onehot= to_onehot(labels)



indices = np.random.permutation(train.shape[0])

print (indices.shape)

valid_cnt = int(train.shape[0] * 0.1)

print (valid_cnt)
test_idx, training_idx = indices[:valid_cnt],indices[valid_cnt:]

print (test_idx)
#print (training_idx)

test, train = train[test_idx,:],train[training_idx,:]

print (train.shape)
print (test.shape)

onehot_test,onehot_train = onehot[test_idx,:],onehot[training_idx,:]

#plt.show()

sess = tf.InteractiveSession()

x= tf.placeholder("float",[None,1296])

y_=tf.placeholder("float",[None,5])


## Hidden Layer
number_of_hidden= 128

W1=tf.Variable(tf.truncated_normal([1296,number_of_hidden],stddev=1./math.sqrt(1296)))


b1= tf.Variable(tf.constant(0.1,shape=[number_of_hidden]))
h1= tf.sigmoid(tf.matmul(x,W1)+b1)


## Output Layer
W2=tf.Variable(tf.truncated_normal([number_of_hidden,5],stddev=1./math.sqrt(5)))
b2=tf.Variable(tf.constant(0.1,shape=[5]))

sess.run(tf.global_variables_initializer())

y=tf.nn.softmax(tf.matmul(h1,W2)+b2)
#
#
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y+1e-20,logits=y_))

print ("W1",W1)
print ("b1",b1)
print ("h1",h1)

print ("W2",W2)
print ("b2",b2)
print ("y",y)




train_step = tf.train.GradientDescentOptimizer(0.02).minimize(cross_entropy)

epochs=5000
train_acc=np.zeros(epochs//10)
test_acc=np.zeros(epochs//10)

correct_prediction = tf.equal(tf.argmax(y,1),tf.arg_max(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,"float"))

for i in tqdm (range(epochs)):
    if i%10 ==0:
        A = accuracy.eval(feed_dict={
            x: train.reshape([-1,1296]),
            y_: onehot_train})
        train_acc[i//10]=A

        A = accuracy.eval(feed_dict={
            x: test.reshape([-1, 1296]),
            y_: onehot_test})
        test_acc[i // 10] = A

    train_step.run(feed_dict={
        x: train.reshape([-1,1296]),
        y_:onehot_train
    })

print (train_acc[-1])
print (test_acc[-1])



#
# correct_prediction = tf.equal(tf.argmax(y,1),tf.arg_max(y_,1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction,"float"))



# W=tf.Variable(tf.zeros([1296,5]))
# b=tf.Variable(tf.zeros([5]))
#
# sess.run(tf.global_variables_initializer())
#
# y=tf.nn.softmax(tf.matmul(x,W)+b)
#
# #
#cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=y_))
# #
# #
# # train_step = tf.train.GradientDescentOptimizer(0.02).minimize(cross_entropy)
#
#
# # How we train
# train_step = tf.train.GradientDescentOptimizer(0.02).minimize(cross_entropy)
#
# correct_prediction = tf.equal(tf.argmax(y,1),tf.arg_max(y_,1))
#
# accuracy = tf.reduce_mean(tf.cast(correct_prediction,"float"))
#
# epochs=1000
# train_acc=np.zeros(epochs//10)
# test_acc=np.zeros(epochs//10)
#
# for i in tqdm (range(epochs)):
#     if i%10 ==0:
#         A = accuracy.eval(feed_dict={
#             x: train.reshape([-1,1296]),
#             y_: onehot_train})
#         train_acc[i//10]=A
#
#         A = accuracy.eval(feed_dict={
#             x: test.reshape([-1, 1296]),
#             y_: onehot_test})
#         test_acc[i // 10] = A
#
#     train_step.run(feed_dict={
#         x: train.reshape([-1,1296]),
#         y_:onehot_train
#     })
#
# print (train_acc[-1])
# print (test_acc[-1])
#
# plt.figure(figsize=(6,6))
# plt.plot(train_acc,'bo')
# plt.plot(test_acc,'rx')
#
# plt.figure(figsize=(6,6))
# f.plts = plt.subplots(5, sharex=True)
#
# for i in range(5):
#     plts[i].pcolor(W.eval()[:,i].reshape([36,36]))
#
#
#
# plt.show()
#
#
#
#
#
#
#
