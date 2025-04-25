from fastapi import FastAPI
import osmnx as ox
from functools import lru_cache

app = FastAPI(title="API de Manresa", 
              description="Datos de carreteras, edificios y puntos de interés en Manresa")

# Cacheamos los datos para no sobrecargar OSM
@lru_cache(maxsize=1)
def get_roads():
    return ox.graph_from_place("Manresa, Spain", network_type="drive")

@app.get("/")
def home():
    return {"message": "API de Manresa. Usa /carreteras"}

@app.get("/carreteras")
def get_carreteras():
    try:
        roads = get_roads()
        nodes, edges = ox.graph_to_gdfs(roads)
        return {"carreteras": edges[["name", "length", "geometry"]].to_dict()}
    except Exception as e:
        return {"error": str(e)}