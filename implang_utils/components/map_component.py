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


def map_component_go(data=[]):
    "Create a Plotly map with the observations"
    z_value = get_z(df_scores, data)
    colorscale = graph_color_scale()
    
    fig = go.Figure(go.Choroplethmapbox(geojson=json_scores, 
                                    locations=df_scores.id,
                                    z= z_value,
                                    colorscale= colorscale,
                                    zmin=1,
                                    zmax=5,
                                    marker_opacity=(z_value/10) + 0.4, 
                                    marker_line_width=0,
                                    hoverinfo='all'))

    fig.update_layout(mapbox_style="stamen-toner",
                      autosize=True,
                      mapbox_center = {"lat": 25.6551647, "lon": -100.3948332},
                      mapbox_zoom=12)

    return dcc.Graph(figure=fig)


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

    # Make background transparent
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0,0,0,0)'
    })

    return dbc.Card(
        [
            dbc.CardHeader(html.H2("Mapas")),
            dbc.CardBody(
                dcc.Graph(figure=fig, responsive=True)
            )
        ]
    )
