from textblob import TextBlob

class SentimentAnalyzer:
    def analyze_sentiment(self, text):
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity

            if polarity > 0:
                return "positive"
            elif polarity < 0:
                return "negative"
            else:
                return "neutral"
        except Exception as e:
            return str(e)
