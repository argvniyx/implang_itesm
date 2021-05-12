"""
navigation_button.py:

Encapsulation of the button behaviors
in our sections.
"""
import dash_bootstrap_components as dbc
from app import app
from dash.dependencies import ClientsideFunction, Input, Output, ALL

# We must use a dummy id and a dummy property
# (i.e. itesm-container, in the itesm.py layout)
# Because Dash will throw errors on duplicate outputs
app.clientside_callback(
    ClientsideFunction(
        namespace="clientside",
        function_name="scrollSection"
    ),
    Output("itesm-container", "n_clicks"),
    Input({'type': ALL, 'direction': ALL}, "n_clicks"),
    prevent_initial_call=True
)


def navigation_button(direction):
    """
    navigation_button: Int -> Row
    """

    return dbc.Row(
        dbc.Button(
            [
                "Siguiente" if direction == "down" else "Atrás"
            ],
            id={'type': 'navigation-button', 'direction': direction},
            className=f'rounded-0 {direction}',
            block=True,
        ),
    )
