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


sections = [
    header,
    overview_section,
    neighborhood_section,
    map_component_inegi,
    map_component,
    map_component_denue
]

# A pages layout is simply a list of Rows
layout = [
    section(func)
    for func in sections
]
