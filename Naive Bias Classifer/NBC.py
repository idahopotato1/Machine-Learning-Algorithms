# Rohith Ravindranath
# Naive Bias Classifer
# March 10 2019

import pandas as pd
import numpy as np
from sys import argv

class NBClassifier:

    def read_data(self, file_name):
        data = pd.read_excel(file_name)
        return data

    def calculate_probability(self, buy, day, discount, delivery):
        day_given_buy_p = len(data.loc[(data['Purchase'] == buy) & (data['Day'] == day) ]) /len(data.loc[(data['Purchase'] == buy) ])
        discount_given_buy_p = len(data.loc[(data['Discount'] == discount) & (data['Purchase'] == buy) ]) /len(data.loc[(data['Purchase'] == buy)])
        delivery_given_buy_p = len(data.loc[(data['Free Delivery'] == delivery) & (data['Purchase'] == buy) ]) /len(data.loc[(data['Purchase'] == buy) ])
        buy_p = len(data.loc[ data['Purchase'] == buy ])  / len(data)
        day_p = len(data.loc[ (data['Day'] == day) ]) / len(data)
        discount_p = len(data.loc[(data['Discount'] == discount) ]) /  len(data)
        delivery_p = len(data.loc[(data['Free Delivery'] == delivery)  ]) / len(data)
        probability = (day_given_buy_p * discount_given_buy_p * delivery_given_buy_p * buy_p ) / (day_p * discount_p * delivery_p )
        return probability

    def classify(self, day, discount, delivery):
        yes_p = self.calculate_probability( 'Yes', day, discount, delivery)
        no_p = self.calculate_probability( 'No', day, discount, delivery)
        total_p = yes_p + no_p
        yes_p = yes_p / total_p
        no_p = no_p / total_p
        return yes_p*100,no_p*100

if len(argv) != 5:
    print('USAGE: python3 NBC.py [file_name] [Buy? Yes or No] [Day? Weekday or Weekend or Holiday] [Discount? Yes or No] [Free Delivery? Yes or No]')
    exit()
file_name = argv[1]
day = argv[2]
discount = argv[3]
delivery = argv[4]

nbc = NBClassifier()
data = nbc.read_data(file_name)
yes,no = nbc.classify(day,discount,delivery)
print('Likelihood of Purchase: ' + str(round(yes, 2)) + '%')
print('Likelihood of No Purchase: ' + str(round(no, 2)) + '%')
