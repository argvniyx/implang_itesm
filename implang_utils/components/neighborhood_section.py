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
from implang_utils.components.count_report import neighborhood_report
from implang_utils.components.utils import highlight

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

n_summary_component = dbc.Row(
    [
        dbc.Col(
            html.H3(
                "Da click en los botones de 'Más Información' para explorar las calificaciones de las etiquetas"
            )
        )
    ]
)

def neighborhood_section():
    "Card component with neighborhood stats"
    return dbc.Col(
        [
            dbc.Row(
                dbc.Col(
                    dbc.Jumbotron(
                        [
                            html.H1("Una manera de priorizar"),
                            html.H5("es a través de las colonias:"),
                            neighborhood_report
                        ],
                    ),
                )
            ),
            dbc.Row(
                dbc.Col(
                    [
                        n_summary_component
                    ],
                    id="count_report_neighborhood"
                )
            )
        ],
    )
