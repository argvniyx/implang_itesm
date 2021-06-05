"""
section.py:
This component is meant to
abstract common styling
conventions such as using 100vh
"""
import dash_bootstrap_components as dbc
from implang_utils.components.navigation_button import navigation_button


def section(component_func, section_number):
    """
    section: (_ -> [DB Component]) -> DB Component
    component_func: a function that returns a list of components
                    which will most likely represent the caller's
                    body
    """

    return dbc.Row(
        [
            navigation_button("up", section_number),
            dbc.Col(
                component_func(),
                className="flex-grow-1 p-0",
                style={"overflowY": "auto"}
            ),
            navigation_button("down", section_number),
        ],
        className="page-section flex-column"
    )
