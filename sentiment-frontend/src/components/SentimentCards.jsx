function SentimentCards({ sentiment, totalReviews }) {
  const positive = sentiment?.positive || 0;
  const negative = sentiment?.negative || 0;
  const neutral = sentiment?.neutral || 0;

  const total = totalReviews || positive + negative + neutral;

  const positivePercent =
    total > 0 ? Math.round((positive / total) * 100) : 0;

  const negativePercent =
    total > 0 ? Math.round((negative / total) * 100) : 0;

  const neutralPercent =
    total > 0 ? Math.round((neutral / total) * 100) : 0;

  return (
    <section className="sentiment-section">

      <h2>Sentiment Analysis</h2>

      <div className="sentiment-cards">

        <div className="sentiment-card positive-card">
          <div className="sentiment-icon">😊</div>

          <h3>Positive</h3>

          <h2>{positivePercent}%</h2>

          <p>{positive} Reviews</p>
        </div>

        <div className="sentiment-card negative-card">
          <div className="sentiment-icon">😞</div>

          <h3>Negative</h3>

          <h2>{negativePercent}%</h2>

          <p>{negative} Reviews</p>
        </div>

        <div className="sentiment-card neutral-card">
          <div className="sentiment-icon">😐</div>

          <h3>Neutral</h3>

          <h2>{neutralPercent}%</h2>

          <p>{neutral} Reviews</p>
        </div>

      </div>

    </section>
  );
}

export default SentimentCards;