import re #Package for splitting 
from spellchecker import SpellChecker

def gradingFunction(file_name,file_name1):
    file1 = open(file_name1,"r")
    filedata1 = file1.readlines()
    spell = SpellChecker()
    marks = 7.5
    mistake_count = 0
    flg = 0
    misspelled = []
    vocab = []
    articles = re.split(', |"|" |-|! |!|\? |\?|\. |\.',file_name)

    for i in range(0,len(filedata1)):
        filedata1[i] = (filedata1[i].rstrip('\n')) #Making clean words from our dataset

    for sentences in articles:
        for words in sentences.split(" "):
            mistake_count += 1 
            wrong_word = spell.unknown([words]) #Catches spelling mistakes
            for i in range(0,len(filedata1)):
                if words.lower() == filedata1[i].lower():
                    marks += 0.4 #Adding "+0.4" for good vocabulary
                    vocab.append(words) #Making list of good vocabulary
            if wrong_word:
                marks = marks - 0.2 #For spelling mistakes "-0.2"
                misspelled.append(wrong_word) #Making a list of spelling mistakes 


    if ((mistake_count > 500)or(mistake_count < 50)):
        marks -= 2 #For more/less the max/min number of lines "-2"
        flg = 1
        
    if marks>10:
        marks = 10
    if marks<4:
        marks = 4
    return marks,misspelled,vocab,flg