from pydantic import BaseModel, confloat


class Station(BaseModel):
    id: int
    lat: confloat(ge=-90, le=90)
    lon: confloat(ge=-180, le=180)
