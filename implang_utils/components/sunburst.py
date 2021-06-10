import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from implang_utils.components.utils import highlight
def sun():
    return dbc.Row(
        [
            dbc.Col(
            [
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                graph()
            ], width=5),
            dbc.Col(
                [
                    html.H1(
                        "Una ciudad para todos",
                        className="display-3 m-5"
                    ),
                    html.H4(
                        [
                            "En San Pedro Garza García, ",
                            highlight("46,200 personas"),
                            " clasifican como población vulnerable, esto representa el 35 por ciento de la población total."
                        ],
                        className="m-3 px-3"
                    ),
                    html.H4(
                        [
                            "En este grupo se encuentran personas con discapacidad, con limitación en la actividad cotidiana o personas mayores de 65 años."
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

def graph():
    fig =go.Figure(go.Sunburst(
        labels=["Población Vulnerable", "3era Edad", "Discapacidad o Limitación", "Condición Mental", "Visual o Auditiva", "Hablar o Comunicarse", "Motriz", "Recordar o concentrarse", "Condición mental", "Ver, aún usando lentes", "Oír, aún usando aparatos", "Caminar, subir o bajar", "Bañarse, vestirse o comer"],
        parents=["","Población Vulnerable",  "Población Vulnerable",  "Población Vulnerable",  "Población Vulnerable",  "Población Vulnerable",  "Población Vulnerable", "Condición Mental", "Condición Mental", "Visual o Auditiva",  "Visual o Auditiva", "Motriz", "Motriz" ],
        values=[46200, 17600, 12568, 2466, 8140,485,4941,982, 1484, 6311, 1829, 4147, 794],
        textinfo='label+percent entry'
    ))
    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0), height=700)

    return dcc.Graph(figure=fig)