"""
storytelling.py:
Components that hold some narrative sections
"""
import dash_bootstrap_components as dbc
import dash_html_components as html
from implang_utils.components.utils import highlight

def story():
    "A simple component that gives an introduction to the topic"
    return dbc.Row(
        [
            dbc.Col(
                [],
                style={
                    "backgroundImage": "url(../../assets/accesibilidad.png)",
                    "backgroundPosition": "center",
                    "backgroundSize": "cover",
                    "backgroundRepeat": "no-repeat",
                },
                width=5
            ),
            dbc.Col(
                [
                    html.H1(
                        "Una ciudad para todos",
                        className="display-3 m-5"
                    ),
                    html.H4(
                        [
                            "En Nuevo Leon el ",
                            highlight("3.8 por ciento de la población"),
                            " padece de alguna condición que limita su autonomía motriz."
                        ],
                        className="m-3 px-3"
                    ),
                    html.H4(
                        [
                            "Por una ciudad más accesible, es necesario identificar las zonas donde es prioridad brindar un espacio adecuado para todos los ciudadanos."
                        ],
                        className="m-3 px-3"
                    )
                ],
                width=7,
                className="d-flex flex-column align-items-center justify-content-center"
            )
        ],
        className="h-100 m-0 text-justify"
    )


def whatsHappening():
    "Setup to the overview reports component/slide"
    return dbc.Row(
        [
            dbc.Col(
                [
                    html.H1(
                        "...y todos por la ciudad",
                        className="display-3 m-5"
                    ),
                    html.H4(
                        "Se han registrado 93,648 de defectos en las banquetas y calles de San Pedro Garza García.",
                        className="m-3 px-3"
                    ),
                    html.H4(
                        "Esto representa un obstáculo para proporcionar acceso a la ciudad para todos y afecta la autonomía de las personas que poseen distintas condiciones.",
                        className="m-3 px-3"
                    )
                ],
                width=7,
                className="d-flex flex-column align-items-center justify-content-center"
            ),

            dbc.Col(
                [],
                style={
                    "backgroundImage": "url(../../assets/anciano.png)",
                    "backgroundPosition": "center",
                    "backgroundSize": "cover",
                    "backgroundRepeat": "no-repeat",
                },
                width=5
            )
        ],
        className="h-100 m-0 text-justify"
    )
