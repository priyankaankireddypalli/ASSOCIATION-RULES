# 2
import pandas as pd

from mlxtend.frequent_patterns import apriori, association_rules

groceries = []

with open("C:\\Users\\WIN10\\Desktop\\LEARNING\\groceries.csv") as f:groceries = f.read()

# splitting the data into separate transactions using separator as "\n"

groceries = groceries.split("\n")

grocerieslist = []

for i in groceries:

    grocerieslist.append(i.split(","))

allgrocerieslist = [i for item in grocerieslist for i in item]

from collections import Counter # ,OrderedDict

itemfrequencies = Counter(allgrocerieslist)

# after sorting

itemfrequencies = sorted(itemfrequencies.items(), key = lambda x:x[1])

# Storing frequencies and items in separate variables 

frequencies = list(reversed([i[1] for i in itemfrequencies]))

items = list(reversed([i[0] for i in itemfrequencies]))

# barplot of top 10 

import matplotlib.pyplot as plt

plt.bar(height = frequencies[0:11], x = list(range(0, 11)), color = 'rgbkymc')

plt.xticks(list(range(0, 11), ), items[0:11])

plt.xlabel("items")

plt.ylabel("Count")

plt.show()

# Creating Data Frame for the transactions data

groceriesseries = pd.DataFrame(pd.Series(grocerieslist))

groceriesseries = groceriesseries.iloc[:9835, :] # removing the last empty transaction

groceriesseries.columns = ["transactions"]

# creating a dummy columns for the each item in each transactions ... Using column names as item name

X = groceriesseries['transactions'].str.join(sep = '*').str.get_dummies(sep = '*')

frequentitemsets = apriori(X, min_support = 0.0075, max_len = 4, use_colnames = True)

# Most Frequent item sets based on support 

frequentitemsets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = frequentitemsets.support[0:11], color ='rgmyk')

plt.xticks(list(range(0, 11)), frequentitemsets.itemsets[0:11], rotation=20)

plt.xlabel('item-sets')

plt.ylabel('support')

plt.show()

rules = association_rules(frequentitemsets, metric = "lift", min_threshold = 1)

rules.head(20)

rules.sort_values('lift', ascending = False).head(10)

# creating a csv file 

rules.to_csv("groceriesassociation.csv", encoding = "utf-8")

import os

os.getcwd()



# The heighest lift ratio value is 4.15, so that is the best rule