import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project_notebooks.data_preprocessing.load_data import load_data
from project_notebooks.data_preprocessing.data_preprocessing import data_preprocessing
from project_notebooks.data_preprocessing.predict import load_model #loading function from predict.py file

app = FastAPI()


# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/predict")
def predict(
    n=output_chunk_length,
    series=y_val_series,
    past_covariates = past_cov_val_series,
    future_covariates = future_cov_val_series)
    ):

    model = load_model()
    assert model is not None
