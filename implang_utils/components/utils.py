import dash_html_components as html
import dash_bootstrap_components as dbc


def highlight(component, color="yellow"):
    return html.Span(
        component,
        style={ "background": f'var(--{color})' }
    )
