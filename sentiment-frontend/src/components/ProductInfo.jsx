function ProductInfo({
  productName,
  source,
  rating,
  totalReviews,
}) {
  return (
    <div className="product-info">

      <div className="product-details">
        <h2>{productName || "No product analyzed"}</h2>

        <p>
          Product from {source || "Unknown source"}
        </p>
      </div>

      <div className="product-rating">
        <span>⭐</span>

        <strong>
          {rating !== null && rating !== undefined
            ? rating
            : "N/A"}
        </strong>

        <p>Rating</p>
      </div>

      <div className="review-count">
        <strong>
          {totalReviews ?? 0}
        </strong>

        <p>Total Reviews</p>
      </div>

    </div>
  );
}

export default ProductInfo;