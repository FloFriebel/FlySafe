import os
from darts.models import TFTModel


def load_model(): # add target_scaler to load model
    print(os.path.dirname(__file__))
    model_loaded = TFTModel.load('tft_v1_1yeardata_3h.pt', map_location='cpu') #path
    model_loaded.to_cpu()
    return model_loaded

def predict(model_loaded, y_val_series, past_cov_val_series, future_cov_val_series, target_scaler):

    preds = model_loaded.predict(n=3,
                   series=y_val_series,
                   past_covariates = past_cov_val_series,
                   future_covariates = future_cov_val_series)

    original_preds = target_scaler.inverse_transform(preds.pd_dataframe())
    #print("Original predictions (pressure values):", original_preds.flatten())

    #use target_scaler to inversetranform


    #conversion from timeseries number to hPa
    return original_preds

# Example
if __name__=="__main__":
    data_pro = load_model("2024-02-10", "2024-03-15")
    print(data_pro)
