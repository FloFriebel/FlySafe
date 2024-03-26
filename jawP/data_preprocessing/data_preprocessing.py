
from sklearn.preprocessing import MinMaxScaler
from darts import TimeSeries
import pandas as pd
import numpy as np
from jawp.data_preprocessing.load_data import load_data

def data_preprocessing(_start, _end):
    correct = load_data(_start, _end)

    # #Getting 'date'  to be used in the future covariates
    correct['dayofyear'] = correct.index.get_level_values('date').dayofyear

    #sin and cos calculation
    correct['day_sin'] = np.sin(2 * np.pi * correct['dayofyear'] / 365.0)
    correct['day_cos'] = np.cos(2 * np.pi * correct['dayofyear'] / 365.0)
    originalindex = correct.index

    #Scaling
    scaler = MinMaxScaler()
    target_scaler = MinMaxScaler()
    target_scaler.fit(correct[['surface_pressure_zh', 'surface_pressure_lu', 'surface_pressure_in', 'surface_pressure_bo']])
    scaled_data = pd.DataFrame(scaler.fit_transform(correct), columns=scaler.get_feature_names_out())
    scaled_data.index = originalindex
    target = scaled_data[['surface_pressure_zh', 'surface_pressure_lu', 'surface_pressure_in', 'surface_pressure_bo']]

    #Covariates and train test split
    past_cov = scaled_data.drop(columns=['dayofyear', 'day_sin', 'day_cos'])
    future_cov = scaled_data[['dayofyear', 'day_sin', 'day_cos']]

    #validation data
    val_start = '2024-03-04 00:00:00+00:00'
    val_end = '2024-03-12 20:00:00+00:00'
    val_future_end = '2024-03-12 23:00:00+00:00'

    #defining target adn features( no x and y in timeseries)
    y_val = target.loc[val_start:val_end]
    past_cov_val = past_cov.loc[val_start:val_end]
    future_cov_val = future_cov.loc[val_start:val_future_end]

    #Conversion to Timesseries
    y_val_series = TimeSeries.from_dataframe(y_val)
    past_cov_val_series = TimeSeries.from_dataframe(past_cov_val)
    future_cov_val_series = TimeSeries.from_dataframe(future_cov_val)

    return (y_val_series, past_cov_val_series, future_cov_val_series, target_scaler)


# Example
if __name__=="__main__":
    data_pro = data_preprocessing("2024-02-10", "2024-03-15")
    print(data_pro)





    # train_start = '2024-02-10 00:00:00+00:00'
    # train_end = '2024-03-03 23:00:00+00:00' #70% = 21 days
    # train_future_end ='2024-03-04 02:00:00+00:00'

    # test_start = '2024-03-13 00:00:00+00:00'
    # test_end = '2024-03-15 23:00:00+00:00'

    # y_train = target.loc[train_start:train_end]
    # past_cov_train = past_cov.loc[train_start:train_end]
    # future_cov_train = future_cov.loc[train_start:train_future_end]



    # y_test = target.loc[test_start:test_end]

    # y_train_backtest = target.loc[train_start:val_end]
    # past_cov_train_backtest = past_cov.loc[train_start:val_end]
    # future_cov_train_backtest = future_cov.loc[train_start:val_future_end]

    # y_train_series = TimeSeries.from_dataframe(y_train)
    # past_cov_train_series = TimeSeries.from_dataframe(past_cov_train)
    # future_cov_train_series = TimeSeries.from_dataframe(future_cov_train)



    # y_test_series = TimeSeries.from_dataframe(y_test)

    # y_train_backtest_series = TimeSeries.from_dataframe(y_train_backtest)
    # past_cov_train_backtest_series = TimeSeries.from_dataframe(past_cov_train_backtest)
    # future_cov_train_backtest_series = TimeSeries.from_dataframe(future_cov_train_backtest)
