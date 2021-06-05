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

add = lambda a,b: a+b
positive_counts = reduce(add, map(lambda x: x[1], [(k, v) for k,v in defect_counts.iteritems() if k in positive_labels]))
neutral_counts = reduce(add, map(lambda x: x[1], [(k, v) for k,v in defect_counts.iteritems() if k in neutral_labels]))
negative_counts = reduce(add, map(lambda x: x[1], [(k, v) for k,v in defect_counts.iteritems() if k in negative_labels]))

label_counts = {
    "Positivas": positive_counts,
    "Neutrales": neutral_counts,
    "Negativas": negative_counts
}

label_colors = {
    "Positivas": "success",
    "Neutrales": "info",
    "Negativas": "danger"
}

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
                    html.H5(label, className="card-title", style={"color": "white" if label != "Neutrales" else "black"}),
                    html.P(label_counts[label], className="card-text", style={"color": "white" if label != "Neutrales" else "black"}),
                ]
            ),
            className="mt-3 md-3",
            color=label_colors[label]
        )
        for label in label_counts
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
