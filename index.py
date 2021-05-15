"""
index.py:
Archivo que se encarga de enrutar.
Se requiere separar la inicialización de
la `app` para evitar dependencias
circulares. Así, podemos también separar
los callbacks.
"""
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from dash.dependencies import ClientsideFunction, Input, Output
from app import app
from apps import home, itesm


app.layout = html.Div(
    [
        dbc.Container([], id='page-content', fluid=True),
        dcc.Location(id='url', refresh=False),
        html.Div([], id="hijack-target")
    ],
    id="top-container"
)


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')],
    prevent_initial_call=True
)
def display_page(pathname):
    "Enrutamiento de las páginas"
    if pathname == '/apps/itesm':
        return itesm.layout

    return home.layout


app.clientside_callback(
    ClientsideFunction(
        namespace="clientside",
        function_name="scrollHijack"
    ),
    Output("hijack-target", "n_clicks"),
    Input('url', 'pathname'),
    prevent_initial_call=True
)


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
