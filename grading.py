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
                misspelled.append(wrong_word)
    if count > 200:
        marks -= 2 #For exceeding the maximum number of lines -2
    print("You have scored:",marks,"on 10")
    print("These are the spelling mistakes you have made:",misspelled)

grading("msft.txt")