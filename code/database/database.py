import json
import os

RUTA_DATOS = os.path.join(os.path.dirname(__file__), "datos.json")

class Database:
    @staticmethod
    def cargar_datos():
        if not os.path.exists(RUTA_DATOS):
            return {"usuarios": [], "equipos": [], "solicitudes": []}
        
        with open(RUTA_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def guardar_datos(datos):
        with open(RUTA_DATOS, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)