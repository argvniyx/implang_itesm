"""
count_report.py:
A component that gives statistical information
on a list of counts
"""
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output, ALL
from dash.exceptions import PreventUpdate
from implang_utils.data.dataframe import df_points
from app import app

label_translations = {
    "NoSidewalk": "No hay banqueta",
    "Obstacle": "Obstáculo",
    "SurfaceProblem": "Problema de superficie",
    "NoCurbRamp": "Sin Rampa",
    "CurbRamp": "Rampa con imperfectos",
    "Occlusion": "Obstrucción de vista",
    "Other": "Otro"
}

label_descriptions = {
    "NoSidewalk": "Esta observación se hace a todo punto donde una banqueta pierda su continuación. No aplica a camellones a menos de que tengan un espacio explícitamente designado para el peatón.",
    "Obstacle": "Se denomina obstáculo todo objeto que impida el paso, y su severidad depende de qué tan fácil o difícil es rodearle. Ejemplos de esto pueden ser árboles o postes.",
    "SurfaceProblem": "Un problema de superficie puede ser una superficie agrietada, con grava o con desniveles.",
    "NoCurbRamp": "Estas observaciones corresponden a faltas de rampas, particularmente cuando se espera que haya (por ejemplo, en un cruce peatonal).",
    "CurbRamp": "Estas observaciones tienen que ver con la calidad de las rampas existentes. Si una rampa está mal posicionada, la observación tiene mayor severidad.",
    "Occlusion": "Se considera oclusión toda vez que una persona etiquetando puntos no pueda ver la banqueta con claridad. Por su naturaleza, éstas observaciones no tienen calificación.",
    "Other": "Todo otro tipo de observación que no se pueda explicar con las otras etiquetas se considera como Otro."
}

label_img_paths = {
    "NoSidewalk": "../../assets/noSidewalk.png",
    "Obstacle": "../../assets/obstacle.png",
    "SurfaceProblem": "../../assets/surfaceProblem.png",
    "NoCurbRamp": "../../assets/noCurbRamp.png",
    "CurbRamp": "../../assets/curbRamp.jpg",
    "Occlusion": "../../assets/occlusion.png",
    "Other": "../../assets/other.png"
}


def count_attr_of_col(dataframe, pred, attr):
    """
    count_attr_of_col takes a dataframe and a predicate
    that acts as a filter for the dataframe. Then, it
    counts occurrences of `attr` in that dataframe, returning
    a list of pairs with the attribute's value and its count
    """
    total_of_col = dataframe[pred()]
    if attr is not None:
        attr_count = total_of_col[attr].value_counts()
    else:
        attr_count = total_of_col.value_counts()

    return [(a, attr_count[a]) for a in attr_count.keys()]


def count_attr_of_col_df(dataframe, pred, attr):
    """
    Same as count_attr_of_col but instead returns a dataframe
    as processed by groupby and aggregated with .count(). This
    way we can use the results with plotly
    """
    total_of_col = dataframe[pred()]
    if attr is None:
        attr_count = total_of_col.shape[0]
    else:
        attr_count = total_of_col.groupby(attr).count()

    return attr_count


def count_report_cards(counts):
    """
    A type of report where each attribute and its count
    is presented as a card. Used for general observations.
    """
    return dbc.CardDeck(
        [
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H5(label_translations[c[0]], className="card-title"),
                            html.P(f'{c[1]} defectos', className="card-text"),
                        ]
                    ),
                    dbc.CardFooter(
                        dbc.Button(
                            "Más información",
                            id={
                                "type":  "observation_card",
                                "index": c[0]
                            }
                        )
                    )
                ],
                className="mt-3 md-3",
            )
            for c in counts
        ],
    )

def count_report_cards_n(counts):
    """
    A type of report where each attribute and its count
    is presented as a card. Used for general observations.
    """
    return dbc.CardDeck(
        [
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H5(c[0], className="card-title"),
                            html.P(f'{c[1]} defectos', className="card-text"),
                        ]
                    ),
                    dbc.CardFooter(
                        dbc.Button(
                            "Más información",
                            id={
                                "type":  "neighborhood_card",
                                "index": c[0]
                            }
                        )
                    )
                ],
                className="mt-3 md-3",
            )
            for c in counts
        ],
    )


def count_report_sheet(title, counts):
    """
    Type of report where there is a simple parent container that hosts
    attributes and their values
    """

    # Indexing this way makes it agnostic, versus using a given column name
    count_list = counts[counts.columns[0]]
    count_reset = counts.reset_index()
    fig = px.bar(
        count_reset,
        x=count_reset.columns[0], y="label_type",
        labels={'label_type': 'Cantidad de observaciones', 'severity': "Severidad"}
    )

    fig.update_layout(
        font_family="Roboto, sans serif, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji",
        font_color="#242423",
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return dbc.Row(
        [
            dbc.Col(
                [
                    html.H4(label_translations[title]),
                    html.P(label_descriptions[title]),
                    html.Div(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(html.Div(html.Img(src=label_img_paths[title], style={'width':'30em'})))
                                ]
                            ),
                        ],
                        style={'display': 'flex', 'flexDirection': 'row', 'justifyContent' : 'center'}
                    )
                ],
            ),
            dbc.Col(
                dcc.Graph(figure=fig) if len(count_list) != 0 else None
            )
        ],
        className="d-flex"
    )

