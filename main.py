from fastapi import FastAPI
import json

app = FastAPI()

@app.post("/guardar-json/")
async def guardar_json(data: dict):
    with open("archivo.json", "w") as f:
        json.dump(data, f)
    return {"mensaje": "JSON guardado correctamente"}
