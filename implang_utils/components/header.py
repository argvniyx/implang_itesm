"""
header.py:
Componente con la primera seccion de
la página. Funge como un call to action,
da una breve reseña, etc.
"""
import dash_bootstrap_components as dbc
import dash_html_components as html


def header():
    "Header produces a Jumbotron"
    return dbc.Col(
        dbc.Jumbotron(
            [
                html.H1("Movilidad Implang"),
                html.H2("El estado de las banquetas de San Pedro")
            ],
            className="h-100 rounded-0"
        )
    )
