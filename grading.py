import re #Package for splitting 
from spellchecker import SpellChecker


def grading(file_name):
    file = open(file_name, "r")
    filedata = file.readlines()
    spell = SpellChecker()
    marks = 7.5
    count = 0
    misspelled = []
    articles = re.split(', |"|_|-|!|\. ',filedata[0])
    for sentences in articles:
        for words in sentences.split(" "):
            count += 1 #number of words
            wrong_word = spell.unknown([words])
            if wrong_word:
                if (marks>4):
                    marks = marks - 0.2 #For spelling mistakes "-0.2"
                misspelled.append(wrong_word) #Making a list of spelling mistakes
    if ((count > 200)or(count < 50)):
        if (marks>4):
            marks -= 2 #For more/less the max/min number of lines "-2"
            
    print("You have scored:",round(marks,1),"on 10")
    print("These are the spelling mistakes you have made:",misspelled)

grading("msft.txt")