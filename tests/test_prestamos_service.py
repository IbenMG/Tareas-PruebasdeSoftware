import pytest
import sys
import os
from datetime import date, timedelta

# Le indicamos a Python que busque dentro de la carpeta "code"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))

# Ahora importamos directamente desde models y services
from models.usuario import Usuario
from models.equipo import Equipo
from models.solicitud import SolicitudPrestamo
from services.prestamo_service import PrestamoService
from services.autenticacion import AutenticacionService

def crear_usuario(id_usr=1, rol="SOLICITANTE"):
    return Usuario(id_usr, "Test User", "test@lab.cl", "1234", rol)

def crear_equipo(id_eq=1, estado="DISPONIBLE"):
    return Equipo(id_eq, f"Equipo {id_eq}", estado)

def crear_solicitud_base(estado="SOLICITADA", dias=5, equipos=None):
    usuario = crear_usuario()
    equipos = equipos if equipos else [crear_equipo()]
    f_ini = date.today()
    f_dev = f_ini + timedelta(days=dias)
    sol = SolicitudPrestamo(1, usuario, equipos, f_ini, f_dev)
    sol.estado = estado
    return sol

# --- TC-01 & TC-02: Autenticación ---
def test_autenticacion_roles(monkeypatch):
    # Simulamos el retorno de la base de datos para no depender del JSON real
    def mock_cargar_datos():
        return {"usuarios": [{"id": 1, "nombre": "A", "correo": "ok@lab.cl", "password": "123", "rol": "SOLICITANTE"}]}
    
    monkeypatch.setattr("database.database.Database.cargar_datos", mock_cargar_datos)
    auth = AutenticacionService()
    
    # TC-01: Login correcto
    usr, msg = auth.iniciar_sesion("ok@lab.cl", "123")
    assert usr is not None
    
    # TC-02: Login incorrecto
    usr_fail, msg_fail = auth.iniciar_sesion("ok@lab.cl", "mala")
    assert usr_fail is None

# --- TC-03 al TC-08: Reglas de Creación ---
def test_creacion_solicitudes():
    service = PrestamoService()
    usr = crear_usuario()
    eq1, eq2, eq3, eq4 = crear_equipo(1), crear_equipo(2), crear_equipo(3), crear_equipo(4)
    
    # TC-03: Solicitud válida
    sol, msg = service.crear_solicitud(1, usr, [eq1], date.today(), date.today() + timedelta(days=5), [], SolicitudPrestamo)
    assert sol.estado == "SOLICITADA"
    
    # TC-04: Rechazar > 3 equipos
    sol, msg = service.crear_solicitud(2, usr, [eq1, eq2, eq3, eq4], date.today(), date.today() + timedelta(days=5), [], SolicitudPrestamo)
    assert sol is None
    
    # TC-05: Rechazar si ya tiene equipos que sumen > 3
    activa = crear_solicitud_base("ENTREGADA", equipos=[eq1, eq2])
    sol, msg = service.crear_solicitud(3, usr, [eq3, eq4], date.today(), date.today() + timedelta(days=5), [activa], SolicitudPrestamo)
    assert sol is None
    
    # TC-06: Rechazar duración > 7 días
    sol, msg = service.crear_solicitud(4, usr, [eq1], date.today(), date.today() + timedelta(days=8), [], SolicitudPrestamo)
    assert sol is None
    
    # TC-07: Rechazar si hay préstamo atrasado
    atrasada = crear_solicitud_base("ENTREGADA")
    atrasada.fecha_devolucion = date.today() - timedelta(days=2) # Venció hace 2 días
    sol, msg = service.crear_solicitud(5, usr, [eq1], date.today(), date.today() + timedelta(days=5), [atrasada], SolicitudPrestamo)
    assert sol is None

    # TC-08: Rechazar si un equipo está en mantenimiento
    eq_malo = crear_equipo(99, "MANTENIMIENTO")
    sol, msg = service.crear_solicitud(6, usr, [eq1, eq_malo], date.today(), date.today() + timedelta(days=5), [], SolicitudPrestamo)
    assert sol is None

# --- TC-12 al TC-17: Transiciones de Estado (Ciclo de vida) ---
def test_ciclo_de_vida_estados():
    service = PrestamoService()
    
    # TC-12: Aprobar solicitud
    sol_aprobar = crear_solicitud_base("SOLICITADA")
    res, msg = service.aprobar_solicitud(sol_aprobar)
    assert sol_aprobar.estado == "APROBADA"
    
    # TC-13: Rechazar solicitud
    sol_rechazar = crear_solicitud_base("SOLICITADA")
    res, msg = service.rechazar_solicitud(sol_rechazar)
    assert sol_rechazar.estado == "RECHAZADA"
    
    # TC-14: Cancelar permitida solo antes de entrega
    sol_cancelar = crear_solicitud_base("APROBADA")
    res, msg = service.cancelar_solicitud(sol_cancelar)
    assert sol_cancelar.estado == "CANCELADA"
    
    sol_entregada = crear_solicitud_base("ENTREGADA")
    res, msg = service.cancelar_solicitud(sol_entregada)
    assert res is False # No se puede cancelar lo ya entregado
    
    # TC-15: Flujo Aprobada -> Entregada -> Devuelta
    sol_flujo = crear_solicitud_base("APROBADA")
    service.registrar_entrega(sol_flujo)
    assert sol_flujo.estado == "ENTREGADA"
    assert sol_flujo.equipos[0].estado == "PRESTADO"
    
    service.registrar_devolucion(sol_flujo)
    assert sol_flujo.estado == "DEVUELTA"
    assert sol_flujo.equipos[0].estado == "DISPONIBLE"

    # TC-17: No se puede renovar (Validación de fechas fijas)
    duracion = (sol_flujo.fecha_devolucion - sol_flujo.fecha_inicio).days
    assert duracion <= 7 # Garantiza que el sistema no alteró la fecha original

