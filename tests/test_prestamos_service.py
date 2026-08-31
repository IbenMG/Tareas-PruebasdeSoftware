from datetime import date, timedelta

from src.models.usuario import Usuario
from src.models.equipo import Equipo
from src.models.solicitud import SolicitudPrestamo
from src.services.prestamo_service import PrestamoService


def crear_usuario():
    return Usuario(
        1,
        "Juan Pérez",
        "juan@universidad.cl",
        "1234",
        "SOLICITANTE"
    )


def crear_equipo(id_equipo, nombre, estado="DISPONIBLE"):
    return Equipo(
        id_equipo,
        nombre,
        estado
    )


def crear_solicitud(
    id_solicitud,
    usuario,
    equipos,
    fecha_inicio,
    fecha_devolucion,
    estado="SOLICITADA"
):
    solicitud = SolicitudPrestamo(
        id_solicitud,
        usuario,
        equipos,
        fecha_inicio,
        fecha_devolucion
    )

    solicitud.estado = estado

    return solicitud


# ---------------------------------------------------
# TC-01: solicitud válida
# ---------------------------------------------------

def test_crear_solicitud_valida():

    service = PrestamoService()

    usuario = crear_usuario()

    equipos = [
        crear_equipo(1, "Notebook"),
        crear_equipo(2, "Cámara")
    ]

    fecha_inicio = date.today()
    fecha_devolucion = fecha_inicio + timedelta(days=5)

    solicitud, mensaje = service.crear_solicitud(
        1,
        usuario,
        equipos,
        fecha_inicio,
        fecha_devolucion,
        [],
        SolicitudPrestamo
    )

    assert solicitud is not None
    assert solicitud.estado == "SOLICITADA"
    assert mensaje == "Solicitud creada correctamente."


# ---------------------------------------------------
# TC-02: superar máximo de 3 equipos
# RN-01
# ---------------------------------------------------

def test_rechazar_mas_de_tres_equipos():

    service = PrestamoService()

    usuario = crear_usuario()

    equipos = [
        crear_equipo(1, "Notebook"),
        crear_equipo(2, "Cámara"),
        crear_equipo(3, "Tablet"),
        crear_equipo(4, "Proyector")
    ]

    fecha_inicio = date.today()
    fecha_devolucion = fecha_inicio + timedelta(days=5)

    solicitud, mensaje = service.crear_solicitud(
        1,
        usuario,
        equipos,
        fecha_inicio,
        fecha_devolucion,
        [],
        SolicitudPrestamo
    )

    assert solicitud is None
    assert "más de 3 equipos" in mensaje


# ---------------------------------------------------
# TC-03: duración superior a 7 días
# RN-02
# ---------------------------------------------------

def test_rechazar_prestamo_mayor_a_siete_dias():

    service = PrestamoService()

    usuario = crear_usuario()

    equipos = [
        crear_equipo(1, "Notebook")
    ]

    fecha_inicio = date.today()
    fecha_devolucion = fecha_inicio + timedelta(days=8)

    solicitud, mensaje = service.crear_solicitud(
        1,
        usuario,
        equipos,
        fecha_inicio,
        fecha_devolucion,
        [],
        SolicitudPrestamo
    )

    assert solicitud is None
    assert "7 días" in mensaje


# ---------------------------------------------------
# TC-04: fecha de devolución inválida
# ---------------------------------------------------

def test_rechazar_fecha_devolucion_anterior():

    service = PrestamoService()

    usuario = crear_usuario()

    equipos = [
        crear_equipo(1, "Notebook")
    ]

    fecha_inicio = date.today()
    fecha_devolucion = fecha_inicio - timedelta(days=1)

    solicitud, mensaje = service.crear_solicitud(
        1,
        usuario,
        equipos,
        fecha_inicio,
        fecha_devolucion,
        [],
        SolicitudPrestamo
    )

    assert solicitud is None
    assert "posterior" in mensaje


# ---------------------------------------------------
# TC-05: usuario con préstamo atrasado
# RN-03
# ---------------------------------------------------

def test_usuario_atrasado_no_puede_solicitar():

    service = PrestamoService()

    usuario = crear_usuario()

    equipo_prestado = crear_equipo(
        1,
        "Notebook",
        "PRESTADO"
    )

    prestamo_atrasado = crear_solicitud(
        100,
        usuario,
        [equipo_prestado],
        date.today() - timedelta(days=10),
        date.today() - timedelta(days=3),
        "ENTREGADA"
    )

    nuevo_equipo = crear_equipo(
        2,
        "Cámara"
    )

    solicitud, mensaje = service.crear_solicitud(
        2,
        usuario,
        [nuevo_equipo],
        date.today(),
        date.today() + timedelta(days=5),
        [prestamo_atrasado],
        SolicitudPrestamo
    )

    assert solicitud is None
    assert "atrasado" in mensaje


# ---------------------------------------------------
# TC-06: equipo en mantenimiento
# RN-07
# ---------------------------------------------------

def test_equipo_en_mantenimiento_no_puede_solicitarse():

    service = PrestamoService()

    usuario = crear_usuario()

    equipo = crear_equipo(
        1,
        "Notebook",
        "MANTENIMIENTO"
    )

    solicitud, mensaje = service.crear_solicitud(
        1,
        usuario,
        [equipo],
        date.today(),
        date.today() + timedelta(days=5),
        [],
        SolicitudPrestamo
    )

    assert solicitud is None
    assert "no está disponible" in mensaje


# ---------------------------------------------------
# TC-07: equipo fuera de servicio
# RN-07
# ---------------------------------------------------

