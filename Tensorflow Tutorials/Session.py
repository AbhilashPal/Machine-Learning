import tensorflow as tf 
import numpy as np 

mat1 = tf.constant([[3,3]]) # a 1x2 matrix 
mat2 = tf.constant([[2],	# a 2x1 matrix
					[2]])
product = tf.matmul(mat1,mat2) #np.dot(m1,m2)

#method 1
sess = tf.Session()
result1 = sess.run(product)
print(result1)
sess.close()

#method 2
with tf.Session() as sess:
	result2 = sess.run(product)
	print(result2)