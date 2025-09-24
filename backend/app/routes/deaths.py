from fastapi import APIRouter, HTTPException
import json
import os

router = APIRouter()

# Load GeoJSON once at startup
geojson_path = os.path.join(os.path.dirname(__file__), "../data/road_deaths.geojson")
with open(geojson_path, "r", encoding="utf-8") as f:
    geojson_data = json.load(f)


@router.get("/road-deaths/{year}")
def get_deaths_by_year(year: int):
    """
    Return all road deaths data for a given year as a FeatureCollection
    (for use in choropleth maps).
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
    Return road deaths for a specific country (ISO_A2 or ISO_A3) in a given year.
    Example: /road-deaths/2015/DE
    """
    feature = next(
        (
            f for f in geojson_data["features"]
            if f["properties"].get("Year") == year and
               (
                   f["properties"].get("ISO_A2") == country_code.upper() or
                   f["properties"].get("ISO_A3") == country_code.upper() or
                   f["properties"].get("Country") == country_code.upper()
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

@router.get("/road-deaths/{year}")
def get_deaths_by_year(year: int):
    features = [
        f for f in geojson_data["features"]
        if f["properties"].get("Year") == year
    ]

    # Force Year field to match requested year
    for f in features:
        f["properties"]["Year"] = year  

    if not features:
        raise HTTPException(status_code=404, detail=f"No data found for year {year}")

    return {
        "type": "FeatureCollection",
        "features": features
    }



