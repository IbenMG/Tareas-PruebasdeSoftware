# Requerimiento mejorado

El sistema deberá permitir gestionar, mediante una aplicación ejecutada por
terminal, el préstamo de equipos tecnológicos pertenecientes a un laboratorio
universitario.

El sistema deberá permitir el acceso de usuarios autorizados mediante
autenticación. Existirán al menos dos roles: solicitante y encargado.

El solicitante podrá consultar equipos y gestionar sus propias solicitudes.
El encargado podrá administrar usuarios y equipos, aprobar o rechazar
solicitudes y registrar entregas y devoluciones.

Cada equipo será registrado individualmente y contará con un identificador
único y un estado operativo. Los equipos en mantenimiento o fuera de servicio
no podrán ser solicitados.

Un solicitante podrá generar solicitudes para uno o más equipos. Las solicitudes
con múltiples equipos se tratarán como una unidad completa.

Un solicitante podrá mantener como máximo tres equipos simultáneamente y la
duración máxima de un préstamo será de siete días. Un solicitante con préstamos
atrasados no podrá generar nuevas solicitudes.

Las solicitudes podrán ser aprobadas o rechazadas por un encargado. Podrán
cancelarse mientras estén SOLICITADAS o APROBADAS. Una vez registrada la
entrega, deberán finalizar mediante devolución.

El sistema permitirá consultar préstamos vigentes, futuros y atrasados y
registrará mediante logs los eventos relevantes y errores ocurridos durante
la ejecución.

No se permitirán renovaciones, notificaciones mediante correo electrónico ni
aprobaciones parciales de solicitudes con múltiples equipos.


# Desglose funcional del requerimiento

Los siguientes requisitos funcionales descomponen el requerimiento mejorado con el objetivo de facilitar su implementación, verificación,
validación y trazabilidad.

| ID | Requisito funcional |
|---|---|
| RQ-01 | El sistema deberá autenticar a los usuarios mediante sus credenciales. |
| RQ-02 | El encargado deberá poder registrar personas autorizadas. |
| RQ-03 | El encargado deberá poder registrar equipos individualmente. |
| RQ-04 | El sistema deberá permitir consultar los equipos y su estado. |
| RQ-05 | El solicitante deberá poder crear solicitudes para uno o más equipos. |
| RQ-06 | El sistema deberá impedir superar el máximo de tres equipos simultáneos. |
| RQ-07 | El sistema deberá impedir préstamos cuya duración supere siete días. |
| RQ-08 | El encargado deberá poder aprobar o rechazar solicitudes. |
| RQ-09 | El sistema deberá permitir cancelar solicitudes únicamente en los estados permitidos. |
| RQ-10 | El encargado deberá poder registrar la entrega de una solicitud aprobada. |
| RQ-11 | El encargado deberá poder registrar la devolución de un préstamo entregado. |
| RQ-12 | El sistema deberá impedir nuevas solicitudes de usuarios con préstamos atrasados. |
| RQ-13 | El sistema deberá impedir solicitar equipos en mantenimiento o fuera de servicio. |
| RQ-14 | Las solicitudes con varios equipos deberán procesarse como una unidad completa. |
| RQ-15 | El sistema deberá permitir consultar préstamos vigentes, futuros y atrasados. |
| RQ-16 | El sistema deberá registrar eventos relevantes y errores mediante logs. |
| RQ-17 | El sistema no deberá permitir renovar o extender un préstamo aprobado o entregado. |