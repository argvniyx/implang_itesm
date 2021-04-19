import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


def section(component_func):
    """
    section: (_ -> [DB Component]) -> DB Component
    component_func: a function that returns a list of components
                    which will most likely represent the caller's
                    body
    """
    return dbc.Card([
        *component_func()
    ], color="light", className="mb-3")
