# Rohith Ravindranath
# Language Modeling Script
# March 09 2019

from sys import argv
import re
import operator

class LanguageModel:


    def __init__(self, input_file, n):
        self.global_lines = self.read_data(input_file)
        self.global_lines = self.cleaned_data(self.global_lines)
        self.n = n

    def read_data(self, file_name):
        lines = []
        final_lines = []
        with open(file_name) as f:
            lines = f.read().splitlines()
        for line in lines:
            for l in line.split(' s '):
                final_lines.append('<s> ' + l)
        return final_lines

    def cleaned_data(self, data):
        for x in range(len(data)):
            data[x] = data[x].lower()
        return data

    def build_n_gram_dict(self,n,clean_data):
        dict = {}
        for line in clean_data:
            word_array = line.split()
            for x in range(len(word_array) - (n-1)):
                s = ' '.join(word_array[x:x+(n)])
                if s in dict.keys():
                    dict[s] = dict[s] + 1
                else:
                    dict[s] = 1
        return dict

    def calculate_PP(self, n_gram_models):
        V = len(n_gram_models[1].keys())
        P_list = []
        for line in self.global_lines:
            P = 1
            word_array = line.split()
            if len(word_array) <= self.n:
                z = 2
                while z != len(word_array):
                    s1 = ' '.join(word_array[:z])
                    s2 = ' '.join(word_array[:z-1])
                    P *= (n_gram_models[z][s1] + 1) / (n_gram_models[z-1][s2] + V)
                    y += 1
                    z += 1
            else:
                y = 2
                while y != self.n:
                    s1 = ' '.join(word_array[:y])
                    s2 = ' '.join(word_array[:y-1])
                    P *= (n_gram_models[y][s1] + 1) / (n_gram_models[y-1][s2] + V)
                    y += 1
                for x in range(len(word_array) - (self.n-1)):
                    s1 = ' '.join(word_array[x:x+(self.n)])
                    s2 = ' '.join(word_array[x:x+(self.n-1)])
                    P *= (n_gram_models[self.n][s1] + 1) / (n_gram_models[self.n-1][s2] + V)
            P_list.append(P)
        return sum(P_list) / len(P_list)

    def train_model(self):
        predictated_dict = {}
        #self.global_lines = ['<s> if it talks like a duck walks like a duck it’s a duck']
        for x in range(self.n):
            y = x + 1
            predictated_dict[y] = self.build_n_gram_dict(y,self.global_lines)
        return predictated_dict

    def test_model(self, dict):
        return lm.calculate_PP(predictated_dict)

    def generate_text(self, n_gram_models, text_length, seed_word):
        text = '<s> ' + str(seed_word)
        words = n_gram_models[1].keys()
        V = len(n_gram_models[1].keys())
        while len(text.split()) < text_length:
            dict = {}
            text_1_count = 0
            text_2_count = 0
            for word in words:
                if len(text.split()) < self.n:
                    text1 = text
                    text2 = text + ' ' + str(word)
                else:
                    text1 = text.split()
                    text1 = ' '.join(text1[-1 * (self.n-1):])
                    text2 = text1 + ' ' + str(word)
                try:
                    text_1_count = n_gram_models[len(text1.split())][text1]
                except KeyError:
                    text_1_count = 0
                try:
                    text_2_count = n_gram_models[len(text2.split())][text2]
                except KeyError:
                    text_2_count = 0
                p = (text_2_count + 1) / (text_1_count + V)
                dict[text2] = p
            sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
            if len(text.split()) < self.n:
                text = str(sorted_x[-1][0])
            else:
                text3 = text.split()
                text3 = ' '.join(text3[0:-1 * (self.n - 1)])
                text = text3 + ' ' + str(sorted_x[-1][0])
        return text

input_file = argv[1]
K = int(argv[2])
length_sen = int(argv[3])
seed_word = argv[4]
lm = LanguageModel(input_file, K)
print('Training Model...')
predictated_dict = lm.train_model()
print('Generating Text...')
sentence = lm.generate_text(predictated_dict,length_sen,seed_word)
print(sentence)
#print('Testing Model...')
#pp = lm.test_model(predictated_dict)
#print(pp)
