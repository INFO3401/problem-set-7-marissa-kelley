#Friday's Work for Problem Set 7
#Marissa Kelley 

#PROBLEM 6
#Store the contents of the csv data into a variable in R
titanic = read.csv(file=titanic.csv,head=TRUE,sep=",")
#Print the variable
titanic

#Print a summary table of that variable
summary(titanic)

#Referencing different values in each column
titanic$name 