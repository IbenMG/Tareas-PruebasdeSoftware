# Plan de Pruebas

## Iben Muñoz

| ID | Descripción | Estado |
|---|---|---|
| **TC-01** | Verificar inicio de sesión correcto con credenciales válidas de un solicitante. | PENDIENTE |
| **TC-02** | Verificar que se rechace el inicio de sesión con contraseña incorrecta. | PENDIENTE |
| **TC-03** | Verificar la creación correcta de una solicitud válida con equipos disponibles. | PENDIENTE |
| **TC-04** | Verificar que se rechace una solicitud de más de 3 equipos simultáneos. | PENDIENTE |
| **TC-05** | Verificar que un usuario con 2 equipos activos no pueda solicitar otros 2, ya que superaría el máximo permitido. | PENDIENTE |
| **TC-06** | Verificar que se rechace una solicitud cuya duración sea superior a 7 días. | PENDIENTE |
| **TC-07** | Verificar que un usuario con un préstamo atrasado no pueda crear una nueva solicitud. | PENDIENTE |
| **TC-08** | Verificar que una solicitud múltiple sea rechazada completamente si uno de los equipos está en mantenimiento o no disponible. | PENDIENTE |
| **TC-09** | Verificar que un encargado pueda registrar correctamente un nuevo usuario. | PENDIENTE |
| **TC-10** | Verificar que se rechace el registro de un usuario cuando faltan datos obligatorios. | PENDIENTE |

## Benjamin Araos

| ID | Descripción | Estado |
|---|---|---|
| **TC-11** | Verificar que un encargado pueda registrar correctamente un nuevo equipo y que este quede inicialmente disponible. | PENDIENTE |
| **TC-12** | Verificar que una solicitud válida en estado `SOLICITADA` pueda ser aprobada. | PENDIENTE |
| **TC-13** | Verificar que una solicitud en estado `SOLICITADA` pueda ser rechazada por el encargado. | PENDIENTE |
| **TC-14** | Verificar que una solicitud pueda cancelarse únicamente en los estados permitidos y no después de ser entregada. | PENDIENTE |
| **TC-15** | Verificar el flujo completo `SOLICITADA → APROBADA → ENTREGADA → DEVUELTA` y la actualización del estado de los equipos. | PENDIENTE |
| **TC-16** | Verificar que no pueda aprobarse una solicitud si uno de sus equipos pasa a mantenimiento antes de la aprobación. | PENDIENTE |
| **TC-17** | Verificar que no sea posible renovar o extender la fecha de devolución de un préstamo aprobado o entregado. | PENDIENTE |
| **TC-18** | Verificar que las operaciones relevantes del sistema queden registradas en `app.log`. | PENDIENTE |
| **TC-19** | Verificar que el solicitante pueda consultar el catálogo mostrando ID, nombre y estado de los equipos. | PENDIENTE |
| **TC-20** | Verificar que un solicitante pueda consultar únicamente sus propios préstamos y solicitudes. | PENDIENTE |
