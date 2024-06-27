import pandas as pd
import geopandas as gpd

# Charger les données des villes
cities_data = pd.read_csv("cities_data.csv")

# Convertir en GeoDataFrame
gdf = gpd.GeoDataFrame(
    cities_data,
    geometry=gpd.points_from_xy(cities_data.longitude, cities_data.latitude),
)

# Charger les données des côtes
coastlines = gpd.read_file(
    "data/coastlines-split-4326/lines.shp"
)  # Source: https://osmdata.openstreetmap.de/data/coastlines.html

# Buffer autour des côtes pour définir "proche de la mer" (e.g., 10 km)
coastlines_buffer = coastlines.buffer(0.1)  # 0.1 degré approximativement égal à 10 km

# Identifier les villes côtières
coastal_cities = gdf.intersects(coastlines_buffer.unary_union)

# Filtrer les villes côtières
coastal_cities_df = cities_data[coastal_cities][["name", "country_code"]]

# Enregistrer les villes côtières dans un fichier CSV
coastal_cities_df.to_csv("coastal_cities.csv", index=False)
