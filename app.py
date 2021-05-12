"""
app.py:
Archivo para cargar la
funcionalidad de Dash
"""
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    title='Instituto Municipal de Planeación y Gestión Urbana - IMPLANG',
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1.0'
        }
    ]
)
app.config.suppress_callback_exceptions = True
server = app.server
