import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD
import numpy as np


class NeuralNet():

	def __init__(self):
		self.model = self.create_neural_model()


	def create_neural_model(self):
		model = Sequential()
		model.add(Dense(4, input_shape = (5,), activation='relu'))
		model.add(Dense(2, activation="softmax"))
		model.compile(SGD(lr= .2), "mse")

		return model


	def predict(self, input):
		input = np.expand_dims(input, axis = 0)
		return self.model.predict(input)[0]

