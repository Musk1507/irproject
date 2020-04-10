import re #Package for splitting 
from spellchecker import SpellChecker

def gradingFunction(file_name,file_name1):
    file_name = file_name[:-1]
    file1 = open(file_name1,"r")
    filedata1 = file1.readlines()
    spell = SpellChecker()
    marks = 75
    count = 0
    flg = 0
    misspelled = []
    vocab = []
    articles = re.split(', |"|" |-|! |!|\? |\?|\. |\.',file_name)

    for i in range(0,len(filedata1)):
        filedata1[i] = (filedata1[i].rstrip('\n')) #Making clean words from our dataset

    for sentences in articles:
        for words in sentences.split(" "):
            count += 1 
            wrong_word = spell.unknown([words]) #Catches spelling mistakes
            for i in range(0,len(filedata1)):
                if words.lower() == filedata1[i].lower():
                    marks += 4 #Adding "+4" for good vocabulary
                    vocab.append(words) #Making list of good vocabulary
            if wrong_word:
                marks = marks - 2 #For spelling mistakes "-2"
                misspelled.append(wrong_word) #Making a list of spelling mistakes 


    if ((count > 500)or(count < 50)):
        marks -= 20 #For more/less the max/min number of lines "-20"
        flg = 1
        
    if marks>100:
        marks = 100
    if marks<40:
        marks = 40

    if (marks >= 90): 
        grade = "S" 
    elif (marks >= 80): 
        grade = "A" 
    elif (marks >= 70): 
        grade = "B" 
    elif (marks >= 60): 
        grade = "C" 
    elif (marks >= 50): 
        grade = "D" 
    else: 
        grade = "E"

    return marks,misspelled,vocab,flg,grade