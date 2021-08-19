# Load the Groceries dataset
library(readr)
input <- read_csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\groceries.csv')
install.packages("arules")
library("arules") # Used for building association rules i.e. apriori algorithm
# Building rules using apriori algorithm
arules <- apriori(input, parameter = list(support = 0.002, confidence = 0.75, minlen = 2))
arules
# Viewing rules based on lift value
inspect(head(sort(arules, by = "lift"))) # to view we use inspect 
# Overal quality 
head(quality(arules))
library("arulesViz") # for visualizing rules
# Different Ways of Visualizing Rules
plot(arules)
windows()
plot(arules, method = "grouped")
plot(arules[1:5], method = "graph") # for good visualization try plotting only few rules
# Exporting as csv file
write(arules, file = "groceriesarules.csv", sep = ",")
getwd()

# Here the highest lift ratio is 118.05, therefore that is the best rule