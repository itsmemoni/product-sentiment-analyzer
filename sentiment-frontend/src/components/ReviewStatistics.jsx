function ReviewStatistics({ sentiment, totalReviews }) {
  const positive = sentiment?.positive || 0;
  const negative = sentiment?.negative || 0;
  const neutral = sentiment?.neutral || 0;

  const total =
    totalReviews ?? positive + negative + neutral;

  return (
    <section className="statistics-section">

      <h2>Review Statistics</h2>

      <div className="statistics-cards">

        <div className="stat-card">
          <div className="stat-icon">📝</div>

          <h3>Total Reviews</h3>

          <h2>{total}</h2>
        </div>

        <div className="stat-card">
          <div className="stat-icon">😊</div>

          <h3>Positive Reviews</h3>

          <h2>{positive}</h2>
        </div>

        <div className="stat-card">
          <div className="stat-icon">😞</div>

          <h3>Negative Reviews</h3>

          <h2>{negative}</h2>
        </div>

        <div className="stat-card">
          <div className="stat-icon">😐</div>

          <h3>Neutral Reviews</h3>

          <h2>{neutral}</h2>
        </div>

      </div>

    </section>
  );
}

export default ReviewStatistics;