def test_equipo_fuera_de_servicio_no_puede_solicitarse():

    service = PrestamoService()

    usuario = crear_usuario()

    equipo = crear_equipo(
        1,
        "Cámara",
        "FUERA_DE_SERVICIO"
    )

    solicitud, mensaje = service.crear_solicitud(
        1,
        usuario,
        [equipo],
        date.today(),
        date.today() + timedelta(days=5),
        [],
        SolicitudPrestamo
    )

    assert solicitud is None
    assert "no está disponible" in mensaje


# ---------------------------------------------------
# TC-08: solicitud múltiple con un equipo no disponible
# RN-04
# ---------------------------------------------------

def test_solicitud_multiple_se_rechaza_completa():

    service = PrestamoService()

    usuario = crear_usuario()

    equipo1 = crear_equipo(
        1,
        "Notebook",
        "DISPONIBLE"
    )

    equipo2 = crear_equipo(
        2,
        "Cámara",
        "PRESTADO"
    )

    solicitud, mensaje = service.crear_solicitud(
        1,
        usuario,
        [equipo1, equipo2],
        date.today(),
        date.today() + timedelta(days=5),
        [],
        SolicitudPrestamo
    )

    assert solicitud is None
    assert "no está disponible" in mensaje


# ---------------------------------------------------
# TC-09: aprobar una solicitud
# ---------------------------------------------------

def test_aprobar_solicitud():

    service = PrestamoService()

    usuario = crear_usuario()
    equipo = crear_equipo(1, "Notebook")

    solicitud = crear_solicitud(
        1,
        usuario,
        [equipo],
        date.today(),
        date.today() + timedelta(days=5)
    )

    resultado, mensaje = service.aprobar_solicitud(
        solicitud
    )

    assert resultado is True
    assert solicitud.estado == "APROBADA"


# ---------------------------------------------------
# TC-10: no aprobar una solicitud ya aprobada
# ---------------------------------------------------

def test_no_aprobar_solicitud_ya_aprobada():

    service = PrestamoService()

    usuario = crear_usuario()
    equipo = crear_equipo(1, "Notebook")

    solicitud = crear_solicitud(
        1,
        usuario,
        [equipo],
        date.today(),
        date.today() + timedelta(days=5),
        "APROBADA"
    )

    resultado, mensaje = service.aprobar_solicitud(
        solicitud
    )

    assert resultado is False
    assert solicitud.estado == "APROBADA"


# ---------------------------------------------------
# TC-11: cancelar solicitud
# RN-05
# ---------------------------------------------------

def test_cancelar_solicitud_aprobada():

    service = PrestamoService()

    usuario = crear_usuario()
    equipo = crear_equipo(1, "Notebook")

    solicitud = crear_solicitud(
        1,
        usuario,
        [equipo],
        date.today(),
        date.today() + timedelta(days=5),
        "APROBADA"
    )

    resultado, mensaje = service.cancelar_solicitud(
        solicitud
    )

    assert resultado is True
    assert solicitud.estado == "CANCELADA"


# ---------------------------------------------------
# TC-12: solicitud entregada no puede cancelarse
# RN-06
# ---------------------------------------------------

def test_no_cancelar_solicitud_entregada():

    service = PrestamoService()

    usuario = crear_usuario()
    equipo = crear_equipo(1, "Notebook", "PRESTADO")

    solicitud = crear_solicitud(
        1,
        usuario,
        [equipo],
        date.today(),
        date.today() + timedelta(days=5),
        "ENTREGADA"
    )

    resultado, mensaje = service.cancelar_solicitud(
        solicitud
    )

    assert resultado is False
    assert solicitud.estado == "ENTREGADA"


# ---------------------------------------------------
# TC-13: entregar solicitud aprobada
# ---------------------------------------------------

def test_entregar_solicitud_aprobada():

    service = PrestamoService()

    usuario = crear_usuario()
    equipo = crear_equipo(1, "Notebook")

    solicitud = crear_solicitud(
        1,
        usuario,
        [equipo],
        date.today(),
        date.today() + timedelta(days=5),
        "APROBADA"
    )

    resultado, mensaje = service.registrar_entrega(
        solicitud
    )

    assert resultado is True
    assert solicitud.estado == "ENTREGADA"
    assert equipo.estado == "PRESTADO"


# ---------------------------------------------------
# TC-14: no entregar una solicitud no aprobada
# ---------------------------------------------------

def test_no_entregar_solicitud_solicitada():

    service = PrestamoService()

    usuario = crear_usuario()
    equipo = crear_equipo(1, "Notebook")

    solicitud = crear_solicitud(
        1,
        usuario,
        [equipo],
        date.today(),
        date.today() + timedelta(days=5),
        "SOLICITADA"
    )

    resultado, mensaje = service.registrar_entrega(
        solicitud
    )

    assert resultado is False
    assert solicitud.estado == "SOLICITADA"


# ---------------------------------------------------
# TC-15: registrar devolución
# ---------------------------------------------------

def test_devolver_equipo_entregado():

    service = PrestamoService()

    usuario = crear_usuario()

    equipo = crear_equipo(
        1,
        "Notebook",
        "PRESTADO"
    )

    solicitud = crear_solicitud(
        1,
        usuario,
        [equipo],
        date.today() - timedelta(days=3),
        date.today() + timedelta(days=2),
        "ENTREGADA"
    )

    resultado, mensaje = service.registrar_devolucion(
        solicitud
    )

    assert resultado is True
    assert solicitud.estado == "DEVUELTA"
    assert equipo.estado == "DISPONIBLE"