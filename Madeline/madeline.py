import numpy as np

class Neural_Network:

	def __init__(self, n_in:int=1, n_out:int=1, depth:int=1, width:int=1, activation:function=lambda x: 1 if x>0 else 0):
		self.input_size=n_in
		self.output_size=n_out
		self.hidden_size=width
		self.hidden_depth=depth
		self.activation = activation
		
		self.weights_input_hidden = np.random.randn(n_in, width)
		self.weights_hidden_hidden = np.array([np.random.rand(width, width) for i in range(depth-1)])
		self.weights_hidden_output = np.random.randn(width, n_out)

		self.bias_hidden = np.zeros(depth, 1, width)
		self.bias_output = np.zeros(1, n_out)

	def feed_forw(self, X):
		res = np.dot(X, self.wights_input_hidden)+self.bias_hidden[0]
		res = self.activation(res)
		
		for n_layer in range(self.hidden_depth-1):
			res = np.dot(res, self.weights_hidden_hidden[n_layer])+self.bias_hidden[n_layer+1]

		res = np.dot(res, self.weights_hidden_output)+self.bias_output
		res = self.activaction(res)

	def backprop(self):
		pass

	def train(self):
		pass