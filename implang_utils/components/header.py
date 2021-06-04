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
                "Movilidad IMPLANG",
                className="display-2 d-none d-md-block",
                style={"text-align" : "center"}
            ),
            html.H1(
                "Movilidad IMPLANG",
                className="d-block d-md-none"
            ),
            html.Div([
                html.H2("El estado de las banquetas de San Pedro Garza García, Monterrey"),
                html.H3("Según el INEGI en Nuevo León existen 220 mil 206 personas con discapacidad lo que representa al 3.80 por ciento de la población"),
                html.H3("Es decir, 38 personas de cada mil sufren una discapacidad")            
            ], style={"text-align" : "center"})
        ],
        className="rounded-0 h-100 m-0",
        style={
            "backgroundImage": "url(../../assets/san-pedro-background.jpg)",
            "backgroundPosition": "center",
            "backgroundSize": "cover",
            "backgroundRepeat": "no-repeat",
            "display": "flex",
            "flex-flow": "column",
            "justify-content": "center"
        }
    )
