import googletrans                          #importing packages

from googletrans import Translator

translator = Translator()                   #creating translate object


def checkLang(userInput):                   #method to translate user input to english
    result = translator.translate(userInput)
    if(result.src != 'en'):                 #checking of input is not english
        userInput = result.text             #setting return value to translated statement
    return userInput

