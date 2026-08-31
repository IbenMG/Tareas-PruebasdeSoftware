import sys
import os
import logging
from datetime import datetime

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from database.database import Database
from models.equipo import Equipo
from models.solicitud import SolicitudPrestamo
from models.usuario import Usuario
from services.prestamo_service import PrestamoService

def mostrar_opciones():
    print("\n--- MENÚ ENCARGADO ---")
    print("1. Administrar usuarios")
    print("2. Administrar inventario")
    print("3. Aprobar o rechazar solicitudes")
    print("4. Registrar entrega de equipos")
    print("5. Registrar devolución de equipos")
    print("6. Cerrar sesión")

def administrar_usuarios(usuario_actual):
    print("\n--- ADMINISTRAR USUARIOS ---")
    print("1. Listar usuarios registrados")
    print("2. Registrar nuevo usuario")
    print("3. Volver")
    
    opcion = input("Seleccione una opción: ").strip()
    try:
        datos = Database.cargar_datos()
        
        if opcion == "1":
            print(f"\n{'ID':<5} | {'NOMBRE':<20} | {'CORREO':<25} | {'ROL':<15}")
            print("-" * 70)
            for u in datos.get("usuarios", []):
                print(f"{u['id']:<5} | {u['nombre']:<20} | {u['correo']:<25} | {u['rol']:<15}")
                
        elif opcion == "2":
            print("\n-- Registro de Usuario --")
            nombre = input("Nombre completo: ").strip()
            correo = input("Correo electrónico: ").strip()
            password = input("Contraseña: ").strip()
            print("Roles: 1. SOLICITANTE | 2. ENCARGADO")
            rol_opcion = input("Seleccione el rol (1 o 2): ").strip()
            
            if not nombre or not correo or not password or rol_opcion not in ["1", "2"]:
                print("Error: Todos los campos son obligatorios y el rol debe ser válido.")
                return
                
            # Validar que el correo no exista
            if any(u["correo"] == correo for u in datos.get("usuarios", [])):
                print("Error: Ya existe un usuario con ese correo.")
                return
                
            rol = "ENCARGADO" if rol_opcion == "2" else "SOLICITANTE"
            nuevo_id = max([u["id"] for u in datos.get("usuarios", [])] + [0]) + 1
            
            nuevo_usuario = {
                "id": nuevo_id,
                "nombre": nombre,
                "correo": correo,
                "password": password,
                "rol": rol
            }
            
            datos["usuarios"].append(nuevo_usuario)
            Database.guardar_datos(datos)
            print(f"\n¡Éxito! Usuario {nombre} registrado con el ID {nuevo_id}.")
            logging.info(f"Usuario {nuevo_id} ({rol}) creado por Encargado {usuario_actual.id}")
            
        elif opcion == "3":
            return
        else:
            print("Opción inválida.")
            
    except Exception as e:
        print(f"Error inesperado: {e}")
        logging.error(f"Error en administrar_usuarios: {e}")


def administrar_inventario(usuario_actual):
    print("\n--- ADMINISTRAR INVENTARIO ---")
    print("1. Listar catálogo completo")
    print("2. Registrar nuevo equipo")
    print("3. Cambiar estado de un equipo (Ej. Mantenimiento)")
    print("4. Volver")
    
    opcion = input("Seleccione una opción: ").strip()
    try:
        datos = Database.cargar_datos()
        equipos = datos.get("equipos", [])
        
        if opcion == "1":
            print(f"\n{'ID':<5} | {'NOMBRE':<25} | {'ESTADO':<15}")
            print("-" * 50)
            for eq in equipos:
                print(f"{eq['id']:<5} | {eq['nombre']:<25} | {eq['estado']:<15}")
                
        elif opcion == "2":
            print("\n-- Registro de Equipo --")
            nombre = input("Nombre del equipo: ").strip()
            if not nombre:
                print("Error: El nombre es obligatorio.")
                return
                
            nuevo_id = max([eq["id"] for eq in equipos] + [0]) + 1
            nuevo_equipo = {
                "id": nuevo_id,
                "nombre": nombre,
                "estado": "DISPONIBLE" # Por defecto, ingresan disponibles
            }
            
            datos["equipos"].append(nuevo_equipo)
            Database.guardar_datos(datos)
            print(f"\n¡Éxito! Equipo '{nombre}' registrado con el ID {nuevo_id}.")
            logging.info(f"Equipo {nuevo_id} creado por Encargado {usuario_actual.id}")
            
        elif opcion == "3":
            id_input = input("Ingrese el ID del equipo: ").strip()
            if not id_input.isdigit():
                print("Error: Ingrese un ID numérico.")
                return
                
            id_eq = int(id_input)
            eq_json = next((eq for eq in equipos if eq["id"] == id_eq), None)
            
            if not eq_json:
                print("Error: Equipo no encontrado.")
                return
                
            print(f"Estado actual: {eq_json['estado']}")
            print("Nuevos estados: 1. DISPONIBLE | 2. MANTENIMIENTO | 3. FUERA_DE_SERVICIO")
            est_op = input("Seleccione el nuevo estado (1, 2 o 3): ").strip()
            
            estados_map = {"1": "DISPONIBLE", "2": "MANTENIMIENTO", "3": "FUERA_DE_SERVICIO"}
            nuevo_estado = estados_map.get(est_op)
            
            if not nuevo_estado:
                print("Error: Opción inválida.")
                return
                
            # Pequeña validación para evitar que el Encargado rompa un préstamo activo
            if eq_json["estado"] == "PRESTADO" and nuevo_estado != "PRESTADO":
                print("Advertencia: El equipo está PRESTADO a un alumno.")
                confirmar = input("¿Forzar el cambio de estado de todas formas? (S/N): ").strip().upper()
                if confirmar != "S":
                    print("Operación cancelada.")
                    return
                    
            eq_json["estado"] = nuevo_estado
            Database.guardar_datos(datos)
            print(f"\n¡Éxito! El equipo {id_eq} ahora está {nuevo_estado}.")
            logging.info(f"Estado de equipo {id_eq} cambiado a {nuevo_estado} por Encargado {usuario_actual.id}")
            
        elif opcion == "4":
            return
        else:
            print("Opción inválida.")
            
    except Exception as e:
        print(f"Error inesperado: {e}")
        logging.error(f"Error en administrar_inventario: {e}")

