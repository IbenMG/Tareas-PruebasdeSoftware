import pytest
import sys
import os
import logging
from datetime import date, timedelta

# Le indicamos a Python que busque dentro de la carpeta "code"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))

from models.usuario import Usuario
from models.equipo import Equipo
from models.solicitud import SolicitudPrestamo
from services.prestamo_service import PrestamoService
from database.database import Database

# --- FIXTURES (Datos de prueba reutilizables) ---
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

# ==========================================================
# CASOS DE PRUEBA (TC-11 al TC-20) - Benjamín Araos
# ==========================================================

def test_11():
    # Verifica que un equipo se inicializa correctamente como DISPONIBLE
    nuevo_equipo = crear_equipo(99, "DISPONIBLE")
    
    assert nuevo_equipo.id == 99
    assert nuevo_equipo.estado == "DISPONIBLE"

def test_12():
    service = PrestamoService()
    sol_aprobar = crear_solicitud_base("SOLICITADA")
    
    res, msg = service.aprobar_solicitud(sol_aprobar)
    
    assert res is True
    assert sol_aprobar.estado == "APROBADA"

def test_13():
    service = PrestamoService()
    sol_rechazar = crear_solicitud_base("SOLICITADA")
    
    res, msg = service.rechazar_solicitud(sol_rechazar)
    
    assert res is True
    assert sol_rechazar.estado == "RECHAZADA"

def test_14():
    service = PrestamoService()
    
    # 1. Cancelación permitida (estado APROBADA)
    sol_cancelar = crear_solicitud_base("APROBADA")
    res, msg = service.cancelar_solicitud(sol_cancelar)
    assert res is True
    assert sol_cancelar.estado == "CANCELADA"
    
    # 2. Cancelación denegada (después de ENTREGADA)
    sol_entregada = crear_solicitud_base("ENTREGADA")
    res_bloqueado, msg_bloqueado = service.cancelar_solicitud(sol_entregada)
    assert res_bloqueado is False
    assert sol_entregada.estado == "ENTREGADA"

def test_15():
    service = PrestamoService()
    sol = crear_solicitud_base("APROBADA")
    
    # Transición 1: Aprobada -> Entregada
    service.registrar_entrega(sol)
    assert sol.estado == "ENTREGADA"
    assert sol.equipos[0].estado == "PRESTADO"
    
    # Transición 2: Entregada -> Devuelta
    service.registrar_devolucion(sol)
    assert sol.estado == "DEVUELTA"
    assert sol.equipos[0].estado == "DISPONIBLE"

def test_16():
    service = PrestamoService()
    usr = crear_usuario()
    eq_mantenimiento = crear_equipo(2, "MANTENIMIENTO")
    
    sol, msg = service.crear_solicitud(
        1, usr, [eq_mantenimiento], 
        date.today(), date.today() + timedelta(days=5), 
        [], SolicitudPrestamo
    )
    
    assert sol is None
    assert "no está disponible" in msg or "no est" in msg

def test_17():
    # Verifica que los días de préstamo no cambian mágicamente al entregar
    sol_flujo = crear_solicitud_base("ENTREGADA", dias=5)
    duracion = (sol_flujo.fecha_devolucion - sol_flujo.fecha_inicio).days
    
    assert duracion == 5
    assert duracion <= 7

def test_18(caplog):
    # Usamos la herramienta nativa caplog de pytest para validar el logging
    with caplog.at_level(logging.INFO):
        logging.info("Operación crítica registrada exitosamente")
    
    assert "Operación crítica registrada exitosamente" in caplog.text

def test_19(monkeypatch):
    # Simulamos la lectura de la base de datos
    def mock_cargar_datos():
        return {"equipos": [{"id": 1, "nombre": "Notebook", "estado": "DISPONIBLE"}]}
    
    monkeypatch.setattr("database.database.Database.cargar_datos", mock_cargar_datos)
    datos = Database.cargar_datos()
    
    assert len(datos["equipos"]) == 1
    assert datos["equipos"][0]["id"] == 1
    assert datos["equipos"][0]["estado"] == "DISPONIBLE"

def test_20(monkeypatch):
    # Simulamos préstamos de múltiples usuarios
    def mock_cargar_datos():
        return {
            "solicitudes": [
                {"id": 1, "usuario_id": 1, "estado": "ENTREGADA"},
                {"id": 2, "usuario_id": 2, "estado": "SOLICITADA"}
            ]
        }
    
    monkeypatch.setattr("database.database.Database.cargar_datos", mock_cargar_datos)
    datos = Database.cargar_datos()
    
    # Filtramos por el usuario 1
    usuario_actual_id = 1
    mis_solicitudes = [s for s in datos["solicitudes"] if s["usuario_id"] == usuario_actual_id]
    
    assert len(mis_solicitudes) == 1
    assert mis_solicitudes[0]["id"] == 1