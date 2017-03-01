"""
Simple

"""

import tensorflow as tf

a = tf.constant(1)
b = tf.constant(2)

c = a+b
d= a*b

v1 = tf.constant([1.,2.])
v2 = tf.constant([3.,4.])

M = tf.constant([[1.,2.]])
N = tf.constant([[1.,2.],[3.,4.]])
K = tf.constant([[[1.,2.],[3.,4.]]])

v3= v1+v2
M2= M*M
NN = tf.matmul(N, N)

sess = tf.Session()

output = sess.run(NN)

print(output)

sess.close()

sess = tf.InteractiveSession()
print ("M2 is {}".format(M2.eval()))

W = tf.Variable(0, name="weight")

init_op = tf.global_variables_initializer()
sess.run(init_op)

print ("W is {}".format(W.eval()))

W +=a

print ("W after adding a")
print (W.eval())

W+=a
print ("W after adding a again")
print (W.eval())



E = d + b

print ("E is ")
print (E.eval())

print (" E and d: ")

print (sess.run([E,d]))