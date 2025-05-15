from fastapi import FastAPI
from app.schemas import RoadInput, ClusterOutput
from app.utils import predict_cluster

app = FastAPI(title="Road Clustering API")

@app.get("/")
def root():
    return {"message": "Welcome to Road Clustering API"}

@app.post("/predict", response_model=ClusterOutput)
def predict(input_data: RoadInput):
    input_dict = {
        'Panjang_Ruas(Km)': input_data.Panjang_Ruas_Km,
        'Aspal': input_data.Aspal,
        'Beton': input_data.Beton,
        'Kerikil': input_data.Kerikil,
        'Tanah': input_data.Tanah,
        'Rasio_Baik': input_data.Rasio_Baik,
        'Rasio_Rusak': input_data.Rasio_Rusak
    }
    result = predict_cluster(input_dict)
    return {"cluster": result}
