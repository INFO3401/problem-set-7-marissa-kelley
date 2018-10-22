#Friday's Work for Problem Set 7
#Marissa Kelley 

######PROBLEM 6###########
#Store the contents of the csv data into a variable in R
titanic = read.csv(file="titanic.csv",head=TRUE,sep=",")
#Print the variable
print(titanic)

#Print a summary table of that variable or print a statistical summary
summary(titanic)

#######PROBLEM 7###########
#Print out the names of the columns in the csv
names(titanic)

#Print out the values for the first two columns
titanic$"PassengerId"
titanic$"Survived"

table(titanic$PassengerId,Survived)

#Create a table that outlines the distribution of genders
#prop.table(titanic.csv)

######PROBLEM 8###########
#Compute the proportion of men & women who survived
prop.table(gender_table)
#prop.table(table(Sex$male,survived$1))
gender_table = prop.table(table("Sex","Survived"))
print(gender_table)

#Probability of survival for men and women
#prop.table(table(Sex$female,survived$1))
#prop.table(table(Sex$male,survived$1))

######PROBLEM 9###########
#Create a new column with age to define a child
#Child (0-18) = 1, Adult(18+) = 0
titanic$"Child"<=18
titanic$"Child"[titanic$"Age"<18]<-1
aggregate(titanic, by = list(R$"Sex", R$"Survived"), FUN = "mean")
aggregate(titanic, by = list(R$"Gender", R$"Survived"), FUN = "mean")

#Find the average number of survivors for men & women

#Find the average number of survivors for children and adults
