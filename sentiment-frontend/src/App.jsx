import "./App.css";
import Navbar from "./components/Navbar";
import SearchBar from "./components/SearchBar";
import ProductInfo from "./components/ProductInfo";
import SentimentCards from "./components/SentimentCards";
import SentimentChart from "./components/SentimentChart";
import SentimentTrend from "./components/SentimentTrend";
import CustomerReviews from "./components/CustomerReviews";
import ReviewStatistics from "./components/ReviewStatistics";

import Dashboard from "./pages/Dashboard";
import About from "./pages/About";

import { useState } from "react";

import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";


function Home({ result, setResult }) {

  const product = result?.product;
  const sentiment = result?.sentiment;
  const reviews = result?.reviews || [];

  return (
    <div className="app">

      <h1>Product Sentiment Analyzer</h1>

      <p>
        Analyze customer reviews and understand product sentiment.
      </p>

      <SearchBar onResult={setResult} />


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


function App() {

  // Shared analysis result
  const [result, setResult] = useState(null);

  return (
    <BrowserRouter>

      <Navbar />

      <Routes>

        <Route
          path="/"
          element={
            <Home
              result={result}
              setResult={setResult}
            />
          }
        />

        <Route
          path="/dashboard"
          element={
            <Dashboard
              result={result}
            />
          }
        />

        <Route
          path="/about"
          element={<About />}
        />

      </Routes>

    </BrowserRouter>
  );
}


export default App;