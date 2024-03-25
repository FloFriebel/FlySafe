import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project_notebooks.data_preprocessing.data_preprocessing import data_preprocessing
from project_notebooks.data_preprocessing.predict import load_model, predict #loading function from predict.py file

app = FastAPI()


# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.state.model = load_model()
@app.get("/")
def root():
    return dict(greetings= "hallo")

@app.get("/predict")
def prediction(
    _start,
    _end):

    model = app.state.model
    assert model is not None

    y_val_series, past_cov_val_series, future_cov_val_series, target_scaler = data_preprocessing(_start, _end)
    preds = predict(model, y_val_series, past_cov_val_series, future_cov_val_series, target_scaler)
    result = {
        "Zurich" : list(preds[:,0]),
        "Lugano": list(preds[:,1]),
        "Innsbruck": list(preds[:,2]),
        "Bolzano" : list(preds[:,3])
    }
    print(result)
    return result
