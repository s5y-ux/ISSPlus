import urllib.request
import json 
import time
import pandas as pd
import plotly.express as px

Data = [[],[],[]]

i = 0

for count in range(500):
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']
    lat = float(lat)
    lon = float(lon)
    Data[0].append(lat)
    Data[1].append(lon)
    Data[2].append(i)
    i += 1
    time.sleep(1)

grabber = pd.DataFrame({"lat": Data[0], "lon": Data[1], "second":Data[2]})

fig = px.scatter_mapbox(grabber, lat="lat", lon="lon", animation_frame="second")
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
