from pydantic import BaseModel

class RoadDeath(BaseModel):
    country_code: str
    year: int
    deaths: int

    class Config:
        orm_mode = True
