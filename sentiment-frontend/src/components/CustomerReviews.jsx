function CustomerReviews({ reviews = [] }) {
  return (
    <section className="reviews-section">

      <h2>Customer Reviews</h2>

      <div className="reviews-list">

        {reviews.length > 0 ? (
          reviews.map((review) => (

            <div className="review-card" key={review.id}>

              <div className="review-header">

                <span
                  className={`sentiment-badge ${
                    review.sentiment.toLowerCase()
                  }`}
                >
                  {review.sentiment}
                </span>

              </div>

              <p className="review-text">
                "{review.text}"
              </p>

            </div>

          ))
        ) : (
          <p>No reviews available.</p>
        )}

      </div>

    </section>
  );
}

export default CustomerReviews;