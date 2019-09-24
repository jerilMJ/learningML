'''
The perceptron is one of the old basic unit of a Neural Network. 
See: https://en.wikipedia.org/wiki/Perceptron

The code below is for creating a single perceptron and training it to classify linearly seperable inputs.
The inputs given are OR, AND, a sample and XOR of which the first 3 are linearly seperable but the last is not (XOR).

The aim of this program is to test the limitations of a single Perceptron and understand that:
One perceptron alone can do only so much but with multiple perceptrons linked to each other, we can overcome the limitation of
linear separation.

References: Neural Networks, Fuzzy Logic and Evolutionary Algorithms, S. Rajasekaran, G.A Vijayalakshmi Pai
			https://towardsdatascience.com/perceptron-the-artificial-neuron-4d8c70d5cc8d
'''

import numpy as np

# Sample Inputs [ [0.25, 0.353], [0.25, 0.471], [0.5, 0.353], [0.5, 0.647], [0.75, 0.705], [0.75, 0.882], [1, 0.705], [1, 1] ]
# Sample Outputs [ 0, 1, 0, 1, 0, 1, 0, 1 ]

# OR Inputs [ [0, 0], [0, 1], [1, 0], [1, 1] ]
# OR Outputs [ 0, 1, 1, 1 ]

# AND Inputs [ [0, 0], [0, 1], [1, 0], [1, 1] ]
# AND Outputs [ 0, 0, 0, 1 ]

# XOR Inputs [ [0, 0], [0, 1], [1, 0], [1, 1] ]
# XOR Outputs [ 0, 1, 1, 0 ]

class Perceptron:
    def __init__(self, eta, epoch):
        self.eta = eta
        self.epoch = epoch
        self.weights = np.random.rand(3)
    
    def netInput(self, X):		# Finding the weighted sum and adding the bias
        weightedSum = self.weights[0]
        for i in range(len(X)):
            weightedSum += X[i] * self.weights[i+1]
        return weightedSum
    
    def predict(self, X):		# Activation function used is the Heaviside Step Function
        weightedSum = self.netInput(X)
        return 1 if weightedSum > 0 else 0
    
    def train(self, trainingBatch, targets):	# The place where the magic happens
        for _ in range(self.epoch):
            for inputSet, target in zip(trainingBatch, targets):
                prediction = self.predict(inputSet)
                update = self.eta * (target - prediction)
                self.weights[0] += update
                for index, input_ in enumerate(inputSet):
                    self.weights[index + 1] += update * input_

    def printChart(self, inputs, targets):		# For printing a table of expected and predicted values in a neat format
        headers = '{:>15} {:>15} {:>15} {:>15}'.format("X1", "X2", "Predicted", "Expected")
        print(headers)
        for datas, target in zip(inputs, targets):
            for data in datas:
                print('{:>15}'.format(data), end = '')
            print('{:>15}'.format(self.predict(datas)), end='')
            print('{:>15}'.format(target))
	
	
# OR	
print('\n\nOR\n')
training_inputs = [ [0, 0], [0, 1], [1, 0], [1, 1] ]
training_targets = [ 0, 1, 1, 1 ]
p1 = Perceptron(0.1, 100)
p1.train(training_inputs, training_targets)
p1.printChart(training_inputs, training_targets)

# AND
print('\n\nAND\n')
training_inputs = [ [0, 0], [0, 1], [1, 0], [1, 1] ]
training_targets = [ 0, 0, 0, 1 ]
p2 = Perceptron(0.1, 100)
p2.train(training_inputs, training_targets)
p2.printChart(training_inputs, training_targets)

# Sample
print('\n\nSample\n')
training_inputs = [ [0.25, 0.353], [0.25, 0.471], [0.5, 0.353], [0.5, 0.647], [0.75, 0.705], [0.75, 0.882], [1, 0.705], [1, 1] ]
training_targets = [ 0, 1, 0, 1, 0, 1, 0, 1 ]
p3 = Perceptron(0.1, 100)
p3.train(training_inputs, training_targets)
p3.printChart(training_inputs, training_targets)

# XOR
print('\n\nXOR (Perceptron fails as XOR is not linearly separable) See predicted and expected values.\n')
training_inputs = [ [0, 0], [0, 1], [1, 0], [1, 1] ]
training_targets = [ 0, 1, 1, 0 ]
p4 = Perceptron(0.1, 100)
p4.train(training_inputs, training_targets)
p4.printChart(training_inputs, training_targets)
