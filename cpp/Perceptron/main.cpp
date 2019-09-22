#include "perceptron.h"
#include <iostream>
#include <vector>
// OR Inputs { {0, 0}, { 0, 1 }, { 1, 0 }, { 1, 1 } };
// OR Outputs { 0, 1, 1, 1 };
int main()
{
	Perceptron* p = new Perceptron(0.1, pow(10, 2));
	std::vector<std::vector<float>> training_inputs = { {0, 0}, { 0, 1 }, { 1, 0 }, { 1, 1 } };//{ {0.25, 0.353}, {0.25, 0.471}, {0.5, 0.353}, {0.5, 0.647}, {0.75, 0.705}, {0.75, 0.882}, {1, 0.705}, {1, 1} };
	std::vector<float> training_targets = { 0, 1, 1, 1 };//{ 0, 1, 0, 1, 0, 1, 0, 1 };
	p->train(training_inputs, training_targets);
	p->printWeights();
	p->printChart(training_inputs, training_targets);

	std::cout << p->predict({ 0, 0 }) << std::endl;
	delete p;
}