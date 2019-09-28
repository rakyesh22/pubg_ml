import tensorflow as tf
import numpy as np
from tensorflow.keras import layers
from tensorflow.keras.backend import set_session

def init():
	sess = tf.Session()
	set_session(sess)
	loaded_model = tf.keras.Sequential()
	loaded_model.add(layers.Dense(10, activation='relu', input_dim=23))
	loaded_model.add(layers.Dense(10, activation='relu'))
 	loaded_model.add(layers.Dense(2, activation='softmax'))
	training = np.genfromtxt('/root/training.csv', delimiter=",")
	labels = np.genfromtxt('/root/labels.csv', delimiter=",")
	loaded_model.compile(optimizer=tf.train.AdamOptimizer(0.001), loss='categorical_crossentropy', metrics=['accuracy'])
	loaded_model.fit(training, labels, epochs=0)
	loaded_model.load_weights('/root/pubg_model_weights.h5')
	graph = tf.get_default_graph()
	return loaded_model, graph, sess
