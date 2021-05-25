import dash_html_components as html
import dash_bootstrap_components as dbc


def highlight(component, color="yellow"):
    return html.Span(
        component,
        style={ "background": f'var(--{color})' }
    )

def graph_color_scale():
    return [(0.0, 'rgba(102, 153, 204, 0.9)'), 
            (0.199, 'rgba(102, 153, 204, 0.9)'), 
            (0.2, 'rgba(245, 203, 92, 0.9)'), 
            (0.399, 'rgba(245, 203, 92, 0.9)'), 
            (0.4, 'rgba(255, 140, 66, 0.9)'), 
            (0.599, 'rgba(255, 140, 66, 0.9)'), 
            (0.6, 'rgba(255, 60, 56, 0.9)'), 
            (0.799, 'rgba(255, 60, 56, 0.9)'), 
            (0.8, 'rgba(162, 62, 72, 0.9)'), 
            (1, 'rgba(162, 62, 72, 0.9)')]

def get_z(df, data):
    if len(data) == 3:
        return round(df[data[0]] * 0.70 + 
                     df[data[1]] * 0.15 + 
                     df[data[2]] * 0.15)
    elif len(data) == 2:
        return round(df[data[0]] * 0.70 + 
                     df[data[1]] * 0.30)
    elif len(data) == 1:
         return df[data[0]]
    else:
        return df['Score_PTS']
