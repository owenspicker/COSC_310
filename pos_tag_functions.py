import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag



#this first method checks if a currency is present in the userInput

def checkForCurrency(userInput):
    userInput = nltk.word_tokenize(userInput)   #sentences are split by words
    userInput = nltk.pos_tag(userInput)         #words are assigned pos tag
    truth = False
    for i in range(len(userInput)):
        a = userInput[i]
        if (a[1] == '$'):                       #if a currency is found, return true
            truth = True
    return truth

#this method checks if a year is present in the userInput

def checkForNum(userInput):
    userInput = nltk.word_tokenize(userInput)   #sentences split by words
    userInput = nltk.pos_tag(userInput)         #words assigned a pos tag
    truth = False
    for i in range(len(userInput)):
        a = userInput[i]                        #if year is found starting with 1 or 2, return true
        if (a[1] == 'CD' and len(a[0]) == 4 and (a[0][0] == '2' or a[0][0] == '1')):
            truth = True
    return truth