def count_report_sheet_n(title, counts):
    """
    Type of report where there is a simple parent container that hosts
    attributes and their values
    """

    # Indexing this way makes it agnostic, versus using a given column name
    count_list = counts[counts.columns[0]]
    count_reset = counts.reset_index()
    fig = px.bar(
        count_reset,
        x=count_reset.columns[0], y="neighborhood",
        labels={'neighborhood': 'Cantidad de observaciones', 'severity': "Severidad"}
    )

    fig.update_layout(
        font_family="Roboto, sans serif, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji",
        font_color="#242423",
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )

    return dbc.Row(
        [
            dbc.Col(
                [
                    html.H2(title, className="display-4"),
                ],
            ),
            dbc.Col(
                dcc.Graph(figure=fig) if len(count_list) != 0 else None
            )
        ],
        className="d-flex"
    )


neighborhood_report = count_report_cards_n(
    count_attr_of_col(
        df_points,
        lambda: "neighborhood",
        None
    )
)

observation_types = count_report_cards(
    count_attr_of_col(
        df_points,
        lambda: "label_type",
        None
    )
)

obstacle_component = count_report_sheet(
    "Obstacle",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "Obstacle",
        "severity"
    )
)

no_sidewalk_component = count_report_sheet(
    "NoSidewalk",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "NoSidewalk",
        "severity"
    )
)

surface_problem_component = count_report_sheet(
    "SurfaceProblem",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "SurfaceProblem",
        "severity"
    )
)

no_curbramp_component = count_report_sheet(
    "NoCurbRamp",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "NoCurbRamp",
        "severity"
    )
)

curbramp_component = count_report_sheet(
    "CurbRamp",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "CurbRamp",
        "severity"
    )
)

occlusion_component = count_report_sheet(
    "Occlusion",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "Occlusion",
        "severity"
    )
)

other_component = count_report_sheet(
    "Other",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "Other",
        "severity"
    )
)

component_map = {
    "NoSidewalk": no_sidewalk_component,
    "Obstacle": obstacle_component,
    "SurfaceProblem": surface_problem_component,
    "NoCurbRamp": no_curbramp_component,
    "CurbRamp": curbramp_component,
    "Occlusion": occlusion_component,
    "Other": other_component
}


san_pedro = count_report_sheet_n(
    "San Pedro",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "San Pedro",
        "severity"
    )
)

del_valle = count_report_sheet_n(
    "Del Valle",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "Del Valle",
        "severity"
    )
)

lomas = count_report_sheet_n(
    "Lomas",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "Lomas",
        "severity"
    )
)

valle_poniente = count_report_sheet_n(
    "Valle Poniente",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "Valle Poniente",
        "severity"
    )
)

el_obispo = count_report_sheet_n(
    "El Obispo",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "El Obispo",
        "severity"
    )
)

san_angel = count_report_sheet_n(
    "San Angel",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "San Angel",
        "severity"
    )
)

valle_oriente = count_report_sheet_n(
    "Valle Oriente",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "Valle Oriente",
        "severity"
    )
)

los_callejones = count_report_sheet_n(
    "Los Callejones",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "Los Callejones",
        "severity"
    )
)

san_agustin = count_report_sheet_n(
    "San Agustín",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "San Agustín",
        "severity"
    )
)

industrial = count_report_sheet_n(
    "Industrial",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "Industrial",
        "severity"
    )
)

santa_catarina = count_report_sheet_n(
    "Río Santa Catarina",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.neighborhood == "Rio Santa Catarina",
        "severity"
    )
)

neighborhood_map = {
    "San Pedro": san_pedro,
    "Del Valle": del_valle,
    "Lomas": lomas,
    "Valle Poniente": valle_poniente,
    "El Obispo": el_obispo,
    "San Angel": san_angel,
    "Valle Oriente": valle_oriente,
    "Los Callejones": los_callejones,
    "San Agustín": san_agustin,
    "Industrial": industrial,
    "Rio Santa Catarina": santa_catarina
}

@app.callback(
    Output("count_report", "children"),
    Input({"type": "observation_card", "index": ALL}, "n_clicks"),
    prevent_initial_call=True
)
def select_report(*args):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    id_json = json.loads(button_id)
    return component_map[id_json["index"]]


@app.callback(
    Output("count_report_neighborhood", "children"),
    Input({"type": "neighborhood_card", "index": ALL}, "n_clicks"),
    prevent_initial_call=True
)
def select_report_n(*args):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    id_json = json.loads(button_id)
    return neighborhood_map[id_json["index"]]
