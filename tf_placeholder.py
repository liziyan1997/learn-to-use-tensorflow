#How to use placeholder

import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

#output = tf.multiply(input1,input2)
output = input1*input2

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[3.5],input2:[4.]}))