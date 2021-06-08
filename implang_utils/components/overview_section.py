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
'''
table_header = [
    html.Thead(html.Tr([html.Th("Nivel de emergencia"), html.Th("Ejemplo")]))
]

row1 = html.Tr([html.Td("1"), html.Td(html.Img(src='../../assets/1.png', style={'height':'10%', 'width':'10%'}))])
row2 = html.Tr([html.Td("2"), html.Td(html.Img(src='../../assets/2.png', style={'height':'10%', 'width':'10%'}))])
row3 = html.Tr([html.Td("3"), html.Td(html.Img(src='../../assets/3.png', style={'height':'10%', 'width':'10%'}))])
row4 = html.Tr([html.Td("4"), html.Td(html.Img(src='../../assets/4.png', style={'height':'10%', 'width':'10%'}))])

table_body = [html.Tbody([row1, row2, row3, row4])]

table = dbc.Table(table_header + table_body, bordered=True)
'''
row = html.Div(
    [
        dbc.Row([
            html.H1("Ejemplos de problemas en las banquetas"),
        ]),
        dbc.Row([
            html.H4("1 siendo lo menos importante y 5 siendo lo más importante")
        ]),
        dbc.Row(
            [
                dbc.Col(html.Div(html.Img(src='../../assets/1.png', style={'height':'100%', 'width':'100%'}))),
                dbc.Col(html.Div(html.Img(src='../../assets/2.png', style={'height':'100%', 'width':'100%'}))),
                dbc.Col(html.Div(html.Img(src='../../assets/3.png', style={'height':'100%', 'width':'100%'}))),
                dbc.Col(html.Div(html.Img(src='../../assets/4.png', style={'height':'100%', 'width':'100%'}))),
                dbc.Col(html.Div(html.Img(src='../../assets/5.png', style={'height':'100%', 'width':'100%'}))),
            ]
        ),
    ], style={'display': 'flex', 'flexDirection': 'column', 'position': 'absolute', 'bottom': '-55vh'}
)

def overview_section():
    "DB Component<Container>"

    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H1("En SPGG", className="card-title"),
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
                    row
                ],
            ),
        ]
    )
