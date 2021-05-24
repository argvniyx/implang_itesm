"""
overview_section.py:
Componente que resume las cantidades de
defectos/observaciones de banquetas
"""
import dash_bootstrap_components as dbc
import dash_html_components as html
from implang_utils.data.dataframe import df_points
from implang_utils.components.utils import highlight

label_translations = {
    "NoSidewalk": "No hay banqueta",
    "Obstacle": "Obstáculo",
    "SurfaceProblem": "Problema de superficie",
    "NoCurbRamp": "Sin Rampa",
    "CurbRamp": "Con Rampa",
    "Occlusion": "Obstrucción de vista",
    "Other": "Otro"
}

positive_labels = ["CurbRamp"]
neutral_labels = ["Other"]
negative_labels = [
    label for label in list(label_translations.keys())
    if label not in positive_labels + neutral_labels
]

total_defects = df_points.shape[0]
defect_counts = df_points["label_type"].value_counts()

positive_counts = len([p for p in defect_counts if p in positive_labels])
neutral_counts = len([p for p in defect_counts if p in neutral_labels])
negative_counts = len([p for p in defect_counts if p in negative_labels])


category_cards = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(label_translations[defect], className="card-title"),
                    html.P(defect_counts[defect], className="card-text")
                ]
            ),
            className="mt-3 md-3"
        )
        for defect in defect_counts.keys()
    ],
)

label_cards = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(label_translations[defect], className="card-title"),
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
                    html.H1("En San Pedro", className="card-title"),
                    html.H5(
                        [
                            "Se han hecho un total de ",
                            highlight(
                                html.Span(
                                    f'{total_defects} observaciones de banquetas:',
                                    className="text-light"
                                ),
                                "green"
                            ),
                        ]
                    ),
                    label_cards,
                    category_cards
                ],
            ),
        ]
    )
