# Mathematical Operators Recognition
-------------------------------

These are a set of python code to implement a feedforward neural network for the recognition
of the 4 main mathematical operators(+, -, x, /). 
The dataset used is the one I created using my dataset_maker app and the code was written with 
reference to the code from Michael Nielssen's Neural Networks and Deep Learning web book and github repo.
This was made to test the importance of good data for machine learning and the tweaking of parameters
to increase a model's accuracy.

## How to use:
-------------------------------
The parameters of the network can be changed to improve accuracy.
Pull up terminal or cmd and open up the python IDE in the src directory
Now type the following script:

```
>>> import data_loader
>>> import network
>>> training_data, test_data = data_loader.load_data_wrapper()
>>> net = network.Network([784, 100, 4])
>>> net.SGD(training_data, 50, 10, 0.1, test_data=test_data)
```
After the SGD function is called, the network should start to train and the results for the test data
for each epoch should start printing. 
Do note that this may take minutes depending upon your CPU/GPU and the network parameters.


## References:
-------------------------------
* Yotube series made by 3blue1brown on neural networks and deep learning
* Neural Networks and Deep Learning, Michael Nielssen
* Michael Nielssen's code: https://github.com/mnielsen/neural-networks-and-deep-learning
