#1 
# Installing arules package
install.packages("arules")
library(arules)
library(readr)
# Loading the dataset
books <- read.csv("C:\\Users\\WIN10\\Desktop\\LEARNING\\book.csv")
# Applying Apriori algoritm
arules <- apriori(books,parameter = list(support = 0.002, confidence = 0.75, minlen = 2))
arules
# Viewing rules based on lift value
inspect(head(sort(arules,by='lift')))
# Overall quality
head(quality(arules))
windows()  # Opens a window for graphical representation
# Installing arules visualization package
install.packages('arulesViz')
library('arulesViz')
# Different ways of visualizing rules
plot(arules)
plot(arules,method = 'grouped')

plot(arules[1:10],method = 'grouped')
# Exporting the file
write(arules,file = 'booksarules.csv',sep = ',')
getwd()

# By this we can conclude that,
# Since, the lift is equal to 1 we cannot make any conclusion