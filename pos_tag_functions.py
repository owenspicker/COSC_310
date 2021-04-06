import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


def checkForCurrency(userInput):
    userInput = nltk.word_tokenize(userInput)
    userInput = nltk.pos_tag(userInput)
    truth = False
    for i in range(len(userInput)):
        a = userInput[i]
        if (a[1] == '$'):
            truth = True
    return truth

def checkForNum(userInput):
    userInput = nltk.word_tokenize(userInput)
    userInput = nltk.pos_tag(userInput)
    truth = False
    for i in range(len(userInput)):
        a = userInput[i]
        if (a[1] == 'CD' and len(a[0]) == 4 and (a[0][0] == '2' or a[0][0] == '1')):
            truth = True
    return truth
