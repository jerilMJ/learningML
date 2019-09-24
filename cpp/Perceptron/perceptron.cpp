#include <iostream>
#include <iomanip>
#include "perceptron.h"

Perceptron::Perceptron(float eta, int epoch)
{
	srand(time(NULL));
	m_epoch = epoch;
	m_eta = eta;
}

float Perceptron::netInput(std::vector<float> X)
{
	float bias = m_w[0];
	float weightedSum = 0;
	for (int i = 0; i < X.size(); i++)
	{
		weightedSum += X[i] * m_w[i + 1];
	}
	weightedSum += bias;
	return weightedSum;
}

int Perceptron::predict(std::vector<float> X)
{
	return netInput(X) > 0 ? 1 : 0;	// Activation function (Heaviside Step Function)
}

void Perceptron::train(std::vector<std::vector<float>> X, std::vector<float> Y)
{
	for (int i = 0; i < X[0].size() + 1; i++)
	{
		float r = ((double)rand() / (RAND_MAX));
		m_w.push_back(r);
	}
	std::cout << "Weights before training (random): " << std::endl;
	printWeights();
	for (int i = 0; i < m_epoch; i++)
	{
		for (int j = 0; j < X.size(); j++)
		{
			int prediction = predict(X[j]);
			float update = m_eta * (Y[j] - prediction);
			m_w[0] += update;	// updating bias
			for (int k = 1; k < m_w.size(); k++)
			{
					m_w[k] += update * X[j][k - 1];
			}
		}
	}
	
}

void Perceptron::printWeights()
{
	for (int i = 0; i < m_w.size(); i++)
	{
		std::cout << m_w[i] << std::endl;
	}
}

void Perceptron::printChart(std::vector<std::vector<float>> X, std::vector<float> Y)
{
	int width = 15;
	std::cout << "\nChart of inputs & outputs: " << std::endl;
	std::cout << std::setw(width) << "X1" << std::setw(width) << "X2" << std::setw(width) << "Predicted" << std::setw(width) << "Expected" << std::endl;
	for (int i = 0; i < X.size(); i++)
	{
		for (int j = 0; j < X[0].size(); j++)
		{
			std::cout << std::setw(width) << X[i][j];
		}
		std::cout << std::setw(width) << predict(X[i]) << std::setw(width) << Y[i] << std::endl;
	}
	
}