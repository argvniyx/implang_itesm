"""
overview_section.py:
Componente que resume las cantidades de
defectos/observaciones de banquetas
"""
import dash_bootstrap_components as dbc
import dash_html_components as html
from implang_utils.data.dataframe import df_points
from implang_utils.components.utils import highlight

total_defects = df_points.shape[0]
defect_counts = df_points["label_type"].value_counts()

cards = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(defect, className="card-title"),
                    html.P(defect_counts[defect], className="card-text")
                ]
            ),
            className="mt-3 md-3"
        )
        for defect in defect_counts.keys()
    ],
)


def overview_section():
    "DB Component<Container>"

    return dbc.Card(
       [
           dbc.CardBody(
               [
                   html.H2("En resumen", className="card-title"),
                   html.H5(
                       [
                           "Hay un total de ",
                           highlight(
                               f'{total_defects} defectos en banquetas'
                           )
                       ]
                   ),
                   cards
               ],
           )
       ]
    )
