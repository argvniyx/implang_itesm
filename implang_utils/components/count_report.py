"""
count_report.py:
A component that gives statistical information
on a list of counts
"""
import dash
import json
import dash_html_components as html
import dash_bootstrap_components as dbc
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
                            html.P("Más información"),
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


def count_report_sheet(title, counts):
    """
    Type of report where there is a simple parent container that hosts
    attributes and their values
    """
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
                                    html.P(c[1], className="card-text")
                                ]
                            )
                        ],
                        className="mt-3 md-3"
                    )
                    for c in counts
                ],
            )
        ]
    )


def count_report_builder(title, counts, component_type):
    """
    Given a list of pairs, counts, and a component, build
    a little report of the counts provided
    """
    if component_type == "cards":
        return count_report_cards(counts)

    return count_report_sheet(title, counts)


observation_types = count_report_builder(
    "Observaciones",
    count_attr_of_col(
        df_points,
        lambda: "label_type",
        None
    ),
    "cards"
)

obstacle_component = count_report_builder(
    "Obstacle",
    count_attr_of_col(
        df_points,
        lambda: df_points.label_type == "Obstacle",
        "severity"),
    "sheet"
)

no_sidewalk_component = count_report_builder(
    "NoSidewalk",
    count_attr_of_col(
        df_points,
        lambda: df_points.label_type == "NoSidewalk",
        "severity"),
    "sheet"
)

surface_problem_component = count_report_builder(
    "SurfaceProblem",
    count_attr_of_col(
        df_points,
        lambda: df_points.label_type == "SurfaceProblem",
        "severity"),
    "sheet"
)

no_curbramp_component = count_report_builder(
    "NoCurbRamp",
    count_attr_of_col(
        df_points,
        lambda: df_points.label_type == "NoCurbRamp",
        "severity"),
    "sheet"
)

curbramp_component = count_report_builder(
    "CurbRamp",
    count_attr_of_col(
        df_points,
        lambda: df_points.label_type == "CurbRamp",
        "severity"),
    "sheet"
)

occlusion_component = count_report_builder(
    "Occlusion",
    count_attr_of_col(
        df_points,
        lambda: df_points.label_type == "Occlusion",
        "severity"),
    "sheet"
)

other_component = count_report_builder(
    "Other",
    count_attr_of_col(
        df_points,
        lambda: df_points.label_type == "Other",
        "severity"),
    "sheet"
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