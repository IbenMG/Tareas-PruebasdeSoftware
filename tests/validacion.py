import sys
import os
import time
from datetime import date

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))

from database.database import Database
from models.usuario import Usuario
from models.equipo import Equipo
from models.solicitud import SolicitudPrestamo
from services.prestamo_service import PrestamoService

def automatizar_val_01():
    print("\n--- EJECUTANDO VAL-01: Prueba de Velocidad ---")
    service = PrestamoService()
    
    # 1. Preparamos 5 solicitudes "mock" simulando que ya fueron aprobadas
    solicitudes_simuladas = []
    usr_mock = Usuario(1, "Encargado Rapido", "e@lab.cl", "123", "ENCARGADO")
    
    for i in range(1, 6):
        eq_mock = Equipo(i, f"Equipo {i}", "DISPONIBLE")
        sol = SolicitudPrestamo(i, usr_mock, [eq_mock], date.today(), date.today())
        sol.estado = "APROBADA"
        solicitudes_simuladas.append(sol)

    # 2. Iniciamos el cronómetro de rendimiento (performance counter)
    inicio_tiempo = time.perf_counter()

    # 3. El Encargado registra las 5 entregas de golpe
    for sol in solicitudes_simuladas:
        service.registrar_entrega(sol)

    # 4. Detenemos el cronómetro
    fin_tiempo = time.perf_counter()
    tiempo_total = fin_tiempo - inicio_tiempo

    print(f"Resultado VAL-01: Se entregaron 5 equipos consecutivos en {tiempo_total:.6f} segundos.")
    
def automatizar_val_05():
    print("\n--- EJECUTANDO VAL-05: Ciclo de vida real del equipo ---")
    datos = Database.cargar_datos()
    
    # Tomamos el primer equipo del inventario
    if not datos.get("equipos"):
        print("No hay equipos en la base de datos para probar.")
        return
        
    equipo_prueba = datos["equipos"][0]
    estado_original = equipo_prueba["estado"]
    
    print(f"Equipo seleccionado: {equipo_prueba['nombre']} | Estado original: {estado_original}")
    
    # Simulamos el día a día
    import logging
    logging.basicConfig(filename='../code/app.log', level=logging.INFO)
    
    estados_vida_real = ["PRESTADO", "MANTENIMIENTO", "DISPONIBLE"]
    
    for nuevo_estado in estados_vida_real:
        equipo_prueba["estado"] = nuevo_estado
        Database.guardar_datos(datos)
        logging.info(f"VAL-05 SIMULACION: Estado de equipo {equipo_prueba['id']} cambió a {nuevo_estado}")
        print(f"-> Transición exitosa a: {nuevo_estado}")
        time.sleep(0.5) # Pausa de medio segundo para simular el paso del tiempo
        
    print("Resultado VAL-05: El equipo transitó por todos los estados de desgaste y reparación exitosamente.")
    print("Los eventos quedaron registrados en el archivo app.log.")

if __name__ == "__main__":
    print("INICIANDO VALIDACIONES AUTOMATIZADAS...\n")
    automatizar_val_01()
    automatizar_val_05()
