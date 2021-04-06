from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#this method will check the overall sentiment of the userInput

def checkPolarity(userInput):
    analyzer1 = SentimentIntensityAnalyzer()
    text = analyzer1.polarity_scores(userInput)
    truth = False
    if text['compound'] < -0.299:           #if sentence is found to be generally mean, return true
        truth = True
    return truth