def solicitudes(usuario_actual):
    print("\n--- APROBAR O RECHAZAR SOLICITUDES ---")
    try:
        datos = Database.cargar_datos()
        # Filtramos solo las pendientes
        pendientes = [s for s in datos.get("solicitudes", []) if s["estado"] == "SOLICITADA"]
        
        if not pendientes:
            print("No hay solicitudes pendientes de revisión.")
            return

        print(f"{'ID':<5} | {'USR_ID':<8} | {'EQUIPOS':<15} | {'FECHA DEV':<12}")
        print("-" * 50)
        for sol in pendientes:
            print(f"{sol['id']:<5} | {sol['usuario_id']:<8} | {str(sol['equipos_ids']):<15} | {sol['fecha_devolucion']:<12}")
        
        id_input = input("\nIngrese el ID de la solicitud a gestionar: ").strip()
        if not id_input.isdigit():
            print("Error: Ingrese un ID numérico.")
            return
            
        id_gestionar = int(id_input)
        solicitud_json = next((s for s in pendientes if s["id"] == id_gestionar), None)
        
        if not solicitud_json:
            print("Error: Solicitud no encontrada o ya fue gestionada.")
            return

        accion = input("¿Desea (A)probar o (R)echazar la solicitud?: ").strip().upper()
        if accion not in ["A", "R"]:
            print("Acción inválida. Operación cancelada.")
            return

        # Reconstruir objeto mínimo para el servicio
        usr_mock = Usuario(id=solicitud_json["usuario_id"], nombre="", correo="", password="", rol="")
        f_ini = datetime.strptime(solicitud_json["fecha_inicio"], "%Y-%m-%d").date()
        f_dev = datetime.strptime(solicitud_json["fecha_devolucion"], "%Y-%m-%d").date()
        
        sol_obj = SolicitudPrestamo(solicitud_json["id"], usr_mock, [], f_ini, f_dev)
        sol_obj.estado = solicitud_json["estado"]

        service = PrestamoService()
        if accion == "A":
            resultado, mensaje = service.aprobar_solicitud(sol_obj)
        else:
            resultado, mensaje = service.rechazar_solicitud(sol_obj)

        # Si el servicio aprueba el cambio, guardamos
        if resultado:
            solicitud_json["estado"] = sol_obj.estado
            Database.guardar_datos(datos)
            print(f"\n¡Éxito! {mensaje}")
            logging.info(f"Solicitud {sol_obj.id} cambiada a {sol_obj.estado} por Encargado {usuario_actual.id}")
        else:
            print(f"\nError: {mensaje}")

    except Exception as e:
        print(f"Error inesperado: {e}")

