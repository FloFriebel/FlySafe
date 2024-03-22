from pytorch_lightning.callbacks.early_stopping import EarlyStopping

def predict():
    input_chunk_length = 24
    output_chunk_length = 3
    my_stopper = EarlyStopping(
    monitor="val_loss",
    patience=100,
    min_delta=0.0001,
    mode='min',
)

    # use GPU
    pl_trainer_kwargs={"callbacks": [my_stopper],
                    "accelerator": "gpu",
                    "devices": [0]}

    # use CPU
    #pl_trainer_kwargs={"callbacks": [my_stopper],
                    #"accelerator": "cpu"}

    # Advanced tuning
    tft = TFTModel(input_chunk_length =input_chunk_length ,
                output_chunk_length = output_chunk_length,
                pl_trainer_kwargs = pl_trainer_kwargs,
                lstm_layers=2,
                num_attention_heads=8,
                dropout=0.2,
                batch_size=16,
                hidden_size=64,
                torch_metrics=MeanAbsoluteError(),
                n_epochs=200,
                # add_encoders=add_encoders
                )
    tft.fit(series=y_train_series,
        past_covariates = past_cov_train_series,
        future_covariates = future_cov_train_series,
        val_series=y_val_series,
        val_past_covariates=past_cov_val_series,
        val_future_covariates=future_cov_val_series)

    preds = tft.predict(n=output_chunk_length,
                   series=y_val_series,
                   past_covariates = past_cov_val_series,
                   future_covariates = future_cov_val_series)
    preds.plot(label='prediction_pressure')
    y_test_series[:output_chunk_length].plot()
    historical_fcast_tft = tft.historical_forecasts(
        series=y_train_backtest_series,
        past_covariates=past_cov_train_backtest_series,
        future_covariates=future_cov_train_backtest_series,
        start=0,
        forecast_horizon=7,
        verbose=False,
        retrain=False
    )
    y_train_backtest_series.plot(label="data")
    historical_fcast_tft.plot(low_quantile=0.01, high_quantile=0.99,label="backtest ahead forecast (TFTModel)")
