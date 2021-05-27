"""
navigation_button.py:

Encapsulation of the button behaviors
in our sections.
"""
import dash_bootstrap_components as dbc
import dash_html_components as html
from app import app
from dash.dependencies import ClientsideFunction, Input, Output, ALL

# We must use a dummy id and a dummy property
# Because Dash will throw errors on duplicate outputs
app.clientside_callback(
    ClientsideFunction(
        namespace="clientside",
        function_name="scrollSection"
    ),
    Output("scrollSection-callback-target", "n_clicks"),
    Input({'type': ALL, 'direction': ALL}, "n_clicks"),
    prevent_initial_call=True
)


def navigation_button(direction):
    """
    navigation_button: Int -> Row
    """

    return dbc.Button(
        [
            # Cursed Python
            html.I(className="bi bi-chevron-down")
            if direction == "down"
            else
            html.I(className="bi bi-chevron-up"),
            html.Div([], id="scrollSection-callback-target")
        ],
        id={'type': 'navigation-button', 'direction': direction},
        className='rounded-0',
        block=True,
        color="dark"
    )
