# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from components.header import header
from components.neighborhood_section import neighborhood_section
from components.section import section
from components.curb_evaluation import curb_evaluation
from components.overview_section import overview_section

app = dash.Dash(__name__,
                external_stylesheets=['assets/bootstrap.css'],
                meta_tags=[
                    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
])

sections = [
    neighborhood_section,
    curb_evaluation
]

layout = dbc.Container(
    children=[
        header(),
        overview_section(),
        *[section(func) for func in sections]
    ],
    fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
