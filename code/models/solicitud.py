class SolicitudPrestamo:
    def __init__(self, id, usuario, equipos, fecha_inicio, fecha_devolucion):
        self.id = id
        self.usuario = usuario
        self.equipos = equipos
        self.fecha_inicio = fecha_inicio
        self.fecha_devolucion = fecha_devolucion
        self.estado = "SOLICITADA"