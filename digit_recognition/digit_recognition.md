# Digit Recognition

These are a set of python code to implement a feedforward neural network for the recognition
of handwritten digits. 
The dataset used is the MNIST Dataset and the code was written with reference to the code 
from Michael Nielssen's Neural Networks and Deep Learning web book and github repo.


## How to use:

The parameters of the network can be changed to improve accuracy.
Pull up terminal or cmd and open up the python IDE in the src directory
Now type the following script:

```
>>> import data_loader
>>> import network
>>> training_data, validation_data, test_data = data_loader.load_data_wrapper()
>>> net = network.Network([784, 30, 4])
>>> net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
```
After the SGD function is called, the network should start to train and the results for the test data
for each epoch should start printing. 
Do note that this may take minutes depending upon your CPU/GPU and the network parameters.


## References:

* Yotube series made by 3blue1brown on neural networks and deep learning
* Neural Networks and Deep Learning, Michael Nielssen
* Michael Nielssen's code: https://github.com/mnielsen/neural-networks-and-deep-learning
