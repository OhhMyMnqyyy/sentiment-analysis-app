from textblob import TextBlob

def analyze_sentiment(review):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😡"
    else:
        return "Neutral 😐"

