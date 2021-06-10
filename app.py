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
    [dash.dependencies.Input('demo-checklist', 'value')])

def update_output(value):
    data = []
    for e in value:
        if e == 'P' :
            data.append('Score_PTS')
        
        elif e =='PR' :
            data.append('Score_PR')
        
        elif e == 'EST':
            data.append('Score_EST')
    
    title = get_title(data)
    title_size = title.pop()
    title = title.pop()
    colorscale = graph_color_scale()

    if len(data) > 0:
        z_value = get_z(df_scores, data)
        fig = go.Figure(go.Choroplethmapbox(geojson=json_scores, 
                                    locations=df_scores.id,
                                    z= z_value,
                                    colorscale= colorscale,
                                    colorbar = dict(dtick = 1),
                                    zmin=1,
                                    zmax=5,
                                    marker_opacity=(z_value/10) + 0.4, 
                                    marker_line_width=0,))

    else:
        fig = go.Figure(go.Choroplethmapbox(geojson=json_scores, 
                                    locations=df_scores.id,
                                    colorscale= colorscale))
    fig.update_layout(
                    title=dict(text=title, font=dict(size=title_size)),
                    title_xref = "paper",
                    geo_bgcolor = 'rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor = 'rgba(0,0,0,0)',
                    height = 550,
                    mapbox_style="stamen-toner",
                    autosize=True,
                    mapbox_center = {"lat": 25.655624, "lon":-100.373121},
                    mapbox_zoom=11)
    return dcc.Graph(figure=fig, style= {'width' : '90%' } )
   
app.config.suppress_callback_exceptions = True
server = app.server
