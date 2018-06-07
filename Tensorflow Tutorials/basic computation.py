import tensorflow as tf 
import numpy as np 

#create data
xdata = np.random.rand(100).astype(np.float32)
ydata = xdata*0.1 + 0.3

# create tensorflow structure start
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0)) # gen 1 param btn -1 and 1
biases = tf.Variable(tf.zeros([1]))

y = Weights*xdata + biases

loss = tf.reduce_mean(tf.square(y-ydata))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables() #important

#create tensorflow structure end

sess = tf.Session() #points to what you want to run in graph
sess.run(init)	

for step in range(201):
	sess.run(train)
	if step%20 == 0 :
		print(step,sess.run(Weights),sess.run(biases))