<h1>Jaw-P-project</h1>
<h2>Just another weather - Prediction</h2>
by
<h2>Elena Battiston, Florence Friebel, Jessica Jähne, Vincenzo Zeni</h2>
#<p>A <a href="http://example.com">link</a>.</p>
#links to profiles?

<h2>What's it all about:</h2>
Föhn is alpine weather phenomenom and a paragliders hassel
A simple Defenition:
Föhn is defined as sudden gust of wind created by pressure difference on both sides of the alpine range.
Paragliding is a weather dependend outdoor sport. To do it in save conditions we prefer the pressure difference not exceeding 4 hPa between the north and south side of the Alps.
With this project we aim to give a dipslay of conditions betweeen two locations paired to locations on the other side of the alpine range.
To keep it simple we decided to give a forecast of 3 h from a API request.
The locations choosen are Zürich-Lugano and Innsbruck-Bolzano. Where Zurich and Innsbruck are located north of the alpine range and two in the south, Bolzano and Lugano.


<h2>Data source </h2>
**Licence**
By using the Free API from <a href="https://open-meteo.com/en/terms">open-meteo</a> for non-commercial use, we thankful to open-meteo for their 1000 free API-calls per day. And we could use their great work for our project, because the provided data structure is amazing, making the use straight forward.
We utilized the open-meteo website for educational purposes and furthered our understanding of Timeseries, Back-end, Docker and Frontend, building upon our existing knowledge.

<h2>Method</h2>
For this _timeseries_-project we wanted to test different _prediction-possibilities. And there fore we used the _Darts_-library. Testing different _model_. Starting with _BlockRNN_ and _Transformer_ _Model_. Finally trained with the _TFT- Model_. We checked for _unscaled-Data_ and in the end chose _MinMax-Scaler_- We evaluted the prediction using _SMAPE_, that was not realy convincing and used _MAE_ metrics at the End.
The _Streamlit_-FrontEnd was based on an API created with _FastApi_ and _DockerImages_. The setup was deployed to _Google_ _Cloud_.
The model has been trained for one year of Data. The features are:

temperature_2m	Instant	°C 	Air temperature at 2 meters above ground

wind_speed_10m
Instant	km/h	Wind speed at 10 meters above ground. Wind speed on 10 meters is the standard level.

wind_direction_10m Instant	°	Wind direction at 10 meters above ground

wind_gusts_10m	Preceding hour max	km/h Gusts at 10 meters above ground as a maximum of the preceding hour

The Target is :
surface_pressure	Instant	hPa	Atmospheric air pressure reduced to mean sea level or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation.

<h2>Licence and Contributing</h2>
is this necessary!
API will be switched of because of GCP -running costs!


<h2>Acknowledgements</h2>

Thank to leWagon TAs for batch #1601
