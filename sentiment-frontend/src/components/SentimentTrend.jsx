import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer
} from "recharts";

function SentimentTrend({ sentiment, totalReviews }) {
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

  const data = [
    {
      month: "Current",
      positive: positivePercent,
      negative: negativePercent,
      neutral: neutralPercent
    }
  ];

  return (
    <section className="trend-section">

      <h2>Sentiment Trend</h2>

      <div className="trend-container">

        <ResponsiveContainer width="100%" height={350}>

          <LineChart data={data}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="month" />

            <YAxis />

            <Tooltip />

            <Legend />

            <Line
              type="monotone"
              dataKey="positive"
              stroke="#22c55e"
              strokeWidth={3}
            />

            <Line
              type="monotone"
              dataKey="negative"
              stroke="#ef4444"
              strokeWidth={3}
            />

            <Line
              type="monotone"
              dataKey="neutral"
              stroke="#eab308"
              strokeWidth={3}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </section>
  );
}

export default SentimentTrend;