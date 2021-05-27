"""
itesm.py:
Trabajo hecho por el equipo de
Visualización de Datos y Narrativa
"""
import dash_bootstrap_components as dbc
from implang_utils.components.header import header
from implang_utils.components.neighborhood_section import neighborhood_section
from implang_utils.components.section import section
from implang_utils.components.overview_section import overview_section
from implang_utils.components.map_component import map_component_go




sections = [
    header,
    overview_section,
    neighborhood_section,
    map_component_go,
    lambda: map_component_go(['Score_PTS']),
    lambda: map_component_go(['Score_PTS','Score_EST']),
    lambda: map_component_go(['Score_PTS','Score_PR']),
    lambda: map_component_go(['Score_PTS','Score_EST','Score_PR']),

]
# A pages layout is simply a list of Rows
layout = [
    section(func)
    for func in sections
]
