# Rohith Ravindranath
# March 10 2019
# K-Means Clustering Algorithm

import pandas as pd
import numpy as np
from sys import argv
import operator
import random


class KMeans:

    def read_data(self, file_name):
        data = pd.read_csv(file_name, header = None)
        data.columns = ['image_id' , 'class_label', 'feature_1', 'feature_2']
        return data

    def should_continue(self,iterations,iter_count,centriods, old_centroids ):
        if iterations >= iter_count:
            return False
        if centriods == old_centroids:
            return False
        return True

    def get_new_centriods(self, clusters):
        centriods = []
        for key in clusters.keys():
            x = []
            y = []
            lis = clusters[key]
            for id in lis:
                x.append(float(data.loc[data['image_id']== id]['feature_1']))
                y.append(float(data.loc[data['image_id']== id]['feature_2']))
            centriods.append((sum(x) / len(x) , sum(y) / len(y) )  )
        return centriods

    def calculate_distance(self, point, centriod):
        x = np.array(list(point))
        y = np.array(list(centriod))
        return np.sqrt(sum((x - y) ** 2))

    def cluster_points(self, data,centriods):
        dict = {}
        for centriod in centriods:
            dict[centriod] = []
        for index, row in data.iterrows():
            id = data.loc[index]['image_id']
            point = (data.loc[index]['feature_1'], data.loc[index]['feature_2'])
            temp_dict = {}
            for centriod in centriods:
                distance  = self.calculate_distance(point, centriod)
                temp_dict[centriod] = distance
            sorted_x = sorted(temp_dict.items(), key=operator.itemgetter(1))
            desired_point = sorted_x[0]
            dict[desired_point[0]].append(data.loc[index]['image_id'])
        return dict

    def get_inital_centroids(self, k, data):
        lis = data['image_id'].tolist()
        lis_ids = random.sample(lis, k)
        centriods = []
        for id in lis_ids:
            centriods.append((float(data.loc[data['image_id']== id]['feature_1']), float(data.loc[data['image_id']== id]['feature_2'])))
        return centriods

    def cluster(self, data, k, centriods = None, iter_count = -1):
        iterations = 0
        old_centroids = []
        clusters = []
        if iter_count == -1:
            iter_count = float('inf')
        if centriods == None:
            centriods = self.get_inital_centroids(k, data)
        else:
            lis = []
            for centriod in centriods:
                lis.append((float(data.loc[data['image_id']== centriod]['feature_1']), float(data.loc[data['image_id']== centriod]['feature_2'])))
            centriods = lis
        while self.should_continue(iterations,iter_count,centriods, old_centroids):
            print(str(iterations) + ' ' + str(iter_count))
            print(centriods)
            old_centroids = centriods
            clusters = self.cluster_points(data,centriods)
            centriods = self.get_new_centriods(clusters)
            iterations += 1
        return clusters

if len(argv) < 3 or len(argv) > 5:
    print('Usage: python3 KMeans.py [file_name] [k] [ *optional* centriods] [ *optional* iter_count]')
    exit()
file_name = argv[1]
k = int(argv[2])
centriods = None
iter_count = -1
if len(argv) == 4:
    x = argv[3]
    if x.isdigit():
        iter_count = int(x)
    else:
        centriods = argv[3].split(',')
elif len(argv) == 5:
    centriods = argv[3].split(',')
    iter_count = argv[4]

kn = KMeans()
data = kn.read_data(file_name)
cluters = []
if len(argv) == 4:
    if not argv[3].isdigit() and k != len(centriods):
        print('ERROR: Length of centriods input not equal to k')
        exit()
    if not argv[3].isdigit():
        clusters = kn.cluster(data, k, centriods = centriods)
    else:
        clusters = kn.cluster(data, k, iter_count = iter_count)
elif len(argv) == 5:
    if k != len(centriods):
        print('ERROR: Length of centriods input not equal to k')
        exit()
    clusters = kn.cluster(data, k, centriods, iter_count)
else:
    clusters = kn.cluster(data, k)
print(clusters)
