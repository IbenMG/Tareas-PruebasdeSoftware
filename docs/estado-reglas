## Estados

El sistema utilizara los siguientes estados para representar el ciclo de vida
de una solicitud o préstamo:

- **SOLICITADA:** La solicitud fue creada por un solicitante y se encuentra pendiente de revisión.
- **APROBADA:** La solicitud fue revisada y aprobada por un encargado.
- **RECHAZADA:** La solicitud fue rechazada por un encargado.
- **CANCELADA:** La solicitud fue cancelada antes de la entrega.
- **ENTREGADA:** Los equipos asociados a la solicitud fueron entregados al solicitante.
- **DEVUELTA:** Todos los equipos asociados al préstamo fueron devueltos.

## Transiciones permitidas con sus roles autorizados

| Estado actual | Nuevo estado | Rol autorizado | Condicion |
|---|---|---|---|
| SOLICITADA | APROBADA | Encargado | La solicitud cumple las reglas de negocio y todos los equipos pueden ser prestados. |
| SOLICITADA | RECHAZADA | Encargado | El encargado decide rechazar la solicitud o alguna condicion necesaria no se cumple. |
| SOLICITADA | CANCELADA | Solicitante / Encargado | La solicitud aun no ha sido entregada. |
| APROBADA | ENTREGADA | Encargado | Todos los equipos asociados se encuentran disponibles y la solicitud continua vigente. |
| APROBADA | CANCELADA | Solicitante / Encargado | Los equipos aun no han sido entregados. |
| ENTREGADA | DEVUELTA | Encargado | Todos los equipos asociados al prestamo son devueltos. |

### Transiciones no permitidas

El sistema deberá impedir, entre otras, las siguientes transiciones:

- RECHAZADA → APROBADA
- CANCELADA → APROBADA
- ENTREGADA → CANCELADA
- DEVUELTA → ENTREGADA
- DEVUELTA → APROBADA
- SOLICITADA → ENTREGADA

Si una solicitud fue rechazada o cancelada y el solicitante desea realizar un nuevo préstamo, deberá generar una nueva solicitud.

### Roles

#### Solicitante

El solicitante podrá:

- Crear solicitudes.
- Consultar sus solicitudes y préstamos.
- Cancelar una solicitud mientras se encuentre en estado SOLICITADA o APROBADA.

El solicitante no podrá:

- Aprobar solicitudes.
- Rechazar solicitudes.
- Registrar entregas.
- Registrar devoluciones.

#### Encargado

El encargado podrá:

- Aprobar solicitudes.
- Rechazar solicitudes.
- Cancelar solicitudes cuando corresponda.
- Registrar la entrega de los equipos.
- Registrar la devolución de los equipos.
- Administrar usuarios y equipos.

## Condiciones que impiden operaciones

Una solicitud no podrá ser aprobada o continuar con el préstamo cuando:

- El solicitante supere el máximo de tres equipos simultáneos.
- La duración solicitada sea superior a siete días.
- El solicitante mantenga préstamos atrasados.
- Uno o más equipos se encuentren en mantenimiento o fuera de servicio.
- Uno o más equipos no se encuentren disponibles para el préstamo.
- La solicitud se encuentre en un estado que no permita la operación solicitada.

Una solicitud que contenga múltiples equipos será tratada como una unidad
completa. Si alguno de los equipo no cumple las condiciones necesarias,
la solicitud completa no podrá ser aprobada.

## Disponibilidad de los equipos

Un equipo se considerará disponible cuando:

- Se encuentre registrado en el sistema.
- Su estado operativo permita ser prestado.
- No se encuentre asociado a un préstamo activo que impida su entrega.
- No exista otra condición de negocio que impida su utilización.

Los equipos en mantenimiento o fuera de servicio se considerarán no disponibles.

La disponibilidad deberá verificarse nuevamente antes de aprobar una solicitud
y antes de registrar la entrega.
