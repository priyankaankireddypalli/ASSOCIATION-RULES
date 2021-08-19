# 4
library(readr)
library(arules)
# Imporing the dataset
phonedata <- read.csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\myphonedata.csv')
phonedataap <- phonedata[,-c(1,2,3)]
# Applying Apriori algorithm
arules <- apriori(phonedataap,parameter = list(support = 0.002,confidence = 0.75,minlen = 2))
arules
# Viewing rules based on lift value
inspect(head(sort(arules,by = 'lift')))
# Overall quality
head(quality(arules))
windows()
# Different ways of visualizing rules
library(arulesViz)
plot(arules)
plot(arules,method = 'grouped')
plot(arules[1:10],method = 'graph')
# Exporting the output
write(arules,file = 'arulesphonedata.csv')
getwd()

# Since lift ratio is equal to 1, we cannot come to any conclusion
