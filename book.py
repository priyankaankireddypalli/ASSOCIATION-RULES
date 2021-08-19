# 1
# Installing mlxtend package
pip install mlxtend

import pandas as pd

from mlxtend.frequent_patterns import apriori,association_rules

book = pd.read_csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\book.csv')

booklist = []

for i in book:

    booklist.append(i.split(','))

allbooklist = [i for item in booklist for i in item]

from collections import Counter

itemfreq = Counter(allbooklist)

# After sorting

itemfreq = sorted(itemfreq.items(),key = lambda x:x[1])

# Sorting frequencies and items in separate variables

frequencies = list(reversed([i[1] for i in itemfreq]))

items = list(reversed([i[0] for i in itemfreq]))

# Barplot of top 10

import matplotlib.pyplot as plt

plt.bar(height = frequencies[0:11],x = list(range(0,11)),color = 'rgbkymc')

plt.xticks(list(range(0,11),),items[0:11])

plt.xlabel('items')

plt.ylabel('count')

plt.show()

frequentitemset = apriori(book,min_support = 0.0075,max_len = 4,use_colnames = True)

# Most frequent items based on support

frequentitemset.sort_values('support',ascending = False,inplace = True)

# Barplot of top 10

plt.bar(x = list(range(0,11)),height = frequentitemset.support[0:11],color = 'rgmyk')

plt.xticks(list(range(0,11)), frequentitemset.itemsets[0:11],rotation = 30)

plt.xlabel('item-sets')

plt.ylabel('support')

plt.show()

rules = association_rules(frequentitemset, metric = "lift", min_threshold = 1)

rules.head(20)

rules.sort_values('lift', ascending = False).head(10)

# creating a csv file 

rules.to_csv("bookassociation.csv", encoding = "utf-8")

import os

os.getcwd()



# The highest lift ratio we got is 45 so that is the best rule