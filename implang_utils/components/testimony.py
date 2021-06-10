import dash_bootstrap_components as dbc
import dash_html_components as html
from implang_utils.components.utils import highlight

def testimonial():
    "Setup to the overview reports component/slide"
    return dbc.Row(
        [
            dbc.Col(
                [
                    html.H1("Testimonio"),
                    html.H4(
                    [
                        "Debido a la inaccesibilidad generalizada, las personas con discapacidad tienen dificultad para realizar actividades cotidianas en las calles de la ciudad, y por ello se ven invisibilizados al no poder desplazarse con facilidad.",
                    ],
                        className="m-3 px-3"
                    ),
                    html.H4(
                        "“Es importante que existan rampas junto a las escales en todos los lugares, así como rampas y elevadores en lugares que lo requieran. Poner banquetas a nivel de suelo para las personas con discapacidad sería lo ideal para un transito peatonal accesible.” – Alberto Garza",
                        className="m-3 px-3"
                    )
                ],
                width=7,
                className="d-flex flex-column align-items-center justify-content-center"
            ),

            dbc.Col(
                [],
                style={
                    "backgroundImage": "url(../../assets/beto.png)",
                    "backgroundPosition": "center",
                    "backgroundSize": "cover",
                    "backgroundRepeat": "no-repeat",
                },
                width=5
            )
        ],
        className="h-100 m-0 text-justify"
    )