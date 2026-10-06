function About() {
  return (
    <div className="about-page">

      <h1>About ReviewSense</h1>

      <p className="about-intro">
        ReviewSense is a product review sentiment analysis
        system designed to understand customer opinions
        from product reviews.
      </p>

      <div className="about-card">

        <h2>What does ReviewSense do?</h2>

        <p>
          ReviewSense analyzes customer reviews and classifies
          them into three sentiment categories:
        </p>

        <div className="about-sentiments">

          <div className="about-sentiment positive">
            <span>😊</span>
            <h3>Positive</h3>
            <p>Reviews expressing satisfaction or positive opinions.</p>
          </div>

          <div className="about-sentiment neutral">
            <span>😐</span>
            <h3>Neutral</h3>
            <p>Reviews containing neutral or balanced opinions.</p>
          </div>

          <div className="about-sentiment negative">
            <span>😞</span>
            <h3>Negative</h3>
            <p>Reviews expressing dissatisfaction or negative opinions.</p>
          </div>

        </div>

      </div>

      <div className="about-card">

        <h2>Technology Used</h2>

        <div className="technology-list">

          <span>React</span>
          <span>JavaScript</span>
          <span>HTML</span>
          <span>CSS</span>
          <span>Recharts</span>
          <span>Python</span>
          <span>Machine Learning</span>

        </div>

      </div>

      <div className="about-card">

        <h2>Project Goal</h2>

        <p>
          The goal of ReviewSense is to present customer review
          insights in a simple and visual way using sentiment
          analysis, charts, statistics, and customer reviews.
        </p>

      </div>

    </div>
  );
}

export default About;