import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

path = "../data/"
train_data = []
train_set = []

count = 0

for fName in os.listdir(path):
    img = plt.imread(path+fName)
    plt.imshow(img)
    train_set.append(img)
    train_set.append(fName.split('_')[0])
    train_data.append(train_set)
    train_set = []

with open("../dataset/parsed.pkl", "wb") as f:
    pickle.dump(train_data, f)

