from datetime import datetime


class PrestamoService:

    MAX_EQUIPOS = 3
    MAX_DIAS_PRESTAMO = 7

    def validar_solicitud(
        self,
        usuario,
        equipos,
        fecha_inicio,
        fecha_devolucion,
        prestamos_activos
    ):

        # RN-01: máximo 3 equipos simultáneamente
        cantidad_actual = 0

        for prestamo in prestamos_activos:
            if (
                prestamo.usuario.id == usuario.id
                and prestamo.estado in ["APROBADA", "ENTREGADA"]
            ):
                cantidad_actual += len(prestamo.equipos)

        if cantidad_actual + len(equipos) > self.MAX_EQUIPOS:
            return False, "El usuario no puede tener más de 3 equipos simultáneamente."

        # RN-02: duración máxima de 7 días
        duracion = (fecha_devolucion - fecha_inicio).days

        if duracion <= 0:
            return False, "La fecha de devolución debe ser posterior a la fecha de inicio."

        if duracion > self.MAX_DIAS_PRESTAMO:
            return False, "El préstamo no puede superar los 7 días."

        # RN-03: solo bloquea una nueva solicitud si el préstamo sigue vigente
        # y ya venció su fecha de devolución. Un préstamo devuelto no puede
        # seguir considerándose como atrasado.
        hoy = datetime.now().date()

        for prestamo in prestamos_activos:
            if (
                prestamo.usuario.id == usuario.id
                and prestamo.estado == "ENTREGADA"
                and prestamo.fecha_devolucion < hoy
            ):
                return False, "El usuario posee un préstamo atrasado."

        # RN-07: equipo en mantenimiento o fuera de servicio
        for equipo in equipos:
            if equipo.estado in ["MANTENIMIENTO", "FUERA_DE_SERVICIO"]:
                return False, (
                    f"El equipo '{equipo.nombre}' no está disponible para préstamo."
                )

        # RN-04: la solicitud múltiple se trata como una unidad completa
        # Si un equipo no está disponible, se rechaza toda la solicitud
        for equipo in equipos:
            if equipo.estado != "DISPONIBLE":
                return False, (
                    f"El equipo '{equipo.nombre}' no está disponible."
                )

        return True, "Solicitud válida."

    def crear_solicitud(
        self,
        id_solicitud,
        usuario,
        equipos,
        fecha_inicio,
        fecha_devolucion,
        prestamos_activos,
        clase_solicitud
    ):

        valida, mensaje = self.validar_solicitud(
            usuario,
            equipos,
            fecha_inicio,
            fecha_devolucion,
            prestamos_activos
        )

        if not valida:
            return None, mensaje

        solicitud = clase_solicitud(
            id_solicitud,
            usuario,
            equipos,
            fecha_inicio,
            fecha_devolucion
        )

        return solicitud, "Solicitud creada correctamente."

    def aprobar_solicitud(self, solicitud):

        if solicitud.estado != "SOLICITADA":
            return False, (
                "Solo se pueden aprobar solicitudes en estado SOLICITADA."
            )

        solicitud.estado = "APROBADA"

        return True, "Solicitud aprobada correctamente."

    def rechazar_solicitud(self, solicitud):

        if solicitud.estado != "SOLICITADA":
            return False, (
                "Solo se pueden rechazar solicitudes en estado SOLICITADA."
            )

        solicitud.estado = "RECHAZADA"

        for equipo in solicitud.equipos:
            equipo.estado = "DISPONIBLE"

        return True, "Solicitud rechazada correctamente."

    def cancelar_solicitud(self, solicitud):

        if solicitud.estado not in ["SOLICITADA", "APROBADA"]:
            return False, (
                "Solo se pueden cancelar solicitudes SOLICITADAS o APROBADAS."
            )

        solicitud.estado = "CANCELADA"

        for equipo in solicitud.equipos:
            equipo.estado = "DISPONIBLE"

        return True, "Solicitud cancelada correctamente."

    def registrar_entrega(self, solicitud):

        if solicitud.estado != "APROBADA":
            return False, (
                "Solo se pueden entregar solicitudes APROBADAS."
            )

        solicitud.estado = "ENTREGADA"

        # Los equipos quedan marcados como prestados
        for equipo in solicitud.equipos:
            equipo.estado = "PRESTADO"

        return True, "Entrega registrada correctamente."

    def registrar_devolucion(self, solicitud):

        if solicitud.estado != "ENTREGADA":
            return False, (
                "Solo se pueden devolver préstamos ENTREGADOS."
            )

        solicitud.estado = "DEVUELTA"

        # Los equipos vuelven a estar disponibles
        for equipo in solicitud.equipos:
            equipo.estado = "DISPONIBLE"

        return True, "Devolución registrada correctamente."