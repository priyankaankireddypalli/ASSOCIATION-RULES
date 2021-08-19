# 3
library(readr)
library(arules)
# Importing the dataset
movies <- read.csv('C:\\Users\\WIN10\\Desktop\\LEARNING\\my_movies.csv')
moviesap <- movies[,c(-1,-2,-3,-4,-5)]
# Applying Apriori algorithm
arules <- apriori(moviesap,parameter = list(support = 0.002,confidence = 0.75,minlen = 2))
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
# Exporting the file
write(arules,file = 'arulesmovies.csv')
getwd()

# Since the lift ratio is equal to 1, we cannot come to any conclusion