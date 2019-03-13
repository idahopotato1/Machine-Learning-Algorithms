# Perceptron
The perceptron is an algorithm for supervised learning of binary classifiers. A binary classifier is a function which can decide whether or not an input, represented by a vector of numbers, belongs to some specific class. It is a type of linear classifier, i.e. a classification algorithm that makes its predictions based on a linear predictor function combining a set of weights with the feature vector.

## Application 
My version of the perceptron takes 4-inputs and a static bias in order to classify the input as a plant. There are three avaiable classifiers: setosa, versicolor, and virginica. When running the script, you will have to pick two of the tree classifiers for the perceptron.

## Usage
python3 Perceptron.py [file_name] [class_1] [class_2] [training_percent]

[file_name]: the iput file with the labeled data i.e. iris.csv

[class_1]: First class for the perceptron to classify

[class_2]: Second class for the perceptron to classify

[training_percent]: percentage of data from each class to train the weights, the rest will be used a testing data