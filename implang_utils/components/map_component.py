"""
map_component.py:
Componente para cargar el mapa con información
de los geojson provistos por IMPLANG
"""
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from implang_utils.data.dataframe import df_points
from implang_utils.data.dataframe import df_denue_filtered
from implang_utils.data.dataframe import df_inegi
from implang_utils.data.dataframe import df_scores
from implang_utils.data.dataframe import json_scores

from implang_utils.components.utils import graph_color_scale
from implang_utils.components.utils import get_z
from implang_utils.components.utils import get_title
""" fig = px.histogram(df1, x="reviews_per_month", y="price", color="room_type", marginal="rug")
fig.show() """
def map_component_go(data=[]):
    "Create a Plotly map with the observations"
    return html.Div([
        dcc.Checklist(
            id='demo-checklist',
    options=[
            {'label': 'Banquetas', 'value': 'P'},
            {'label': 'Personas de Riesgo', 'value': 'PR'},
            {'label': 'Establecimientos', 'value': 'EST'}
            ],
    value=['P'])  ,
        html.Div(id='dd-output-container')
        ])


def map_componet_points():
    df_points["severity"].fillna(1, inplace=True)
    df_points["severity_norm"] = ((df_points['severity']-min(df_points['severity']))/(max(df_points['severity'])-min(df_points['severity']))) / 2
    "Create a Plotly map with the observations"
    fig = px.scatter_mapbox(df_points,
                        lat=df_points.geometry.y,
                        lon=df_points.geometry.x,
                        mapbox_style="stamen-toner",
                        color="label_type", 
                        hover_data=["neighborhood"],
                        #size = "severity",
                        opacity= df_points.severity_norm,
                        zoom=13)
    
    fig.update_layout(autosize=True)

    return dcc.Graph(figure=fig)
    

# This functions below are for testing purposes
def map_component():
    "Create a Plotly map with the observations"
    fig = px.scatter_mapbox(df_points,
                            lat=df_points.geometry.y,
                            lon=df_points.geometry.x,
                            hover_name="label_type",
                            mapbox_style="stamen-toner",
                            zoom=13)
    fig.update_layout(autosize=True)

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
    fig.update_layout(autosize=True)

    return dcc.Graph(figure=fig)


def map_component_inegi():
    # Copy the original map to avoid mutating global state
    gdf = df_inegi
    gdf['boundary'] = gdf.boundary
    gdf['centroid'] = gdf.centroid

    ncrs = gdf.set_geometry("centroid").to_crs(epsg=4236)

    fig = px.scatter_mapbox(ncrs,
                            lat=ncrs.geometry.y,
                            lon=ncrs.geometry.x,
                            mapbox_style="stamen-toner",
                            zoom=12)

    fig.update_layout(autosize=True)

    return dbc.Card(
        [
            dbc.CardHeader(html.H2("Mapas")),
            dbc.CardBody(
                dcc.Graph(figure=fig, responsive=True)
            )
        ]
    )
