from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

reviews = [
    "This product is excellent. I really love it!",
    "The product is okay, nothing special.",
    "Very bad product. I am completely disappointed."
]

for review in reviews:
    score = analyzer.polarity_scores(review)

    if score["compound"] >= 0.05:
        sentiment = "Positive"
    elif score["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print("\nReview:", review)
    print("Score:", score["compound"])
    print("Sentiment:", sentiment)