"""
app.py:
Archivo para cargar la
funcionalidad de Dash
"""
from implang_utils.components.utils import get_title, get_z, graph_color_scale
from implang_utils.components.map_component import map_component_go
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from implang_utils.data.dataframe import df_scores
from implang_utils.data.dataframe import json_scores
import plotly.graph_objects as go
BOOTSTRAP_ICONS = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css"
external_scripts = [
    'helper.js'
]
app = dash.Dash(
    __name__,
    title='Instituto Municipal de Planeación y Gestión Urbana - IMPLANG',
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        BOOTSTRAP_ICONS
    ],
    meta_tags=[
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        }
    ], 
    # This is to have external JS scripts external_scripts=external_scripts
)
@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    if value == 'A':
        data = ['Score_PTS']
        z_value = get_z(df_scores, data)
        colorscale = graph_color_scale()
        title = get_title(data)
        fig = go.Figure(go.Choroplethmapbox(geojson=json_scores, 
                                    locations=df_scores.id,
                                    z= z_value,
                                    colorscale= colorscale,
                                    zmin=1,
                                    zmax=5,
                                    marker_opacity=(z_value/10) + 0.4, 
                                    marker_line_width=0,
                                    hoverinfo='all'))

        fig.update_layout(title=title,
                      mapbox_style="stamen-toner",
                      autosize=True,
                      mapbox_center = {"lat": 25.6551647, "lon": -100.3948332},
                      mapbox_zoom=12)
        return dcc.Graph(figure=fig)
    elif value == 'B':
        data = ['Score_PTS', 'Score_EST']
        z_value = get_z(df_scores, data)
        colorscale = graph_color_scale()
        title = get_title(data)
        fig = go.Figure(go.Choroplethmapbox(geojson=json_scores, 
                                    locations=df_scores.id,
                                    z= z_value,
                                    colorscale= colorscale,
                                    zmin=1,
                                    zmax=5,
                                    marker_opacity=(z_value/10) + 0.4, 
                                    marker_line_width=0,
                                    hoverinfo='all'))

        fig.update_layout(title=title,
                      mapbox_style="stamen-toner",
                      autosize=True,
                      mapbox_center = {"lat": 25.6551647, "lon": -100.3948332},
                      mapbox_zoom=12)
        return dcc.Graph(figure=fig)
    elif value == 'C':
        data = ['Score_PTS', 'Score_PR']
        z_value = get_z(df_scores, data)
        colorscale = graph_color_scale()
        title = get_title(data)
        fig = go.Figure(go.Choroplethmapbox(geojson=json_scores, 
                                    locations=df_scores.id,
                                    z= z_value,
                                    colorscale= colorscale,
                                    zmin=1,
                                    zmax=5,
                                    marker_opacity=(z_value/10) + 0.4, 
                                    marker_line_width=0,
                                    hoverinfo='all'))

        fig.update_layout(title=title,
                      mapbox_style="stamen-toner",
                      autosize=True,
                      mapbox_center = {"lat": 25.6551647, "lon": -100.3948332},
                      mapbox_zoom=12)
        return dcc.Graph(figure=fig)
    elif value == 'D':
        data = ['Score_PTS', 'Score_EST', 'Score_PR']
        z_value = get_z(df_scores, data)
        colorscale = graph_color_scale()
        title = get_title(data)
        fig = go.Figure(go.Choroplethmapbox(geojson=json_scores, 
                                    locations=df_scores.id,
                                    z= z_value,
                                    colorscale= colorscale,
                                    zmin=1,
                                    zmax=5,
                                    marker_opacity=(z_value/10) + 0.4, 
                                    marker_line_width=0,
                                    hoverinfo='all'))

        fig.update_layout(title=title,
                      mapbox_style="stamen-toner",
                      autosize=True,
                      mapbox_center = {"lat": 25.6551647, "lon": -100.3948332},
                      mapbox_zoom=12)
        return dcc.Graph(figure=fig)
app.config.suppress_callback_exceptions = True
server = app.server
