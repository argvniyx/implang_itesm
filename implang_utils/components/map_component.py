"""
map_component.py:
Componente para cargar el mapa con información
de los geojson provistos por IMPLANG
"""
import dash_core_components as dcc
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

