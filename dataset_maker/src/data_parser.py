'''
Program to parse the image dataset created using dataset_maker using pickle.
By default, the pickled file is saved to the dataset folder in the previous dir.
skimage(scikit-image) is used to conver the images from RGB to Greyscale format as
it is enough.
'''

import os
import pickle
import random
import numpy as np
from skimage import color, io
from collections import defaultdict

path = "../data/"
train_data = [[], []]
test_data = [[], []]
sets = defaultdict(list)

# Label and corresponding number for data validation.
results = {
    'plus': 0,
    'minus': 1,
    'multiply': 2,
    'divide': 3
}

percentage_training_data = 90
percentage_test_data = 10

# Each image is opened and stored into a dictionary
for fName in os.listdir(path):
    img = io.imread(path + fName)
    greyscale = color.rgb2gray(img)
    sets[fName.split('_')[0]].append(greyscale)

# The label and corresponding data are stored into a list
# for training data and test data.
for label, datas in sets.items():
    random.shuffle(datas)
    separator = int((percentage_training_data/100) * len(datas))
    for data in datas[:separator]:
        train_data[0].append(data)
        train_data[1].append(results[label])

    for data in datas[separator:]:
        test_data[0].append(data)
        test_data[1].append(results[label])

# The data is randomly shuffled
combined = list(zip(train_data[0], train_data[1]))
random.shuffle(combined)
train_data[0][:], train_data[1][:] = zip(*combined)

combined = list(zip(test_data[0], test_data[1]))
random.shuffle(combined)
test_data[0][:], test_data[1][:] = zip(*combined)

print(len(train_data[0]), len(train_data[1]))
print(len(test_data[0]), len(test_data[1]))

# Finally the lists are dumped into a pickle file
with open("../dataset/parsed.pkl", "wb") as f:
    pickle.dump([train_data, test_data], f)


print("Parsing done.")
