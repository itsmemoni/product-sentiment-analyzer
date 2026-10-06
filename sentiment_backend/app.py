from flask import Flask, request, jsonify
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from scraper import get_product_data

app = Flask(__name__)
CORS(app)

analyzer = SentimentIntensityAnalyzer()


@app.get("/")
def home():
    return jsonify({
        "message": "Product Sentiment Analyzer API is running"
    })


@app.post("/api/analyze")
def analyze():
    data = request.get_json(silent=True) or {}
    product_url = str(data.get("url", "")).strip()

    if not product_url:
        return jsonify({"error": "Product URL is required"}), 400

    if not (product_url.startswith("http://") or product_url.startswith("https://")):
        return jsonify({"error": "Please enter a valid product URL"}), 400

    try:
        product = get_product_data(product_url)
        reviews = product.get("reviews", [])

        results = []
        positive = neutral = negative = 0

        for review in reviews:
            score = analyzer.polarity_scores(review)
            compound = score["compound"]

            if compound >= 0.05:
                sentiment = "Positive"
                positive += 1
            elif compound <= -0.05:
                sentiment = "Negative"
                negative += 1
            else:
                sentiment = "Neutral"
                neutral += 1

            results.append({
                "id": len(results) + 1,
                "text": review,
                "sentiment": sentiment,
                "compound": compound
            })

        total = positive + neutral + negative

        if positive > negative:
            overall = "Positive"
        elif negative > positive:
            overall = "Negative"
        else:
            overall = "Neutral"

        return jsonify({
            "product": {
                "name": product.get("product_name", "Unknown Product"),
                "source": product.get("source", "Unknown"),
                "rating": product.get("rating"),
                "total_reviews": total
            },
            "sentiment": {
                "positive": positive,
                "negative": negative,
                "neutral": neutral
            },
            "overall_sentiment": overall,
            "reviews": results
        })

    except Exception as exc:
        return jsonify({
            "error": str(exc)
        }), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
