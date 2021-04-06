import wikipedia


def checkLookup(userInput):
    flag = False
    userTest = userInput.lower()
    words = userTest.split()
    if words[0] == 'tell' and words[1] == "me" and words[2] == "about":
        flag = True
    return flag

def lookup(userInput):
    userTest = userInput.lower()
    words = userTest.split()
    newStr = ""
    x = range(3, len(words))
    for i in x:
        newStr = newStr + words[i] + " "
    try:
        newStr = wikipedia.summary(newStr, sentences = 1)
    except:
        newStr = "Sorry, I could not find information on '" + newStr + "'. Try a different topic."
        
    return newStr  

