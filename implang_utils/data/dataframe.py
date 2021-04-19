"""
dataframe.py:
Archivo que contiene las manipulaciones
más comunes de la información y que
expone el estado para un mismo punto de
acceso
"""
import geopandas as gpd


# Manipulación de puntos
df_points = gpd.read_file("implang_utils/data/puntos.geojson")

# Manipulación de banquetas
df_curbs = gpd.read_file("implang_utils/data/lineas.geojson")
