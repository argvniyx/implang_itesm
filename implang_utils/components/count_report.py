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
    "NoSidewalk": "No hay banqueta",
    "Obstacle": "Obstáculo",
    "SurfaceProblem": "Problema de superficie",
    "NoCurbRamp": "Sin Rampa",
    "CurbRamp": "Rampa con imperfectos",
    "Occlusion": "Obstrucción de vista",
    "Other": "Otro"
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
                            html.P(c[1], className="card-text"),
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


def otherImage():
    return html.Div(
        [
        dbc.Row(
                [

                    dbc.Col(html.Div(html.Img(src='../../assets/other.png', style={'height':'100%', 'width':'100%'})), width=10)
                ]
            ),
        ], style={'display': 'flex', 'flexDirection': 'row', 'justifyContent' : 'center'}
    )


def count_report_sheet(title, counts):
    """
    Type of report where there is a simple parent container that hosts
    attributes and their values
    """

    # Indexing this way makes it agnostic, versus using a given column name
    count_list = counts[counts.columns[0]]
    count_reset = counts.reset_index()
    fig = px.bar(count_reset, x=count_reset.columns[0], y="label_type")

    return html.Div(
        [
            html.H1(title),
            dbc.CardDeck(
                [
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H5(c[0], className="card-title"),
                                    html.P(c[1], className="card-text"),
                                ]
                            )
                        ],
                        className="mt-3 md-3"
                    )
                    for c in count_list.iteritems()
                ],
            ),
            dcc.Graph(figure=fig)
        ]
    )


observation_types = count_report_cards(
    count_attr_of_col(
        df_points,
        lambda: "label_type",
        None
    )
)

obstacle_component = count_report_sheet(
    "Obstáculo",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "Obstacle",
        "severity"
    )
)

no_sidewalk_component = count_report_sheet(
    "No hay banqueta",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "NoSidewalk",
        "severity"
    )
)

surface_problem_component = count_report_sheet(
    "Problema de superficie",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "SurfaceProblem",
        "severity"
    )
)

no_curbramp_component = count_report_sheet(
    "Sin Rampa",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "NoCurbRamp",
        "severity"
    )
)

curbramp_component = count_report_sheet(
    "Rampa con imperfectos",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "CurbRamp",
        "severity"
    )
)

occlusion_component = count_report_sheet(
    "Obstrucción de vista",
    count_attr_of_col_df(
        df_points,
        lambda: df_points.label_type == "Occlusion",
        "severity"
    )
)

other_component = count_report_sheet(
    "Otro",
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


@app.callback(
    Output("count_report", "children"),
    Input({"type": "observation_card", "index": ALL}, "n_clicks"),
    prevent_initial_call=True
)
def select_report(n_clicks):
    if n_clicks is None:
        raise PreventUpdate

    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    id_json = json.loads(button_id)
    return component_map[id_json["index"]]
