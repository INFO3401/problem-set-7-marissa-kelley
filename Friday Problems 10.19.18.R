#Friday's Work for Problem Set 7
#Marissa Kelley 

#PROBLEM 6
#Store the contents of the csv data into a variable in R
titanic = read.csv(file=titanic.csv,head=TRUE,sep=",")
#Print the variable
titanic

#print a summary table of that variable
summary(titanic)
