"""
itesm.py:
Trabajo hecho por el equipo de
Visualización de Datos y Narrativa
"""
import dash_bootstrap_components as dbc

from implang_utils.components.header import header
from implang_utils.components.neighborhood_section import neighborhood_section
from implang_utils.components.section import section
from implang_utils.components.curb_evaluation import curb_evaluation
from implang_utils.components.overview_section import overview_section
from implang_utils.components.map_component import map_component
from implang_utils.components.map_component import map_component_denue


sections = [
    neighborhood_section,
    curb_evaluation
]

layout = dbc.Container(
    [
        header(),
        overview_section(),
        *[section(func) for func in sections],
        map_component(),
        map_component_denue()
    ],
    fluid=True
)
