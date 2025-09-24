import React, { useState } from "react";
import RoadDeathsMap from "./RoadDeathsMap";

function App() {
  const [year, setYear] = useState(2015);

  return (
    <div style={{ textAlign: "center" }}>
      <h1>Road Safety Atlas</h1>
      <input
        type="range"
        min="2014"
        max="2024"
        value={year}
        onChange={(e) => setYear(parseInt(e.target.value))}
      />
      <p>Year: {year}</p>
      <RoadDeathsMap year={year} />
    </div>
  );
}

export default App;
