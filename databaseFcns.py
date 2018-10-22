# I worked with Jack, Jacob, Hannah, and Taylor 

# Place any necessary imports here
import sqlite3
import parsers
import pandas as pd
import numpy as np
####################################################
# Part 0
####################################################

# Move your parsers.py file to your Problem Set 7
# directory. Once you've done so, you can use the 
# following code to have access to all of your parsing
# functions. You can access these functions using the 
# parsers.<function name> notation as in: 
# parsers.countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt')
import parsers.py

####################################################
# Part 1
####################################################
# Write a function that will populate your database
    # with the contents of the word counts and us_presidents.csv
    # to your database. 
    # Inputs: A string containing the filepath to your database,
    #         A word count dictionary containing wordcounts for 
    #         each file in a directory,
    #         A metadata file containing a dictionary of data
    #         extracted from a supplemental file
    # Outputs: None
    
def populateDatabase(databaseName, wordCounts, metaData):
    conn = sqlite3.connect(databaseName)
   
    for file in wordCounts:
        print(file)
        for word in file:
            print(word)
            c.execute('''INSERT INTO word_counts(filename,word,count) values(;file;word;count)''',{'file': file,'word', 'count: int(file(word))'})
        c.execute('''SELECT word FROM word_counts''')
    conn.commit()
    conn.close()
    return 0

# Test your code here
populateDatabase("presidents.db",wordCounts)

#I can't get this to run, since my data won't load into this. Hence, I also can't get parts 2 or 3 to run either. I looked at the lecture videos and based all of my code off of that. 
	
	
	for i in range(len(df)):
		data = df.iloc[i]
		c.execute('''INSERT INTO US_Presidents (Idx, Number, Start, End, President, Prior, Party, Vice) 
					Values (?, ?, ?, ?, ?, ?, ?, ?) ''', np.array(data, dtype=str))
					
		conn.commit()
	df_wordcounts = pd.read_csv('targetfile.csv')
	
	for i in range(len(df_wordcounts)):
	
		data = df_wordcounts.iloc[i]
		print (data)
		c.execute('''INSERT INTO Speeches (File_name, Word, Word_Count)
					VALUES (?, ?, ?) ''', np.array(data, dtype=str))
		
		conn.commit()
		
populateDatabase('Presidents.db', parsers.countWordsMany("./state-of-the-union-corpus-1989-2017"), "us_presidents.csv")

####################################################
# Part 2
####################################################

def searchDatabase(databaseName, word): 
    # Write a function that will query the database to find the 
    # president whose speech had the largest count of a specified word.
    # Inputs: A database file to search and a word to search for
    # Outputs: The name of the president whose speech contained 
    # the highest count of the target word
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute('''SELECT count, MAX(count) AS "M''')
    conn.commit()
    conn.close()
    return 0
    conn = sqlite3.connect('./Presidents.db')
	
	
def computeLengthByParty(databaseName): 
    # Write a function that will query the database to find the 
    # average length (number of words) of a speech by presidents
    # of the two major political parties.
    # Inputs: A database file to search and a word to search for
    # Outputs: The average speech length for presidents of each 
    #          of the two major political parties.
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute('''SELECT count, AVG(count) AS "Most''')
    presidents_parties = df_presidents.loc[df_presidents['Party'] == 'Democratic' ]
	presidents_parties = df_presidents.loc[df_presidents['Party'] == 'Republican' ]
    conn.commit()
    conn.close()
    return 0
