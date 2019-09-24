#include "perceptron.h"
#include <iostream>
#include <vector>

// Sample Inputs { {0.25, 0.353}, {0.25, 0.471}, {0.5, 0.353}, {0.5, 0.647}, {0.75, 0.705}, {0.75, 0.882}, {1, 0.705}, {1, 1} };
// Sample Outputs { 0, 1, 0, 1, 0, 1, 0, 1 };

// OR Inputs { {0, 0}, { 0, 1 }, { 1, 0 }, { 1, 1 } };
// OR Outputs { 0, 1, 1, 1 };

// AND Inputs { {0, 0}, { 0, 1 }, { 1, 0 }, { 1, 1 } };
// AND Outputs { 0, 0, 0, 1 };

// XOR Inputs { {0, 0}, { 0, 1 }, { 1, 0 }, { 1, 1 } };
// XOR Outputs { 0, 1, 1, 0 };
int main()
{
	Perceptron* p1 = new Perceptron(0.1, pow(10, 2));
	Perceptron* p2 = new Perceptron(0.1, pow(10, 2));
	Perceptron* p3 = new Perceptron(0.1, pow(10, 2));
	Perceptron* p4 = new Perceptron(0.1, pow(10, 2));


	// OR 
	std::cout << "\n\nOR\n----------------" << std::endl;
	std::vector<std::vector<float>> training_inputs = { {0, 0}, { 0, 1 }, { 1, 0 }, { 1, 1 } };
	std::vector<float> training_targets = { 0, 1, 1, 1 };
	p1->train(training_inputs, training_targets);
	std::cout << "\nWeights after training: " << std::endl;
	p1->printWeights();
	p1->printChart(training_inputs, training_targets);


	// AND
	std::cout << "\n\nAND\n----------------" << std::endl;
	training_inputs = { {0, 0}, { 0, 1 }, { 1, 0 }, { 1, 1 } };
	training_targets = { 0, 0, 0, 1 };
	p2->train(training_inputs, training_targets);
	std::cout << "\nWeights after training: " << std::endl;
	p2->printWeights();
	p2->printChart(training_inputs, training_targets);


	// Sample
	std::cout << "\n\nSample\n----------------" << std::endl;
	training_inputs = { {0.25, 0.353}, {0.25, 0.471}, {0.5, 0.353}, {0.5, 0.647}, {0.75, 0.705}, {0.75, 0.882}, {1, 0.705}, {1, 1} };
	training_targets = { 0, 1, 0, 1, 0, 1, 0, 1 };
	p4->train(training_inputs, training_targets);
	std::cout << "\nWeights after training: " << std::endl;
	p4->printWeights();
	p4->printChart(training_inputs, training_targets);


	// XOR	(Perceptron will fail as XOR is not linearly separable)	See predicted and expected values
	std::cout << "\n\nXOR (Perceptron will fail as XOR is not linearly separable) See predicted and expected values" << std::endl;
	std::cout << "----------------------------------------------------------------------------------------------------" << std::endl;
	training_inputs = { {0, 0}, { 0, 1 }, { 1, 0 }, { 1, 1 } };
	training_targets = { 0, 1, 1, 0 };
	p3->train(training_inputs, training_targets);
	std::cout << "\nWeights after training: " << std::endl;
	p3->printWeights();
	p3->printChart(training_inputs, training_targets);


	delete p1, p2, p3;
}