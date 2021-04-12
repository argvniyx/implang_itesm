import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


# TODO:
# Possibly have a style dict that maps to each specific
# component? i.e. { hr: {...}, jumbo: {...} }

def header():
    "Header produces a Jumbotron"
    return dbc.Jumbotron(
        [
            html.H1("Banquetas en San Pedro"),
            html.P("Una breve introducción por aquí")
        ],
        style={
            "borderRadius": 0
        }
    )
