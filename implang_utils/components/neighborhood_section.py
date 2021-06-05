"""
neighborhood_section.py:
Componente para mostrar información
numérica de colonias
"""
import dash_bootstrap_components as dbc
import dash_html_components as html

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
                    dbc.Col(html.Div(html.Img(src='../../assets/streetDisability.jpg', style={'height':'100%', 'width':'100%', 'margin-left': '30vw'})), width=5)
                ]
            ),
            ]
            ),
        ]
    )
