#pragma once
#include <vector>

class Perceptron {

public:
	Perceptron(float eta, int epoch);
	float netInput(std::vector<float> X);
	int predict(std::vector<float> X);
	void train(std::vector<std::vector<float>> X, std::vector<float> Y);
	void printWeights();
	void printChart(std::vector<std::vector<float>> X, std::vector<float> Y);

private:
	float m_eta;
	int m_epoch;
	std::vector<float> m_w;

};