# 4

import numpy as np

import pandas as pd

Phones = pd.read_csv("C:\\Users\\WIN10\\Desktop\\LEARNING\\myphonedata.csv")

Phones.columns #to get the column names

# To drop the unwanted  repeated columns

Phones1=Phones.drop(["V1","V2","V3"],axis=1)

Phones_list = []

for i in Phones1:

    Phones_list.append(i.split(","))

all_Phones_list = [i for item in Phones_list for i in item]

from collections import Counter 

item_frequencies = Counter(all_Phones_list)

# after sorting

item_frequencies = sorted(item_frequencies.items(), key = lambda x:x[1])

# Sorting frequencies and items in separate variables 

frequencies = list(reversed([i[1] for i in item_frequencies]))

items = list(reversed([i[0] for i in item_frequencies]))

# Barplot of top 10 

import matplotlib.pyplot as plt

plt.bar(height = frequencies[0:1], x = list(range(0, 11)), color = 'rgbkymc')

plt.xticks(list(range(0, 6), ), items[0:10])

plt.xlabel("items")

plt.ylabel("Count")

plt.show()

from mlxtend.frequent_patterns import apriori, association_rules

frequent_itemsets = apriori(Phones1, min_support = 0.0075, max_len = 3, use_colnames = True)

# Most Frequent item sets based on support 

frequent_itemsets.sort_values('support', ascending = False, inplace = True)

# Barplot of top 10 

import matplotlib.pyplot as plt

plt.bar(x = list(range(0, 11)), height = frequent_itemsets.support[0:11], color ='rgmyk')

plt.xticks(list(range(0, 11)), frequent_itemsets.itemsets[0:11], rotation=30)

plt.xlabel('item-sets')

plt.ylabel('support')

plt.show()

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)

rules.head(20)

rules.sort_values('lift', ascending = False).head(10)

# creating a csv file 

rules.to_csv("Phonesassociation.csv", encoding = "utf-8")

import os

os.getcwd()



# The highest lift ratio we got is 1.83 so that is the best rules.