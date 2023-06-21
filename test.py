import pandas as pd
import plotly.express as px
grabber = pd.DataFrame({"lat":[1,2,3,4,5,6,7,8,9], "lon":[1,2,3,4,5,6,7,8,9], 
    "second": [1,2,3,4,5,6,7,8,9]})

'''df = px.data.gapminder()

print(df[["year", "country", "gdpPercap"]])

fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])'''

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