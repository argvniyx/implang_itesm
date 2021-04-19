"""
map_component.py:
Componente para cargar el mapa con información
de los geojson provistos por IMPLANG
"""
import dash_core_components as dcc
import plotly.express as px

from implang_utils.data.dataframe import df_points


def map_component():
    fig = px.scatter_mapbox(df_points,
                            lat=df_points.geometry.y,
                            lon=df_points.geometry.x,
                            hover_name="label_type",
                            mapbox_style="stamen-toner",
                            zoom=13)

    return dcc.Graph(figure=fig)
