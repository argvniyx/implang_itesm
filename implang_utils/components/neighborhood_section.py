import pandas as pd
import geopandas as gpd
import dash_bootstrap_components as dbc
import dash_html_components as html

# Computing the values
df = gpd.read_file("implang_utils/data/banquetas_puntos.geojson")

neighborhoods = df["properties/neighborhood"].value_counts()


# Generating the Components
def tab_content(title):
    "Create a DBC Tab with a structure"
    return dbc.Card(
        dbc.CardBody([
            html.H3(title),
            html.P(["Total de imperfectos: ", neighborhoods[title]])
        ])
        , className="mt-3")


def neighborhood_section():
    "Function that returns a Card Body with neighborhood stats"
    return [
        dbc.CardHeader(html.H2("Las colonias")),
        dbc.CardBody([
            dbc.Tabs([dbc.Tab(tab_content(t), label=t)
                      for t in neighborhoods.keys()])
        ])
    ]
