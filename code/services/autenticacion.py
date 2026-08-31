import sys
import os
import logging # <-- Importamos logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.database import Database
from models.usuario import Usuario

# Configuramos el archivo donde se guardarán los logs
logging.basicConfig(
    filename='app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class AutenticacionService:
    def iniciar_sesion(self, correo, password):
        datos = Database.cargar_datos()
        
        for u_data in datos.get("usuarios", []):
            if u_data["correo"] == correo:
                # Validación crítica: contraseña correcta
                if u_data["password"] == password:
                    usuario = Usuario(
                        id=u_data["id"], nombre=u_data["nombre"],
                        correo=u_data["correo"], password=u_data["password"], rol=u_data["rol"]
                    )
                    logging.info(f"Inicio de sesión exitoso: {correo} ({usuario.rol})")
                    return usuario, "Inicio de sesión exitoso."
                else:
                    logging.warning(f"Intento fallido (Clave incorrecta): {correo}")
                    return None, "Error: Contraseña incorrecta."
        
        logging.warning(f"Intento fallido (Usuario no existe): {correo}")
        return None, "Error: El correo no está registrado."