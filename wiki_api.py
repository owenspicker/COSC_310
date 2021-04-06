import wikipedia


#this method checks if the sentence starts with "Tell me about", which triggers wikipedia API

def checkLookup(userInput):
    flag = False
    userTest = userInput.lower()
    words = userTest.split()
    if words[0] == 'tell' and words[1] == "me" and words[2] == "about":
        flag = True
    return flag


#this method executes the wikipedia search

def lookup(userInput):
    userTest = userInput.lower()
    words = userTest.split()
    newStr = ""                          #newStr will be the string that is searched in wikipedia
    x = range(3, len(words))
    for i in x:
        newStr = newStr + words[i] + " "
    try:
        newStr = wikipedia.summary(newStr, sentences = 1)  #result is limited to the first sentence returned
    except:
        newStr = "Sorry, I could not find information on '" + newStr + "'. Try a different topic."  #if no page is found, return this error message
        
    return newStr  

