#Friday's Work for Problem Set 7
#Marissa Kelley 
#I worked with Hannah and Taylor 

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

#Create a table that outlines the distribution of genders
prop.table(gender_table)
gender_table = prop.table(table(titanic$"Sex", titanic$"Survived"))

######PROBLEM 8###########
#Compute the proportion of men & women who survived
prop.table(gender_table)

#prop.table(table(Sex$male,survived$1))
gender_tables = prop.table(table(titanic$"Sex",titanic$"Survived"))
print(gender_tables)

#Probability of survival for men and women
#prop.table(table(Sex$female,survived$1))
#prop.table(table(Sex$male,survived$1))

######PROBLEM 9###########
#Create a new column with age to define a child
#Child (0-18) = 1, Adult(18+) = 0
titanic$"Child"<=0
titanic$"Child"[titanic$"Age"<18]<-1

#Find the average number of survivors for men and women
aggregate(titanic, by = list(titanic$"Sex", titanic$"Survived"), FUN = "mean")

#Find the average number of survivors for children and adults
aggregate(titanic, by = list(titanic$"Child", titanic$"Survived"), FUN = "mean")