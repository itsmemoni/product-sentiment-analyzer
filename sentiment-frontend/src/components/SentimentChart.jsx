import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer
} from "recharts";

const COLORS = [
  "#22c55e",
  "#ef4444",
  "#eab308"
];

function SentimentChart({ sentiment, totalReviews }) {

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
      name: "Positive",
      value: positivePercent
    },
    {
      name: "Negative",
      value: negativePercent
    },
    {
      name: "Neutral",
      value: neutralPercent
    }
  ];

  return (
    <section className="chart-section">

      <h2>Sentiment Distribution</h2>

      <div className="chart-container">

        <ResponsiveContainer width="100%" height={350}>

          <PieChart>

            <Pie
              data={data}
              dataKey="value"
              nameKey="name"
              cx="50%"
              cy="50%"
              outerRadius={110}
              label={({ name, value }) =>
                `${name}: ${value}%`
              }
            >

              {data.map((entry, index) => (
                <Cell
                  key={`cell-${index}`}
                  fill={COLORS[index]}
                />
              ))}

            </Pie>

            <Tooltip />

            <Legend />

          </PieChart>

        </ResponsiveContainer>

      </div>

    </section>
  );
}

export default SentimentChart;