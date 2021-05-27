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
    return dbc.Jumbotron(
        [
            html.H1(
                "Movilidad Implang",
                className="display-2 d-none d-md-block"
            ),
            html.H1(
                "Movilidad Implang",
                className="d-block d-md-none"
            ),
            html.H2("El estado de las banquetas de San Pedro")
        ],
        className="rounded-0 h-100 m-0",
        style={
            "backgroundImage": "url(../../assets/san-pedro-background.jpg)",
            "backgroundPosition": "center",
            "backgroundSize": "cover",
            "backgroundRepeat": "no-repeat",
        }
    )
