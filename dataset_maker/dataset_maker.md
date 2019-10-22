# Dataset Maker v1.0
### Made By: jerilMJ

This is a pyQt GUI application to create training and test images for
use with neural networks. I made this just for fun and to test if I could
make a dataset and use it to train my neural network in identifying certain
mathematical operators.

The app uses data augmentation in the form of rotation and specific translations
to generate duplicate but transformed images to decrease the time required to build
a dataset.

After opening, the user needs to first type a label for the data. Then they can start drawing.
After drawing, they may wish to choose what all transformations to apply to augment the data.
Options are available to save, clear the canvas, eliminate duplicate images, undo the last save
and count the number of labels created. Most of the tasks are autonomous and thus the user only
needs to draw each image and apply transformations and click save.

If the label is given, clicking the save button will save the created image into the specified
directory in the source code.

CLicking the clear button clears the canvas.

Clicking the eliminate dupes button initializes the function of eliminating dupes by comparing
the md5 checksums of each file. This might be taxing on the program if the dataset is very huge.

If undo last save button is clicked, it will delete the images last saved during the current
session. This can be useful if you spot any mistakes in your drawing.

Count labels button prints out the number of items of each label.

The label numbers are generated smartly so there is no need to be concerned about overwriting
other saves.


## Changelog:

* v1.0: Deployed app with initial features(save, clear, eliminate dupes, undo last save and count labels)
