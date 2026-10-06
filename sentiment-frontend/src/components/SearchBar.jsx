import { useState } from "react";

function SearchBar({ onResult }) {

  const [productUrl, setProductUrl] = useState("");
  const [searchedUrl, setSearchedUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  const handleSearch = async () => {

    if (productUrl.trim() === "") {
      setError("Please enter a product URL");
      return;
    }


    setLoading(true);
    setError("");
    setSearchedUrl(productUrl);


    try {

      const response = await fetch(
        "http://127.0.0.1:5000/api/analyze",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            url: productUrl.trim(),
          }),
        }
      );


      const data = await response.json();


      if (!response.ok) {
        throw new Error(
          data.error || "Backend API request failed"
        );
      }


      // Send backend result to App.jsx
      onResult(data);


      console.log(
        "Backend Response:",
        data
      );

    } catch (error) {

      console.error(
        "API Error:",
        error
      );

      setError(
        error.message ||
        "Unable to connect to backend. Please try again."
      );

      onResult(null);

    } finally {

      setLoading(false);

    }
  };


  return (
    <div className="search-container">

      <div className="search-section">

        <input
          type="url"
          placeholder="Paste product URL..."
          value={productUrl}
          onChange={(e) =>
            setProductUrl(e.target.value)
          }
        />


        <button
          onClick={handleSearch}
          disabled={loading}
        >
          {loading
            ? "Analyzing..."
            : "🔍 Analyze"}
        </button>

      </div>


      {searchedUrl && (
        <div className="search-result">

          <h2>Product URL</h2>

          <p>
            {searchedUrl}
          </p>


          {loading && (
            <p>
              Analyzing product reviews...
            </p>
          )}


          {error && (
            <p style={{ color: "red" }}>
              {error}
            </p>
          )}

        </div>
      )}

    </div>
  );
}


export default SearchBar;