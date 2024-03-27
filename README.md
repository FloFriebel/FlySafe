<h1>Jaw-P-project</h1>
<h2>Just another weather - Prediction</h2>
<h2>by <a href="https://github.com/Elenya92">Elena Battiston</a>, <a href="https://github.com/FloFriebel">Florence Friebel</a>, <a href="https://github.com/jjaehne">Jessica Jähne</a>, <a href="https://github.com/VinceZeni">Vincenzo Zeni</a></h2>

<h2>What's it all about:</h2><br />
Föhn is alpine weather phenomenom and a paragliders hassel<br />

<img src="https://commons.wikimedia.org/wiki/File:Parapente_-_Les_Saisies_02.JPG?uselang=fr" longdesc="This is an image of a two-layered birthday cake." /> [<a href=
"description.html" title="long description of the image">D</a>]

<br />
A simple defenition:

Föhn is defined as sudden gust of wind created by pressure difference on both sides of the alpine range.
Paragliding is a weather dependend outdoor sport. To do it in save conditions we prefer the pressure difference not exceeding 4 hPa between the north and south side of the Alps.

With this project we aim to give a dipslay of conditions betweeen two locations paired to locations on the other side of the alpine range.
To keep it simple we decided to give a forecast of 3 h from a API request.
The locations choosen are Zürich-Lugano and Innsbruck-Bolzano. Where Zurich and Innsbruck are located north of the alpine range and two in the south, Bolzano and Lugano.


<h2>Data source </h2>
By using the Free API from <a href="https://open-meteo.com/en/terms">open-meteo</a> for non-commercial use, we thankful to open-meteo for their 1000 free API-calls per day. And we could use their great work for our project, because the provided data structure is amazing, making the use straight forward.
We utilized the open-meteo website for educational purposes and furthered our understanding of Timeseries, Back-end, Docker and Frontend, building upon our existing knowledge.

<h2>Method</h2>
For this <em>timeseries</em>-project we wanted to test different prediction-possibilities. And there fore we used the <em>Darts</em>-library. Testing different <em>mode</em>. Starting with <em>BlockRNN</em> and <em>Transformer</em> <em>Model</em>. Finally trained with the <em>TFT</em>-<em>Model</em>. We checked for <em>unscaled-Data</em> and in the end chose <em>MinMax-Scaler</em>. We evaluted the prediction using <em>SMAPE</em>, that was not realy convincing and used <em>MAE</em> metrics at the End.<br />
The <em>Streamlit</em>-FrontEnd was based on an API created with <em>FastApi</em> and <em>DockerImages</em>. The setup was deployed to <em>Google</em> <em>Cloud</em>.
The model has been trained for one year of Data. <br />

The <em>features</em> are:<br />
| Variable           | Valid time         | Unit | Description                                                                         |
| :---               |     :---:          |:---: | :---                                                                                |
| temperature_2m     | Instant            | °C   | Air temperature at 2 meters above ground                                            |
| wind_speed_10m     | Instant            | km/h | Wind speed at 10 meters above ground. Wind speed on 10 meters is the standard level.|
| wind_direction_10m | Instant            | °    | Wind direction at 10 meters above ground                                            |
| wind_gusts_10m     | Preceding hour max | km/h | Gusts at 10 meters above ground as a maximum of the preceding hour.                 |


<br />
The <em>target</em> is:<br />

| Variable         | Valid time | Unit | Description                                                                         |
| :---             |     :---:  |:---: | :---                                                                                |
| surface_pressure | Instant    | hPa  | Atmospheric air pressure reduced to mean sea level or pressure at surface. Typically pressure on mean sea level is used in meteorology. Surface pressure gets lower with increasing elevation.|

<h2>Licence and Contributing</h2>
API will be switched of because of GCP -running costs!

<h2>Acknowledgements</h2>
Thank to leWagon TAs for batch #1601 for helping us