def entrega(usuario_actual):
    print("\n--- REGISTRAR ENTREGA DE EQUIPOS ---")
    try:
        datos = Database.cargar_datos()
        # Filtramos las aprobadas que están listas para entregar
        aprobadas = [s for s in datos.get("solicitudes", []) if s["estado"] == "APROBADA"]
        
        if not aprobadas:
            print("No hay solicitudes listas para entrega.")
            return

        print(f"{'ID':<5} | {'USR_ID':<8} | {'EQUIPOS':<15}")
        print("-" * 35)
        for sol in aprobadas:
            print(f"{sol['id']:<5} | {sol['usuario_id']:<8} | {str(sol['equipos_ids']):<15}")
        
        id_input = input("\nIngrese el ID de la solicitud a entregar: ").strip()
        if not id_input.isdigit():
            return print("Error: Ingrese un ID numérico.")
            
        id_entregar = int(id_input)
        solicitud_json = next((s for s in aprobadas if s["id"] == id_entregar), None)
        
        if not solicitud_json:
            return print("Error: Solicitud no encontrada.")

        # Reconstruir equipos completos para que el servicio cambie sus estados
        equipos_objs = []
        for eq_json in datos.get("equipos", []):
            if eq_json["id"] in solicitud_json["equipos_ids"]:
                equipos_objs.append(Equipo(eq_json["id"], eq_json["nombre"], eq_json["estado"]))

        usr_mock = Usuario(solicitud_json["usuario_id"], "","","","")
        sol_obj = SolicitudPrestamo(solicitud_json["id"], usr_mock, equipos_objs, datetime.now().date(), datetime.now().date())
        sol_obj.estado = solicitud_json["estado"]

        service = PrestamoService()
        resultado, mensaje = service.registrar_entrega(sol_obj)

        if resultado:
            solicitud_json["estado"] = sol_obj.estado
            # Actualizamos el estado de los equipos en el JSON (ahora dirán "PRESTADO")
            for eq_obj in sol_obj.equipos:
                for eq_json in datos["equipos"]:
                    if eq_json["id"] == eq_obj.id:
                        eq_json["estado"] = eq_obj.estado
                        
            Database.guardar_datos(datos)
            print(f"\n¡Éxito! {mensaje}")
            logging.info(f"Entrega de solicitud {sol_obj.id} registrada por Encargado {usuario_actual.id}")
        else:
            print(f"\nError: {mensaje}")

    except Exception as e:
        print(f"Error inesperado: {e}")

def devolucion(usuario_actual):
    print("\n--- REGISTRAR DEVOLUCIÓN DE EQUIPOS ---")
    try:
        datos = Database.cargar_datos()
        # Filtramos las que ya están en manos del estudiante
        entregadas = [s for s in datos.get("solicitudes", []) if s["estado"] == "ENTREGADA"]
        
        if not entregadas:
            print("No hay préstamos pendientes de devolución.")
            return

        print(f"{'ID':<5} | {'USR_ID':<8} | {'EQUIPOS':<15}")
        print("-" * 35)
        for sol in entregadas:
            print(f"{sol['id']:<5} | {sol['usuario_id']:<8} | {str(sol['equipos_ids']):<15}")
        
        id_input = input("\nIngrese el ID del préstamo a devolver: ").strip()
        if not id_input.isdigit():
            return print("Error: Ingrese un ID numérico.")
            
        id_devolver = int(id_input)
        solicitud_json = next((s for s in entregadas if s["id"] == id_devolver), None)
        
        if not solicitud_json:
            return print("Error: Préstamo no encontrado.")

        equipos_objs = []
        for eq_json in datos.get("equipos", []):
            if eq_json["id"] in solicitud_json["equipos_ids"]:
                equipos_objs.append(Equipo(eq_json["id"], eq_json["nombre"], eq_json["estado"]))

        usr_mock = Usuario(solicitud_json["usuario_id"], "","","","")
        sol_obj = SolicitudPrestamo(solicitud_json["id"], usr_mock, equipos_objs, datetime.now().date(), datetime.now().date())
        sol_obj.estado = solicitud_json["estado"]

        service = PrestamoService()
        resultado, mensaje = service.registrar_devolucion(sol_obj)

        if resultado:
            solicitud_json["estado"] = sol_obj.estado
            # Actualizamos el estado de los equipos en el JSON (ahora volverán a estar "DISPONIBLE")
            for eq_obj in sol_obj.equipos:
                for eq_json in datos["equipos"]:
                    if eq_json["id"] == eq_obj.id:
                        eq_json["estado"] = eq_obj.estado
                        
            Database.guardar_datos(datos)
            print(f"\n¡Éxito! {mensaje}")
            logging.info(f"Devolución de solicitud {sol_obj.id} registrada por Encargado {usuario_actual.id}")
        else:
            print(f"\nError: {mensaje}")

    except Exception as e:
        print(f"Error inesperado: {e}")

def iniciar_menu(usuario_actual):
    while True:
        mostrar_opciones()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            administrar_usuarios(usuario_actual)
        elif opcion == "2":
            administrar_inventario(usuario_actual)
        elif opcion == "3":
            solicitudes(usuario_actual)
        elif opcion == "4":
            entrega(usuario_actual)
        elif opcion == "5":
            devolucion(usuario_actual)
        elif opcion == "6":
            print("Cerrando sesión de Encargado...")
            logging.info(f"Cierre de sesión: {usuario_actual.id}")
            break
        else:
            print("Opción inválida. Intente nuevamente.")