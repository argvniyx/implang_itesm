"""
dataframe.py:
Archivo que contiene las manipulaciones
más comunes de la información y que
expone el estado para un mismo punto de
acceso
"""
import geopandas as gpd
import json

# Manipulación de puntos
df_points = gpd.read_file("implang_utils/data/puntos.geojson")

# Manipulación de banquetas
df_curbs = gpd.read_file("implang_utils/data/lineas.geojson")

# Manipulación de datos del DENUE costumizada
df_denue_filtered = gpd.read_file("implang_utils/data/filtered_denue.geojson")

# Manipulación de datos del INEGI
df_inegi = gpd.read_file("implang_utils/data/inegi.geojson")

# Manipulación de datos ya con calificaciones
df_scores = gpd.read_file("implang_utils/data/scored_data.geojson")

op = open("implang_utils/data/scored_data.geojson")
json_scores = json.load(op)
