"""
overview_section.py:
Componente que resume las cantidades de
defectos/observaciones de banquetas
"""
import dash_bootstrap_components as dbc
import dash_html_components as html
from implang_utils.data.dataframe import df_points
from implang_utils.components.utils import highlight
from implang_utils.components.count_report import observation_types

total_observations = df_points.shape[0]

data_summary_component = dbc.Row(
    [
        dbc.Col(
            html.H3(
                "Da click en los botones de 'Más Información' para explorar las calificaciones de las etiquetas"
            )
        )
    ]
)


def overview_section():
    "DB Component<Container>"

    observation_string = f'{total_observations} observaciones de banquetas'
    return dbc.Col(
        [
            dbc.Row(
                dbc.Col(
                    dbc.Jumbotron(
                        [
                            html.H1("En SPGG"),
                            html.H5(
                                [
                                    "De un total de ",
                                    html.U(observation_string),
                                    ", se registran:"
                                ]
                            ),
                            observation_types,
                        ],
                    ),
                )
            ),
            dbc.Row(
                dbc.Col(
                    [
                        data_summary_component
                    ],
                    id="count_report"
                )
            )
        ],
    )
