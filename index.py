"""
index.py:
Archivo que se encarga de enrutar.
Se requiere separar la inicialización de
la `app` para evitar dependencias
circulares. Así, podemos también separar
los callbacks.
"""
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from app import app
from apps import home, itesm


app.layout = dbc.Container(
    [
        dbc.NavbarSimple(
            [
                dbc.Button('ITESM', href='/apps/itesm', color='light'),
            ],
            brand='IMPLANG',
            brand_href='/apps/home'
        ),
        html.Div(id='page-content', children=[]),
        dcc.Location(id='url', refresh=False)
    ]
)


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    "Enrutamiento de las páginas"
    if pathname == '/apps/itesm':
        return itesm.layout

    return home.layout


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
