from pydantic import BaseModel

class RoadInput(BaseModel):
    Panjang_Ruas_Km: float
    Aspal: float
    Beton: float
    Kerikil: float
    Tanah: float
    Rasio_Baik: float
    Rasio_Rusak: float

class ClusterOutput(BaseModel):
    cluster: int
