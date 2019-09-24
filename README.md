# learningML
This repo will contain all code that I write as I learn the basics and intermediates of AI and its subsets (Neural Networks, Deep Learning etc..). The code you find may be subject to further optimization with time.
**Please forgive my wacky MS Paint skills..**


## **Perceptron:**

The perceptron is one of the old but basic unit of a neaural network. The algorithm was developed first by Frank Rosenblatt and was made to be a linear classifier between two classes.
i.e, it can predict whether or not an element belongs to one class or another after it is trained to do so.

The basic idea is that while training, the perceptron adjusts its knobs through mathematical equations to adjust a line that separates the two classes. Consider it as a see-saw in space,
swinging up and down, changing its slope, all the while being displaced. 

for eg., consider the OR gate used in logical circuits.
Let X and Y be the inputs.

![OR Truth Table](/assets/OR.png)

Picture the inputs on a 2D plane like so:

![Inputs Graph](/assets/Inputs.png)

An OR gate produces linearly classifiable outputs. The output of the points above the line of separation is 1 and for those below, the output is 0.
This is the desired target of our perceptron:

![OR Graph](/assets/OrTrained.png)

But our perceptron does not know this. It starts with the line of separation at a random point on the 2D plane with random orientations.

![Random Line](/assets/Random.png)

As we adjust the knobs (weights and biases) of the perceptron, we can reach the desired target.

![Training Graphs](/assets/Training.png)

This is the basic visualization of how a perceptron learns.
So how do the knobs get adjusted? It's the work of some savvy Maths which is beyond the scope of this text file. 

Now we can do the same with an AND gate since it also produces linearly seperable outputs.

![AND Graph](/assets/AndTrained.png)

.
.
.

So far, we've seen some great things from a single perceptron but it has some limitations. It cannot classify linearly non-seperable outputs as in the case of an XOR gate.
If you try training a single perceptron to classify XOR outputs, it will produce erroneous results. Why? Lets see:

This is the truth table for an XOR gate:

![XOR Gate](/assets/XOR.png)

We can deduce that for separating the outputs we need such a configuration:

![XOR Graph](/assets/XorTrained.png)

So we need two lines(see-saws) to classify outputs for XOR. This means that we need one more perceptron.
That's where the 'network' in Neural Networks comes from! It's a fascinating topic!




