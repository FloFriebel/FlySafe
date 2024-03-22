from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from darts.models import TFTModel
from project_notebooks.data_preprocessing.load_data import load_data
from project_notebooks.data_preprocessing.data_preprocessing import data_preprocessing

def load_model(_start, _end): # add target_scaler to load model
    model_loaded = TFTModel.load('jawP_projectV2/project_notebooks/data_preprocessing/tft_v1_1monthdata_3h') #path from : /home/luthian/code/FloFriebel/jawP_projectV2/project_notebooks/data_preprocessing/tft_v1_1monthdata_3h

    y_val_series = data_preprocessing(_start, _end)
    past_cov_val_series = data_preprocessing(_start, _end)
    future_cov_val_series = data_preprocessing(_start, _end)

    preds = model_loaded.predict(n=3,
                   series=y_val_series,
                   past_covariates = past_cov_val_series,
                   future_covariates = future_cov_val_series)

    """ original_preds = target_scaler.inverse_transform(preds.reshape(-1, 1))
    print("Original predictions (pressure values):", original_preds.flatten())

     use target_scaler to inversetranform


    """

    #conversion from timeseries number to hPa
    return preds

# Example
if __name__=="__main__":
    data_pro = data_preprocessing("2024-02-10", "2024-03-15")
    print(data_pro)
