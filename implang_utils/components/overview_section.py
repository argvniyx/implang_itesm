"""
overview_section.py:
Componente que resume las cantidades de
defectos/observaciones de banquetas
"""
import dash_bootstrap_components as dbc
import dash_html_components as html
from functools import reduce
from implang_utils.data.dataframe import df_points
from implang_utils.components.utils import highlight
from implang_utils.components.count_report import observation_types

total_observations = df_points.shape[0]
def overview_section():
    "DB Component<Container>"

    observation_string = f'{total_observations} observaciones de banquetas'
    return dbc.Container(
        [
            html.H1("En SPGG"),
            html.Div(
                [
                    html.H5(
                        [
                            "Se han hecho un total de ",
                            html.U(observation_string),
                        ]
                    ),
                    observation_types,
                ],
            ),
            html.Div(
                children=[],
                id="count_report"
            )
        ],
        fluid=True
    )