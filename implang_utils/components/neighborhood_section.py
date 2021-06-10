"""
neighborhood_section.py:
Componente para mostrar información
numérica de colonias
"""
from implang_utils.components.utils import graph_color_scale
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc
from implang_utils.data.dataframe import df_points

neighborhoods = df_points["neighborhood"].value_counts()


# Generating the Components
def tab_content(title):
    "Create a DBC Tab with a structure"
    return dbc.Card(
        dbc.CardBody([
            html.H3(title),
            html.P(["Total de imperfectos: ", neighborhoods[title]])
        ]),
        className="mt-3")

def histogram_neighborhood():
    fig = px.histogram(df_points, x="neighborhood", color_discrete_sequence=['#a23e48'])
    return dcc.Graph(figure=fig)

def neighborhood_section():
    "Card component with neighborhood stats"
    return dbc.Card(
        [
            dbc.CardHeader(html.H2("Las colonias")),
            dbc.CardBody(
                [
                    dbc.Tabs(
                        [
                            dbc.Tab(tab_content(t), label=t)
                            for t in neighborhoods.keys()
                        ]
                    )
                ]
            ),
            html.Div(
            [
                dbc.Row(
                [
                    dbc.Col(histogram_neighborhood()),
                    dbc.Col(html.Div(html.Img(src='../../assets/streetDisability.jpg', style={'height':'100%', 'width':'100%', 'marginLeft': '-1vw'})), width=5)
                ],
                className="m-0"
            ),
            ]
            ),
        ]
    )
