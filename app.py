"""
app.py:
Archivo para cargar la
funcionalidad de Dash
"""
import dash
import dash_bootstrap_components as dbc

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
app.config.suppress_callback_exceptions = True
server = app.server
