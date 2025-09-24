import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, GeoJSON, useMap } from "react-leaflet";
import axios from "axios";
import L from "leaflet";

function RoadDeathsMap({ year }) {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/road-deaths/${year}`)
      .then((res) => setData(res.data))
      .catch((err) => console.error("Error fetching data:", err));
  }, [year]);

const getColor = (deaths) => {
  return deaths > 3000
    ? "#800000" // Dark Red
    : deaths > 1000
    ? "#FF0000" // Bright Red
    : deaths > 500
    ? "#FFA500" // Orange
    : deaths > 100
    ? "#FFFF00" // Yellow
    : deaths > 50
    ? "#008000" // Green
    : "#0000FF"; // Blue
};


  const style = (feature) => {
    return {
      fillColor: getColor(feature.properties.Deaths),
      weight: 1,
      opacity: 1,
      color: "white",
      dashArray: "3",
      fillOpacity: 0.7,
    };
  };

  const onEachFeature = (feature, layer) => {
    if (feature.properties) {
      layer.unbindPopup(); // clear any old popup

      // ✅ Always inject current slider year
      const popupContent = `
        <b>${feature.properties.CountryName}</b><br/>
        Year: ${year}<br/>
        Deaths: ${feature.properties.Deaths}
      `;
      layer.bindPopup(popupContent);
    }
  };

  // ✅ Legend component
  function Legend() {
    const map = useMap();

    useEffect(() => {
      const legend = L.control({ position: "bottomright" });

      legend.onAdd = function () {
        const div = L.DomUtil.create("div", "info legend");
        const grades = [0, 50, 100, 500, 1000, 3000];
        const labels = [];

        for (let i = 0; i < grades.length; i++) {
          labels.push(
            `<i style="background:${getColor(
              grades[i] + 1
            )}; width: 18px; height: 18px; float: left; margin-right: 8px;"></i>
             ${grades[i]}${grades[i + 1] ? "&ndash;" + grades[i + 1] : "+"}`
          );
        }

        div.innerHTML = labels.join("<br>");
        div.style.background = "white";
        div.style.padding = "8px";
        div.style.borderRadius = "6px";
        div.style.boxShadow = "0 0 8px rgba(190, 162, 162, 0.3)";
        return div;
      };

      legend.addTo(map);
      return () => {
        legend.remove();
      };
    }, [map]);

    return null;
  }

  return (
    <MapContainer
      key={year} // 👈 reset map each time year changes
      style={{ height: "600px", width: "100%" }}
      center={[50, 10]}
      zoom={4}
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/">OSM</a>'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {data && (
        <GeoJSON
          key={year} // 👈 reset GeoJSON each time year changes
          data={data}
          style={style}
          onEachFeature={onEachFeature}
        />
      )}
      <Legend /> {/* ✅ Add legend */}
    </MapContainer>
  );
}

export default RoadDeathsMap;
