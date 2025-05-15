import pickle
import numpy as np
import pandas as pd

# Load model dan scaler
with open("app/model/kmeans_model.pkl", "rb") as f:
    kmeans_model = pickle.load(f)

with open("app/model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Fitur yang digunakan
num_features = ['Panjang_Ruas(Km)', 'Aspal', 'Beton', 'Kerikil', 'Tanah', 'Rasio_Baik', 'Rasio_Rusak']

def preprocess_input(data: dict):
    df = pd.DataFrame([data])
    X = df[num_features]
    X_scaled = scaler.transform(X)
    return X_scaled

def predict_cluster(data: dict):
    X_processed = preprocess_input(data)
    cluster = kmeans_model.predict(X_processed)
    return int(cluster[0])
