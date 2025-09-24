from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RoadDeaths(Base):
    __tablename__ = "road_deaths"

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, index=True)  # ISO_A3
    year = Column(Integer, index=True)
    deaths = Column(Integer)
