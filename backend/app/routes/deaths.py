from fastapi import APIRouter, HTTPException
import json
import os

# ✅ Build absolute path (works on local + EC2)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR,  "data", "road_deaths.geojson")

# Load GeoJSON once
try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        geojson_data = json.load(f)
except FileNotFoundError:
    raise RuntimeError(f"GeoJSON file not found at {DATA_FILE}")

router = APIRouter()

@router.get("/road-deaths/{year}")
def get_deaths_by_year(year: int):
    """
    Return all road deaths data for a given year as a FeatureCollection.
    """
    features = [f for f in geojson_data["features"] if f["properties"].get("Year") == year]

    if not features:
        raise HTTPException(status_code=404, detail=f"No data found for year {year}")

    return {
        "type": "FeatureCollection",
        "features": features
    }

@router.get("/road-deaths/{year}/{country_code}")
def get_deaths_by_country(year: int, country_code: str):
    """
    Return road deaths for a specific country in a given year.
    Accepts ISO_A2, ISO_A3, or CountryName.
    """
    country_code = country_code.upper()

    feature = next(
        (
            f for f in geojson_data["features"]
            if f["properties"].get("Year") == year and (
                f["properties"].get("ISO_A2", "").upper() == country_code or
                f["properties"].get("ISO_A3", "").upper() == country_code or
                f["properties"].get("CountryName", "").upper() == country_code
            )
        ),
        None
    )

    if not feature:
        raise HTTPException(status_code=404, detail=f"No data found for {country_code} in {year}")

    return {
        "type": "FeatureCollection",
        "features": [feature]
    }
