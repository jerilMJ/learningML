import numpy as np

class Perceptron:
    
    def __init__(self, eta, epoch):
        self.eta = eta
        self.epoch = epoch
        self.weights = np.random.rand(3)
        
    def netInput(self, X):
        weightedSum = self.weights[0]
        for i in range(len(X)):
            weightedSum += X[i] * self.weights[i+1]
        return weightedSum
    
    def predict(self, X):
        weightedSum = self.netInput(X)
        return 1 if weightedSum > 0 else 0
    
    def train(self, trainingBatch, targets):
        for _ in range(self.epoch):
            for inputSet, target in zip(trainingBatch, targets):
                prediction = self.predict(inputSet)
                update = self.eta * (target - prediction)
                self.weights[0] += update
                for index, input_ in enumerate(inputSet):
                    self.weights[index + 1] += update * input_
        
p = Perceptron(0.1, 100)
p.train([ [0, 0], [0, 1], [1, 0], [1, 1] ], [ 0, 1, 1, 1 ])
print(p.predict([0,0]))
