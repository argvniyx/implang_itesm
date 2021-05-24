"""
utils.py:
A couple of wrappers and other nice to haves
"""
import dash_html_components as html


def highlight(component, color="yellow"):
    """
    Highlight: Dash Component -> Dash Component
    Takes a Dash component and returns it styled
    with a color background, which defaults to
    yellow.
    """
    return html.Span(
        component,
        style={"background": f'var(--{color})'}
    )
