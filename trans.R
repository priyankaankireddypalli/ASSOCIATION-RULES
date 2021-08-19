# 5
library(readr)
library(arules)
# Importing the dataset
trans <- read.csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\transactions_retail1.csv')
# Applying Apriori algorithm
arules <- apriori(trans,parameter = list(support = 0.002,confidence = 0.75, minlen = 2))
arules
# Viewing rules based on lift value
inspect(head(sort(arules,by = 'lift')))
# Overall quality
head(quality(arules))
# Different ways of visualizing rules
library(arulesViz)
windows()
plot(arules)
plot(arules,method = 'grouped')
plot(arules,method = 'graph')
# Exporting the output
write(arules,file = 'arulestrans.csv')
getwd()

# Here the highest lift ratio is 493.39, therefore that is the best rule