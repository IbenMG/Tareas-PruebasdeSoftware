from datetime import date

from models.usuario import Usuario
from models.equipo import Equipo
from models.solicitud import SolicitudPrestamo
from services.prestamo_service import PrestamoService


usuario = Usuario(
    1,
    "Juan Pérez",
    "juan@universidad.cl",
    "1234",
    "SOLICITANTE"
)

notebook = Equipo(
    1,
    "Notebook Lenovo",
    "DISPONIBLE"
)

camara = Equipo(
    2,
    "Cámara Canon",
    "DISPONIBLE"
)

equipos = [notebook, camara]

fecha_inicio = date(2026, 8, 30)
fecha_devolucion = date(2026, 9, 5)

prestamos_activos = []

service = PrestamoService()

solicitud, mensaje = service.crear_solicitud(
    1,
    usuario,
    equipos,
    fecha_inicio,
    fecha_devolucion,
    prestamos_activos,
    SolicitudPrestamo
)

print(mensaje)

if solicitud:
    print("ID:", solicitud.id)
    print("Usuario:", solicitud.usuario.nombre)
    print("Estado:", solicitud.estado)
    print("Cantidad de equipos:", len(solicitud.equipos))
print("\n--- PRUEBA DE TRANSICIONES ---")

resultado, mensaje = service.aprobar_solicitud(solicitud)
print(mensaje)
print("Estado:", solicitud.estado)

resultado, mensaje = service.registrar_entrega(solicitud)
print(mensaje)
print("Estado:", solicitud.estado)

resultado, mensaje = service.registrar_devolucion(solicitud)
print(mensaje)
print("Estado:", solicitud.estado)