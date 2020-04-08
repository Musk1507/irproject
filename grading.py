import re #Package for splitting 
from spellchecker import SpellChecker


def grading(file_name,file_name1):
    file = open(file_name, "r")
    file1 = open(file_name1,"r")
    filedata = file.readlines()
    filedata1 = file1.readlines()
    spell = SpellChecker()
    marks = 7.5
    mistake_count = 0
    misspelled = []
    articles = re.split(', |"|_|-|!|\. ',filedata[0])

    for i in range(0,len(filedata1)):
        filedata1[i] = (filedata1[i].rstrip('\n')).lower() #Making clean words from our dataset

    for sentences in articles:
        for words in sentences.split(" "):
            mistake_count += 1 
            wrong_word = spell.unknown([words]) #Catches spelling mistakes
            for i in range(0,len(filedata1)):
                if words.lower() == filedata1[i]:
                    marks += 0.4 #Adding "+0.4" for good vocabulary
            if wrong_word:
                marks = marks - 0.4 #For spelling mistakes "-0.4"
                misspelled.append(wrong_word) #Making a list of spelling mistakes 


    if ((mistake_count > 200)or(mistake_count < 50)):
        marks -= 2 #For more/less the max/min number of lines "-2"
        
    if marks>10:
        marks = 10
    if marks<4:
        marks = 4
    print("You have scored:",round(marks,1),"on 10")
    print("These are the spelling mistakes you have made:",misspelled)
    
grading("msft.txt","dataset.txt")