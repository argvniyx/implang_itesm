"""
itesm.py:
Trabajo hecho por el equipo de
Visualización de Datos y Narrativa
"""

from implang_utils.components.header import header
from implang_utils.components.neighborhood_section import neighborhood_section
from implang_utils.components.section import section
from implang_utils.components.overview_section import overview_section
from implang_utils.components.map_component import map_component
from implang_utils.components.map_component import map_component_denue
from implang_utils.components.map_component import map_component_inegi
from implang_utils.components.map_component import map_component_go

sections = [
    header,
    overview_section,
    neighborhood_section,
    # evaluate if we need this 3 maps map_component_inegi, map_component, map_component_denue
    map_component_inegi,
    map_component,
    map_component_denue,
    map_component_go,
    lambda: map_component_go(['Score_PTS']),
    lambda: map_component_go(['Score_PTS', 'Score_EST']),
    lambda: map_component_go(['Score_PTS', 'Score_PR']),
    lambda: map_component_go(['Score_PTS', 'Score_EST', 'Score_PR'])
]

# A pages layout is simply a list of Rows
layout = [
    section(func, i)
    for i, func in enumerate(sections)
]
