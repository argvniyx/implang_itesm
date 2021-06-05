"""
navigation_button.py:

Encapsulation of the button behaviors
in our sections.
"""
import dash_html_components as html


def navigation_button(direction, section_number):
    """
    navigation_button: Int -> Row
    """
    prev_a = 0 if section_number == 0 else section_number - 1
    next_a = section_number + 1

    return html.A(
        [
            # Cursed Python
            html.I(className="bi bi-chevron-down")
            if direction == "down"
            else
            html.I(className="bi bi-chevron-up"),
            html.Div([], id="scrollSection-callback-target")
        ],
        id=f'section-{section_number}-{direction}',
        href=f'#section-{prev_a}-up' if direction == "up" else f'#section-{next_a}-up',
        className="btn btn-dark btn-block rounded-0"
    )
