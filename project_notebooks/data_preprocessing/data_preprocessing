from darts.dataprocessing.transformers.scaler import Scaler
from sklearn.preprocessing import MinMaxScaler
from darts import TimeSeries
from darts.models.forecasting.tft_model import TFTModel
from darts.metrics import mse
from darts.metrics import smape, mae
from torchmetrics.regression import MeanAbsoluteError
import pandas as pd
from project_notebooks.data_preprocessing.data_preprocessing import load_data

def data_preprocessing(_number):
    # data_combined.loc[('Zurich')]
    correct = pd.DataFrame()
    if load_data(_city) == "Zurich":
        city_query = [0, 1]
    elif load_data(_city) == "Innsbruck":
        city_query = [2, 3]
    #correct.index = data_combined.loc[('Zurich')].index
    if load_data(_city) == "Zurich" and city_query == 0:
        correct['temperature_2m_zh'] = data_combined.loc[('temperature_2m')].temperature_2m
        correct['surface_pressure_zh'] = data_combined.loc[('surface_pressure')].surface_pressure
        correct['wind_speed_10m_zh'] = data_combined.loc[('wind_speed_10m')].wind_speed_10m
        correct['wind_direction_10m_zh'] = data_combined.loc[('wind_direction_10m')].wind_direction_10m
        correct['wind_gusts_10m_zh'] = data_combined.loc[('wind_gusts_10m')].wind_gusts_10m
    elif load_data(_city) == "Zurich" and city_query == 1:
        correct['temperature_2m_lu'] = data_combined.loc[('temperature_2m')].temperature_2m
        correct['surface_pressure_lu'] = data_combined.loc[('surface_pressure')].surface_pressure
        correct['wind_speed_10m_lu'] = data_combined.loc[('wind_speed_10m')].wind_speed_10m
        correct['wind_direction_10m_lu'] = data_combined.loc[('wind_direction_10m')].wind_direction_10m
        correct['wind_gusts_10m_lu'] = data_combined.loc[('wind_gusts_10m')].wind_gusts_10m
    elif load_data(_city) == "Innsbruck" and city_query == 2:
        correct['temperature_2m_in'] = data_combined.loc[('temperature_2m')].temperature_2m
        correct['surface_pressure_in'] = data_combined.loc[('surface_pressure')].surface_pressure
        correct['wind_speed_10m_in'] = data_combined.loc[('wind_speed_10m')].wind_speed_10m
        correct['wind_direction_10m_in'] = data_combined.loc[('wind_direction_10m')].wind_direction_10m
        correct['wind_gusts_10m_in'] = data_combined.loc[('wind_gusts_10m')].wind_gusts_10m
    elif load_data(_city) == "Innsbruck" and city_query == 3:
        correct['temperature_2m_bo'] = data_combined.loc[('temperature_2m')].temperature_2m
        correct['surface_pressure_bo'] = data_combined.loc[('surface_pressure')].surface_pressure
        correct['wind_speed_10m_bo'] = data_combined.loc[('wind_speed_10m')].wind_speed_10m
        correct['wind_direction_10m_bo'] = data_combined.loc[('wind_direction_10m')].wind_direction_10m
        correct['wind_gusts_10m_bo'] = data_combined.loc[('wind_gusts_10m')].wind_gusts_10m
    return correct

# Example
if __name__=="__main__":
    data_pro = data_preprocessing(1)
    print(data_pro)

    # #Getting 'date' from the Multindex to be used in the future covariates

    # correct['dayofyear'] = correct.index.get_level_values('date').dayofyear

    # #sin and cos calculation

    # correct['day_sin'] = np.sin(2 * np.pi * correct['dayofyear'] / 365.0)
    # correct['day_cos'] = np.cos(2 * np.pi * correct['dayofyear'] / 365.0)
    # originalindex = correct.index
    # scaler = MinMaxScaler()
    # target_scaler = MinMaxScaler()
    # target_scaler.fit(correct[['surface_pressure_zh']])
    # scaled_data = pd.DataFrame(scaler.fit_transform(correct), columns=scaler.get_feature_names_out())
    # scaled_data.index = originalindex
    # target = scaled_data[['surface_pressure_zh']]
    # past_cov = scaled_data.drop(columns=['dayofyear', 'day_sin', 'day_cos'])
    # future_cov = scaled_data[['dayofyear', 'day_sin', 'day_cos']]
    # train_start = '2024-02-10 00:00:00+00:00'
    # train_end = '2024-03-03 23:00:00+00:00' #70% = 21 days
    # train_future_end ='2024-03-04 02:00:00+00:00'

    # val_start = '2024-03-04 00:00:00+00:00'
    # val_end = '2024-03-12 20:00:00+00:00'
    # val_future_end = '2024-03-12 23:00:00+00:00'

    # test_start = '2024-03-13 00:00:00+00:00'
    # test_end = '2024-03-15 23:00:00+00:00'

    # y_train = target.loc[train_start:train_end]
    # past_cov_train = past_cov.loc[train_start:train_end]
    # future_cov_train = future_cov.loc[train_start:train_future_end]

    # y_val = target.loc[val_start:val_end]
    # past_cov_val = past_cov.loc[val_start:val_end]
    # future_cov_val = future_cov.loc[val_start:val_future_end]

    # y_test = target.loc[test_start:test_end]

    # y_train_backtest = target.loc[train_start:val_end]
    # past_cov_train_backtest = past_cov.loc[train_start:val_end]
    # future_cov_train_backtest = future_cov.loc[train_start:val_future_end]
    # y_train_series = TimeSeries.from_dataframe(y_train)
    # past_cov_train_series = TimeSeries.from_dataframe(past_cov_train)
    # future_cov_train_series = TimeSeries.from_dataframe(future_cov_train)

    # y_val_series = TimeSeries.from_dataframe(y_val)
    # past_cov_val_series = TimeSeries.from_dataframe(past_cov_val)
    # future_cov_val_series = TimeSeries.from_dataframe(future_cov_val)

    # y_test_series = TimeSeries.from_dataframe(y_test)

    # y_train_backtest_series = TimeSeries.from_dataframe(y_train_backtest)
    # past_cov_train_backtest_series = TimeSeries.from_dataframe(past_cov_train_backtest)
    # future_cov_train_backtest_series = TimeSeries.from_dataframe(future_cov_train_backtest)
