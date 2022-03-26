from greppo import app
import numpy as np
import geopandas as gpd
import pandas as pd
import numpy as np

app.map(max_zoom=25, min_zoom=4)
app.base_layer(
    name="CartoDB Light",
    visible=True,
    url="https://cartodb-basemaps-a.global.ssl.fastly.net/light_all/{z}/{x}/{y}@2x.png",
    subdomains=None,
    attribution='&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
)

app.base_layer(
    provider="CartoDB Positron"
)
# Possible alternative names:

provider = "CartoDB Positron"
provider = "cartodbpositron"
provider = "cartodb-positron"
provider = "carto db/positron"
provider = "CARTO_DB_POSITRON"
provider = "CartoDB.Positron"

data_gdf_1 = gpd.read_file("test/data/communes.geojson")

data_gdf_1["Value"] = pd.Series(
    np.ones(len(data_gdf_1["code"])),
    index=data_gdf_1.index,
)

app.overlay_layer(
    data_gdf_1,
    name="Communes",
    description="Communes in Normandy, France",
    style={"fillColor": "#F87979"},
    visible=True,
)
