"""
itesm.py:
Trabajo hecho por el equipo de
Visualización de Datos y Narrativa
"""
from implang_utils.components.header import header
from implang_utils.components.neighborhood_section import neighborhood_section
from implang_utils.components.section import section
from implang_utils.components.overview_section import overview_section
from implang_utils.components.map_component import map_component_go
from implang_utils.components.storytelling import story, whatsHappening

sections = [
    header,
    story,
    whatsHappening,
    overview_section,
    neighborhood_section,
    lambda: map_component_go(['Score_PTS']),
]

# A pages layout is simply a list of Rows
layout = [
    section(func, i)
    for i, func in enumerate(sections)
]
