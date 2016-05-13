import numpy as np
import tensorflow as tf

image_size = 28
num_labels = 10

def placeholder_input():
	images_placeholder = tf.placeholder(tf.float32, shape=(None, image_size, image_size, 1))
	labels_placeholder = tf.placeholder(tf.float32, shape=(None, num_labels))

	return images_placeholder, labels_placeholder

def weight_variable(shape):
	initial = tf.truncated_normal(shape, stddev=0.1)
	return tf.Variable(initial)

def bias_variable(shape):
	initial = tf.constant(0.1, shape=shape)
	return tf.Variable(initial)

def conv2d(x, W):
	return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
	return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

def inference(images):
	# Convolutional layer 1
	W_conv1 = weight_variable([5, 5, 1, 20])
	b_conv1 = bias_variable([20])

	h_conv1 = tf.nn.relu(conv2d(images, W_conv1) + b_conv1)

	h_pool1 = max_pool_2x2(h_conv1)

	# Convolutional layer 2
	W_conv2 = weight_variable([5, 5, 20, 40])
	b_conv2 = bias_variable([40])

	h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)

	h_pool2 = max_pool_2x2(h_conv2)

	# Fully connected layer
	W_fc1 = weight_variable([7 * 7 * 40, 150])
	b_fc1 = bias_variable([150])

	h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 40])
	h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

	# Linear layer
	W_fc2 = weight_variable([150, 10])
	b_fc2 = bias_variable([10])

	logits = tf.matmul(h_fc1, W_fc2) + b_fc2

	return logits

def loss_op(logits, labels):
	loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits, labels))

	return loss	

def train_op(loss, learning_rate):
	optimizer = tf.train.AdamOptimizer(learning_rate)
	train = optimizer.minimize(loss)

	return train

def accuracy(predictions, labels):
	correct_prediction = tf.equal(tf.argmax(predictions, 1), tf.argmax(labels, 1))

	return tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

if __name__ == '__main__':
	pass

