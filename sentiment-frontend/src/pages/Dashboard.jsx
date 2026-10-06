import ProductInfo from "../components/ProductInfo";
import SentimentCards from "../components/SentimentCards";
import SentimentChart from "../components/SentimentChart";
import SentimentTrend from "../components/SentimentTrend";
import CustomerReviews from "../components/CustomerReviews";
import ReviewStatistics from "../components/ReviewStatistics";


function Dashboard({ result }) {

  const product = result?.product;
  const sentiment = result?.sentiment;
  const reviews = result?.reviews || [];


  return (
    <div className="dashboard-page">

      <h1>Sentiment Dashboard</h1>

      <p className="dashboard-subtitle">
        View detailed product review sentiment analysis.
      </p>


      <ProductInfo
        productName={product?.name}
        source={product?.source}
        rating={product?.rating}
        totalReviews={product?.total_reviews}
      />


      <SentimentCards
        sentiment={sentiment}
        totalReviews={product?.total_reviews}
      />


      <SentimentChart
        sentiment={sentiment}
        totalReviews={product?.total_reviews}
      />


      <SentimentTrend
        sentiment={sentiment}
        totalReviews={product?.total_reviews}
      />


      <CustomerReviews
        reviews={reviews}
      />


      <ReviewStatistics
        sentiment={sentiment}
        totalReviews={product?.total_reviews}
      />

    </div>
  );
}


export default Dashboard;