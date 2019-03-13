# Rohith Ravindranath
# March 12 2019
# Perceptron

from sys import argv
import pandas as pd
import numpy as np
import operator

class Perceptron:

    def read_data(self, file_name):
        data = pd.read_csv(file_name)
        data.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width' , 'Species']
        return data

    def process_data(self, data, class_1, class_2, training_percent):
        data['Bias'] = 1
        data = data.loc[(data['Species'] == class_1) | (data['Species'] == class_2) ]

        class_1_data = data.loc[(data['Species'] == class_1)]
        class_1_data = class_1_data.drop(columns=['Species'])
        class_1_data['Species'] = 1

        class_2_data = data.loc[(data['Species'] == class_2)]
        class_2_data = class_2_data.drop(columns=['Species'])
        class_2_data['Species'] = 0


        class_1_training_cutoff = int((training_percent / 100) * len(class_1_data))
        class_1_training = class_1_data[ :class_1_training_cutoff]
        class_1_testing_cutoff = int((( training_percent) / 100) * len(class_1_data))
        class_1_testing =class_1_data[class_1_testing_cutoff :]

        class_2_training_cutoff = int((training_percent / 100) * len(class_2_data))
        class_2_training = class_2_data[ :class_2_training_cutoff]
        class_2_testing_cutoff = int((( training_percent) / 100) * len(class_2_data))
        class_2_testing =class_2_data[class_2_testing_cutoff :]

        training_data = pd.concat([class_1_training, class_2_training])
        testing_data = pd.concat([class_1_testing, class_2_testing])
        return training_data, testing_data

    def predict(self, inputs, weights):
        activation = 0.0
        for x in range(len(inputs)):
            activation += inputs[x] * weights[x]
        if activation >= 0.0:
            return 1.0
        else:
            return 0.0

    def check_accuracy(self, data, weights):
        correct = 0.0
        for index, row in data.iterrows():
            lis = list(data.loc[index])[:-1]
            pred = self.predict(lis, weights)
            if pred == list(data.loc[index])[-1]:
                correct += 1.0
        return correct/ float(len(data))

    def train_perceptron(self, data, weights, epoch = 10, rate = 1.0, stop_early = True):
        p_accuracy = self.check_accuracy(data,weights)
        p_weights = weights
        for iter in range(epoch):
            curr_accuracy = self.check_accuracy(data,weights)
            if curr_accuracy < p_accuracy and stop_early:
                weights = p_weights
                break
            else:
                p_accuracy = curr_accuracy
                p_weights = weights
            if curr_accuracy == 1.0 and stop_early:
                break
            for index,row in data.iterrows():
                lis = list(data.loc[index])[:-1]
                pred = self.predict(lis, weights)
                err = list(data.loc[index])[-1] - pred
                for x in range(len(weights)):
                    weights[x] = weights[x] + (rate*err*lis[x])
        return weights

if len(argv) != 5:
    print('USAGE: python3 Perceptron.py [file_name] [1st class] [2nd class] [training percent]')
    exit()
if not argv[4].isdigit():
    print('USAGE: python3 Perceptron.py [file_name] [1st class] [2nd class] [training percent]')
    exit()
file_name = argv[1]
class_1 = argv[2]
class_2 = argv[3]
training_percent = int(argv[4])
perceptron = Perceptron()
data = perceptron.read_data(file_name)
training_data, testing_data = perceptron.process_data(data,class_1, class_2, training_percent)
weights = perceptron.train_perceptron(training_data,[1.00,1.00,1.00,1.00, 0.20])
accuracy = perceptron.check_accuracy(testing_data,weights)
print(str(accuracy*100) + '%')
