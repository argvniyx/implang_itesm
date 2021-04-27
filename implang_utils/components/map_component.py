"""
map_component.py:
Componente para cargar el mapa con información
de los geojson provistos por IMPLANG
"""
import dash_core_components as dcc
import plotly.express as px

from implang_utils.data.dataframe import df_points
from implang_utils.data.dataframe import df_denue_filtered

def map_component():
    "Create a Plotly map with the observations"
    fig = px.scatter_mapbox(df_points,
                            lat=df_points.geometry.y,
                            lon=df_points.geometry.x,
                            hover_name="label_type",
                            mapbox_style="stamen-toner",
                            zoom=13)

    return dcc.Graph(figure=fig)

def map_component_denue():
    "Create a Plotly map with the observations"
    fig = px.scatter_mapbox(df_denue_filtered,
                        lat=df_denue_filtered.geometry.y,
                        lon=df_denue_filtered.geometry.x,
                        mapbox_style="stamen-toner",
                        color="categoria_act", 
                        hover_data=["nom_estab"],
                        size="per_ocu_cat",
                        zoom=13)

    return dcc.Graph(figure=fig)
