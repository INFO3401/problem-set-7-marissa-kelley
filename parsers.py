import string
import csv
from os import listdir #os is a library that allows you to access all the things from the command line into python? 

################################################################################
# PART #1
# I worked with Jacob Paul, Hannah Weber, Taylor Lawrence, Amy Zhai, Steven Rothaus
################################################################################ 
 # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
#import string

def countWordsUnstructured(filename):
    #Initalize a word count dictionary 
    wordCounts = {} 
    
    #Open the file and read it #could also do datafile = open(filename).read()
    file = open(filename)
    
    #Make a for loop to split out the data into words and count it 
    for word in file.read().split(): 
        for mark in string.punctuation:
            word = word.replace(mark, "")
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1
    #Return the word count dictionary 
    return wordCounts
         
    
# In class October 1st work- aka another way of doing it 
    #for word in data: 
        #for mark in string.punctuation:
            #word = word.replace(mark, "")
        #if word in wordCounts:
            #wordCounts[word] = wordCounts[word] + 1
        #else: 
            #wordCounts[word] = 1
    
    #return the word count dictionary
    #return wordCounts 
    
################################################################################
# PART 2
#I worked with Hannah Weber, Taylor Lawrence
################################################################################
 # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting: 
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data
    
# Import the csv (at the top) 
def generateSimpleCSV(targetfile, wordCounts):
    
    #open the csv 
    with open (targetfile, "w") as csv_file:
        
        #Print the headers and write to the csv using commas as a seperator 
        writer = csv.writer(csv_file)
        
        #Make the header 
        writer.writerow(['Word', 'Count'])
        
        #Iterate through the word counts and add to the csv
        for key,value in wordCounts.items():
            writer.writerow([key,value])
    
    #Close the file
    csv_file.close()
    
    #Return pointer to the file 
    return csv_file
    
# Test your part 2 code below
generateSimpleCSV('PleaseWork', countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt'))

################################################################################
# PART 3
# I worked with Hannah and Taylor 
################################################################################
 # This function should create a dictionary of word count dictionaries (key value pairs,
    #key is the reference- so the word is the key, value is the actual count) 

    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    #          text file in the directory
    
    # Key: the file 
    # Value: the counts 
    
def countWordsMany(directory):
    #create a blank dictionary to hold all of the data 
    wordCountDict = {}
    
    #open directory and pull and create a list of all the file names in the directory
    dir_files = listdir(directory)
    
    # Populate the dictionary using a for loop through the list of files
        #For each file, call countWordsUnstructured to get the word counts for that file
        #You already have the list of filenames, so to get the filename, you need to use a for loop structure
        #Place the wordcount into the dictionary name and the filepath 
    for file in dir_files:
        wordCountDict[file] = countWordsUnstructured(directory+"/" + file)  
       
        # Return/Output the wordCountDict 
        return wordCountDict
        
# Test your part 3 code below
manyWordsDict = countWordsMany('./state-of-the-union-corpus-1989-2017')
print(manyWordsDict)
   
#One of the inputs is the directory name and the filepath

################################################################################
# PART 4
# I worked in class and with Hannah 
################################################################################

    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    
#create a placeholder dictionary
# Import the csv (at the top) 

def generateDirectoryCSV(wordCounts, targetfile): 
    #open the csv 
    with open (targetfile, 'w') as csv_file:
        
        #Print the headers and write to the csv using commas as a seperator 
        writer = csv.writer(csv_file)
        
        #Write the header rows
        writer.writerow(['Filename', 'Word', 'Count'])
        
        #Iterate through the word counts and add to the csv
        for key,value in wordCounts.items():
            writer.writerow([key,value])
    
    #Close the file
    csv_file.close()
    
    #Return pointer to the file 
    return csv_file

    
    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting: 
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data
    
# Test your part 4 code below
generateDirectoryCSV(countWordsMany('state-of-the-union-corpus-1989-2017'), 'part_4_CSV')

################################################################################
# PART 5
# I worked with Hannah Weber, Taylor Lawrence, Amy Zhai and Steven Rothaus
################################################################################
# This function should create a JSON containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data

import json

def generateJSONFile(wordCounts, targetfile): 
    
    #open a file as a json_file
    with open(targetfile, 'w') as JSONFile:
        
        #create the json
        JSONFile = open(targetfile, "w")
        #transforms the word count directory to a JSON
        JSONFile.write(str(wordCounts).replace("\'","\""))
        
        
    #close file
    JSONFile.close()
    
    #return the json file
    return JSONFile

    
# Test your part 5 code below
generateJSONFile(manyWordsDict, "part_5_file")

################################################################################
# PART 6
# I worked with Jacob, Hannah and Taylor 
################################################################################
# This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word

def searchCSV(csvfile, word): 
    
    #set the variables to use
    largest_count_file = ""
    largest_count = 0
    
    #open the csv file
    with open(csvfile) as csv_file:
        file = csv.reader(csv_file)
    
    #Make a for loop for finding the filename with the largest count of a specified word  
        for line in file:
            if line[1] == word and int(line[2])> int(largest_count): #finds which line has the highest count 
                largest_count = line[2]
                largest_count_file = line[0]
            
    #return the file with the largest wordcount
    return largest_count_file
    
    #Close the file
    csv_file.close()

    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word  
import json

def searchJSON(JSONFile, word): 
    
    #set the variables to use later
    largest_count_file = ""
    largest_count = 0
    
    #open the json file
    with open(JSONFile) as json_file:
        data = json.load(json_file) 
            
    #Make for loop for finding the file that has the highest count for that word
        for file in data:
            if data[file][word]> largest_count:
                largest_count = data[file][word]
                largest_count_file = file
    
    #Return the highest values filename
    return largest_count_file

    #close the file
    json_file.close()
    
    
# Test your part 6 code to find which file has the highest count of a given word
print(searchCSV("part_4_CSV","for"))
print(searchJSON("part_5_file","for"))

# +1 bonus point for figuring out how many datapoints you had to process to 
# compute this value


################################################################################
# PART 7 - FRIDAY SECTION
# I worked with Jacob, Hannah and Taylor 
################################################################################
#Database Schema: 

#From the slides
#Using SQLite in Python
import sqlite3

#Set up a connection to the database
conn = sqlite3.connect('presidents_speech.db')
c = conn.cursor()

# Ask the connection to execute a SQL statement
c.execute('''CREATE TABLE wordCounts (filename, word, counts)''')
c.execute('''CREATE TABLE presidentInformation(index,number, start, end, president_name, prior occupation, party, VP )''')

#The tables can be joined on either the presidents name or year of their presidency
#Table 1 (wordCounts)
    #Text filename
    #Text word
    #Integer counts
    #Integers Counts
#Table 2 (PresidentInfo- the csv file)
    #Integer index
    #Integer number
    #Text start
    #Text end
    #Text President_name
    #Text prior occumpation
    #Text Party 
    #Text VP

# Save (commit) the changes
conn.commit()
        
# Close the connection
conn.close()