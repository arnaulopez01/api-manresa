from fastapi import FastAPI
import json

app = FastAPI()

# Carga los datos desde el archivo
with open("manresa_roads.json") as f:
    roads_data = json.load(f)

@app.get("/carreteras")
def get_carreteras():
    return roads_data