import numpy as np
import random


def sigmoid(z):
    '''
    Activation function
    '''a
    return 1.0/(1.0 + np.exp(-z))


def sigmoid_prime(z):
    '''
    Derivative of sigmoid to be used for backpropagation
    '''
    return sigmoid(z)*(1 - sigmoid(z))


class Network:
    '''
    The main class to be used for the neural network. It is initialized by passing in
    the required neuron layers with their sizes.
    '''

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(n, 1) for n in sizes[1:]]
        self.weights = [np.random.randn(n, m)
                        for m, n in zip(sizes[:-1], sizes[1:])]

    def feedforward(self, x):
        '''
        The function that accepts inputs from previous layer neurons or the main input,
        finds the weighted sum and passes it through the activation function and then
        to the next layer.
        '''
        for w, b in zip(self.weights, self.biases):
            x = sigmoid(np.dot(w, x) + b)
        return x

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        '''
        The stochastic gradient descent algorithm for training the neural network.
        The training inputs are divided into mini batches before the training begins
        for each epoch.
        '''
        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)

        training_data = list(training_data)
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k: k + mini_batch_size]
                            for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print("Epoch {0}: {1} / {2}".format(j,
                                                    self.evaluate(test_data), n_test))
            else:
                print("Epoch {0} complete". format(j))

    def update_mini_batch(self, mini_batch, eta):
        '''
        The more essential part of the network. The errors are found and then backppropagated
        to adjust the weights and biases.
        '''
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w - (eta/len(mini_batch))*nw for w,
                        nw in zip(self.weights, nabla_w)]
        self.biases = [b - (eta/len(mini_batch))*nb for b,
                       nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        '''
        The heart of learning for this network. The cost function is calculated and changes
        to be made are returned. For more details, read aout the four equations of backpropagation.
        '''
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        activation = x
        activations = [x]
        zs = []

        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        delta = self.cost_derivative(
            activations[-1], y) * sigmoid_prime(zs[-1])

        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())

        return (nabla_b, nabla_w)

    def evaluate(self, test_data):
        '''
        The test data is evaluated to test the network and see the accuracy. Returns the total
        number of correct predictions of the network.
        '''
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]

        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        '''
        Derivative of cost function.
        '''
        return (output_activations-y)
