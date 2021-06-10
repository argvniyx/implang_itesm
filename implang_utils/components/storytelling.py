
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc

def story():
    return html.Div(
        [
            dbc.Row(
            [
                dbc.Col(html.Div(html.Img(src='../../assets/accesibilidad.png', style={'height':'91vh', 'width':'37vw', 'marginLeft': '0vw'})), width=5),
                dbc.Col(
                [
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H1(html.B("Una ciudad para todos")),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H2("En Nuevo Leon el 3.8 por ciento de la población padece de alguna condición que limita su autonomía motriz."),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H2("Por una ciudad más accesible, es necesario identificar las zonas donde es prioridad brindar un espacio adecuado para todos los ciudadanos.")
                ], width=7)
            ])
        ]
    )

def whatsHappening():
    return html.Div(
        [
            dbc.Row(
            [
                dbc.Col(
                [
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H1(html.B("Una ciudad para todos"), style={'marginLeft' : '1vw'}),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H2("Se han registrado 93,648 de defectos en las banquetas y calles de San Pedro Garza García", style={'marginLeft' : '1vw'}),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.H2("Esto representa un obstáculo para proporcionar acceso a la ciudad para todos y afecta la autonomía de las personas que poseen distintas condiciones", style={'marginLeft' : '1vw'})
                ],width=7),
                dbc.Col(html.Img(src='../../assets/anciano.png', style={'height':'90vh', 'width':'37vw', 'marginLeft' : '3.4vw'}), width=5),
            ])
        ]
    )
