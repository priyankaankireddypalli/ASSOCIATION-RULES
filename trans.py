# 5

import pandas as pd

from  mlxtend.frequent_patterns import apriori,association_rules

transactionretail = []

with open('C:\\Users\\WIN10\\Desktop\\LEARNING\\transactions_retail1.csv') as f: transactionretail = f.read()

# Splitting the data into separate transactions using '\n' operator

transactionretail = transactionretail.split('\n')

transactionlist = []

for i in transactionretail:

    transactionlist.append(i.split(','))

alltransactions = [i for item in transactionlist for i in item]

from collections import Counter

itemfrequencies = Counter(alltransactions)

# After sorting

itemfrequencies = sorted(itemfrequencies.items(),key = lambda x:x[1])

# Sorting frequencies and items in separate variables

frequencies = list(reversed([i[1] for i in itemfrequencies]))

items = list(reversed([i[0] for i in itemfrequencies]))

# Barplot of top 10

import matplotlib.pyplot as plt

plt.bar(height = frequencies[3:11], x = list(range(3, 11)), color = 'rgbkymc')

plt.xticks(list(range(3, 11), ), items[3:11])

plt.xlabel("items")

plt.ylabel("Count")

plt.show()

# Creating dataframe for transactions data

mytransactionseries = pd.DataFrame(pd.Series(transactionlist))

mytransactionseries = mytransactionseries.iloc[:9835,:] # Removing the last empty transaction

mytransactionseries.columns = ['transactions']

# Creating dummy variables for each item in each transaction, using column names as item names

x = mytransactionseries['transactions'].str.join(sep = '*').str.get_dummies(sep = '*')

frequentitemsets = apriori(x,min_support=0.0075,use_colnames=True,max_len=4)

# Most frequent itemsets based on support

frequentitemsets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(3, 11)), height = frequentitemsets.support[3:11], color ='rgmyk')

plt.xticks(list(range(3, 11)), frequentitemsets.itemsets[3:11], rotation=20)

plt.xlabel('item-sets')

plt.ylabel('support')

plt.show()

rules = association_rules(frequentitemsets, metric = "lift", min_threshold = 1)

rules.head(20)

rules.sort_values('lift', ascending = False).head(10)

# creating a csv file 

rules.to_csv("transaction.csv", encoding = "utf-8")

import os

os.getcwd()



# The highest lift ratio we got is 127 so that is the best rules.

