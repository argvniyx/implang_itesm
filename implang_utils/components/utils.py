"""
utils.py:
A couple of wrappers and other nice to haves
"""
import dash_html_components as html
import dash_core_components as dcc

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
def get_title(data):
    titulos = {
        "*"    : ["No hay datos selecionados", 26],
        "PTS" : ["Porcentaje de calificación promedio de banquetas", 24],
        "PR"  : ["Porcentaje de personas de alto riesgo por manzana", 24],
        "EST" : ["Número de establecimientos de alta importancia por manzana", 22],
        "PTS+PR" : ["Calificación de banquetas tomando datos de personas de riesgo", 22],
        "PTS+EST" : ["Calificación de banquetas tomando datos de establecimientos", 22],
        "PTS+PR+EST": ["Calificación de banquetas tomando datos de personas de riesgo y establecimientos", 20]
    }
    if len(data) == 0:
        return titulos['*']
    elif len(data) == 3:
        return titulos['PTS+PR+EST']
    elif len(data) == 1:
        if data[0] == "Score_PTS":
            return titulos['PTS']
        elif data[0] == "Score_PR":
            return titulos['PR']
        elif data[0] == "Score_EST":
            return titulos['EST']
    elif len(data) == 2:
            if data[0] == "Score_PTS":
                if data[1] == "Score_PR":
                    return titulos['PTS+PR']
                elif data[1] == "Score_EST":
                    return titulos['PTS+EST']
    else:
        return ""
