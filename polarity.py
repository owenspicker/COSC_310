from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def checkPolarity(userInput):
    analyzer1 = SentimentIntensityAnalyzer()
    text = analyzer1.polarity_scores(userInput)
    truth = False
    if text['compound'] < -0.299:
        truth = True
    return truth
