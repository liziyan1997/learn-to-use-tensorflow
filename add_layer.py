import tensorflow as tf


def add_layer(inputs, in_size, out_size, activation_function=None):
    weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1) #在机器学习中，biases的推荐值不为0，所以我们这里是在0向量的基础上又加了0.1。
    wx_plus_b = tf.matmul(inputs, weights) + biases

    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)

    return outputs
