import sys
import os
from datetime import datetime, timedelta
import logging

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from database.database import Database
from models.equipo import Equipo
from models.solicitud import SolicitudPrestamo
from services.prestamo_service import PrestamoService

def mostrar_opciones():
    print("\n--- MENÚ SOLICITANTE ---")
    print("1. Consultar catálogo de equipos")
    print("2. Crear solicitud de préstamo")
    print("3. Consultar mis préstamos (Vigentes/Atrasados)")
    print("4. Cancelar una solicitud")
    print("5. Cerrar sesión")

def consultar_catalogo():
    print("\n--- CATÁLOGO DE EQUIPOS ---")
    try:
        datos = Database.cargar_datos()
        equipos = datos.get("equipos", [])
        if not equipos:
            print("No hay equipos registrados.")
            return
        print(f"{'ID':<5} | {'NOMBRE':<20} | {'ESTADO':<15}")
        print("-" * 45)
        for eq in equipos:
            print(f"{eq['id']:<5} | {eq['nombre']:<20} | {eq['estado']:<15}")
    except Exception as e:
        print(f"Error crítico al leer el catálogo: {e}")

def solicitud_prestamo(usuario_actual):
    print("\n--- CREAR SOLICITUD DE PRÉSTAMO ---")
    try:
        print("Nota: El préstamo se generará automáticamente por un plazo de 7 días.")
        print("(Si no conoce los IDs, revise la opción '1. Consultar catálogo').\n")
        
        ids_input = input("Ingrese los IDs separados por coma (ej: 1, 2): ")
        ids_solicitados = [int(i.strip()) for i in ids_input.split(",") if i.strip().isdigit()]
        
        if not ids_solicitados:
            print("Error: No ingresó IDs válidos.")
            return
            
        datos = Database.cargar_datos()
        equipos_json = datos.get("equipos", [])
        equipos_objetos = [Equipo(id=eq["id"], nombre=eq["nombre"], estado=eq["estado"]) 
                           for eq in equipos_json if eq["id"] in ids_solicitados]
        
        if len(equipos_objetos) != len(ids_solicitados):
            print("Error: Algunos IDs no existen en el catálogo.")
            return

        solicitudes_json = datos.get("solicitudes", [])
        prestamos_activos = []
        for sol_json in solicitudes_json:
            fecha_inicio_obj = datetime.strptime(sol_json["fecha_inicio"], "%Y-%m-%d").date()
            fecha_dev_obj = datetime.strptime(sol_json["fecha_devolucion"], "%Y-%m-%d").date()
            
            from models.usuario import Usuario
            usr_mock = Usuario(id=sol_json["usuario_id"], nombre="", correo="", password="", rol="")
            sol_obj = SolicitudPrestamo(sol_json["id"], usr_mock, [], fecha_inicio_obj, fecha_dev_obj)
            sol_obj.estado = sol_json["estado"]
            prestamos_activos.append(sol_obj)

        fecha_inicio = datetime.now().date()
        fecha_devolucion = fecha_inicio + timedelta(days=7)
        
        service = PrestamoService()
        solicitud_creada, mensaje = service.crear_solicitud(
            id_solicitud=len(solicitudes_json) + 1,
            usuario=usuario_actual,
            equipos=equipos_objetos,
            fecha_inicio=fecha_inicio,
            fecha_devolucion=fecha_devolucion,
            prestamos_activos=prestamos_activos,
            clase_solicitud=SolicitudPrestamo
        )

        if solicitud_creada:
            datos["solicitudes"].append({
                "id": solicitud_creada.id,
                "usuario_id": usuario_actual.id,
                "equipos_ids": [eq.id for eq in solicitud_creada.equipos],
                "fecha_inicio": solicitud_creada.fecha_inicio.strftime("%Y-%m-%d"),
                "fecha_devolucion": solicitud_creada.fecha_devolucion.strftime("%Y-%m-%d"),
                "estado": solicitud_creada.estado
            })
            Database.guardar_datos(datos)
            print(f"\n¡Éxito! {mensaje} (ID: {solicitud_creada.id})")
            logging.info(f"Solicitud {solicitud_creada.id} creada por {usuario_actual.id}.")
        else:
            print(f"\nOperación rechazada: {mensaje}")
            logging.warning(f"Solicitud rechazada ({usuario_actual.id}): {mensaje}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mis_prestamos(usuario_actual):
    print("\n--- MIS PRÉSTAMOS ---")
    try:
        datos = Database.cargar_datos()
        mis_solicitudes = [s for s in datos.get("solicitudes", []) if s["usuario_id"] == usuario_actual.id]
        
        if not mis_solicitudes:
            print("No tiene préstamos registrados.")
            return
            
        print(f"{'ID':<5} | {'EQUIPOS':<20} | {'INICIO':<12} | {'DEVOLUCIÓN':<12} | {'ESTADO':<10}")
        print("-" * 70)
        for sol in mis_solicitudes:
            equipos_str = ", ".join(str(e) for e in sol["equipos_ids"])
            print(f"{sol['id']:<5} | {equipos_str:<20} | {sol['fecha_inicio']:<12} | {sol['fecha_devolucion']:<12} | {sol['estado']:<10}")
    except Exception as e:
        print(f"Error: {e}")

def cancelar_solicitud(usuario_actual):
    print("\n--- CANCELAR SOLICITUD ---")
    try:
        datos = Database.cargar_datos()
        solicitudes = datos.get("solicitudes", [])
        cancelables = [s for s in solicitudes if s["usuario_id"] == usuario_actual.id and s["estado"] in ["SOLICITADA", "APROBADA"]]
        
        if not cancelables:
            print("No tiene solicitudes pendientes que pueda cancelar.")
            return
            
        print(f"{'ID':<5} | {'ESTADO':<10} | {'DEVOLUCIÓN':<12}")
        print("-" * 35)
        for sol in cancelables:
            print(f"{sol['id']:<5} | {sol['estado']:<10} | {sol['fecha_devolucion']:<12}")
            
        id_input = input("\nIngrese el ID de la solicitud a cancelar: ").strip()
        if not id_input.isdigit():
            print("Error: Ingrese un ID numérico válido.")
            return
            
        id_cancelar = int(id_input)
        solicitud_json = next((s for s in solicitudes if s["id"] == id_cancelar and s["usuario_id"] == usuario_actual.id), None)
        
        if not solicitud_json:
            print("Error: No se encontró la solicitud.")
            return
            
        from models.usuario import Usuario
        usr_mock = Usuario(id=usuario_actual.id, nombre="", correo="", password="", rol="")
        sol_obj = SolicitudPrestamo(solicitud_json["id"], usr_mock, [], datetime.now().date(), datetime.now().date())
        sol_obj.estado = solicitud_json["estado"]
        
        service = PrestamoService()
        resultado, mensaje = service.cancelar_solicitud(sol_obj)
        
        if resultado:
            solicitud_json["estado"] = sol_obj.estado
            Database.guardar_datos(datos)
            print(f"\n¡Éxito! {mensaje}")
        else:
            print(f"\nOperación rechazada: {mensaje}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def iniciar_menu(usuario_actual):
    while True:
        mostrar_opciones()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            consultar_catalogo()
        elif opcion == "2":
            solicitud_prestamo(usuario_actual)
        elif opcion == "3":
            mis_prestamos(usuario_actual)
        elif opcion == "4":
            cancelar_solicitud(usuario_actual)
        elif opcion == "5":
            print("Cerrando sesión de Solicitante...")
            logging.info(f"Cierre de sesión: {usuario_actual.id}")
            break # Rompe el ciclo y devuelve el control a main.py
        else:
            print("Opción inválida. Intente nuevamente.")