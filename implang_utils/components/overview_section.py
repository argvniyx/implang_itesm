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

# Components
# TODO:
# Fix width problems (wrap, or make a 3 x 4 container)
cards = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(defect, className="card-title"),
                    html.P(defect_counts[defect], className="card-text")
                ]
            ),
            style={"flex": "0 0 auto", "width": "20em"},
            className="mt-3"
        )
        for defect in defect_counts.keys()
    ],
    style={
        "alignContents": "space-between",
        "justifyContent": "center",
        "alignItems": "center"
    }
)


def overview_section():
    "DB Component<Container>"

    return dbc.CardBody(
        [
            html.H2("En resumen", className="card-title", style={"textAlign": "center"}),
            html.H5(
                [
                    "Hay un total de ", highlight(f'{total_defects} defectos en banquetas')
                ]
            ),
            cards
        ],
        style={ "textAlign": "center" }
    )