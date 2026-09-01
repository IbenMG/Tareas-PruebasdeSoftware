
La presente matriz de trazabilidad relaciona el requerimiento mejorado con las reglas de negocio y los criterios de aceptación definidos para el sistema.

Las columnas correspondientes a la evidencia de implementación, casos de prueba y resultados serán completadas durante las etapas de implementación y ejecución de pruebas.

| ID Requerimiento | Criterio de aceptación | Evidencia de implementación | Caso(s) de prueba | Resultado |
|---|---|---|---|---|
| **RQ-01** | **CA-01** - Inicio de sesión correcto según rol | `AutenticacionService.iniciar_sesion()` | TC-01 | ✓ |
| **RQ-01** | **CA-02** - Credenciales inválidas / acceso denegado | `AutenticacionService.iniciar_sesion()` | TC-02 | ✓ |
| **RQ-02** | **CA-03** - Registro de nuevos usuarios | `encargado.administrar_usuarios()` | TC-09, TC-10 | ✓ |
| **RQ-03** | **CA-04** - Registro de nuevos equipos con identificador único | `encargado.administrar_inventario()` | TC-11 | ✓ |
| **RQ-06** | **CA-05** - Máximo de 3 equipos simultáneos | `PrestamoService.validar_solicitud()` | TC-04, TC-05 | ✓ |
| **RQ-07** | **CA-06** - Duración máxima de 7 días | `PrestamoService.validar_solicitud()` | TC-06 | ✓ |
| **RQ-12** | **CA-07** - Bloqueo de usuario con préstamo atrasado | `PrestamoService.validar_solicitud()` | TC-07 | ✓ |
| **RQ-13** | **CA-08** - Equipo en mantenimiento o fuera de servicio no puede reservarse | `PrestamoService.validar_solicitud()` | TC-08 | ✓ |
| **RQ-14** | **CA-09** - Solicitud múltiple rechazada completamente si un equipo no está disponible | `PrestamoService.validar_solicitud()` | TC-08, TC-16 | ✓ |
| **RQ-08** | **CA-10** - Aprobación de una solicitud únicamente si cumple las reglas de negocio | `PrestamoService.aprobar_solicitud()` y `encargado.solicitudes()` | TC-12, TC-16 | ✓ |
| **RQ-09** | **CA-11** - Cancelación bloqueada después de la entrega | `PrestamoService.cancelar_solicitud()` y `solicitante.cancelar_solicitud()` | TC-14 | ✓ |
| **RQ-10** | **CA-12** - Entrega permitida únicamente para solicitudes previamente aprobadas | `PrestamoService.registrar_entrega()` | TC-15 | ✓ |
| **RQ-11** | **CA-13** - Devolución permitida únicamente para préstamos previamente entregados | `PrestamoService.registrar_devolucion()` | TC-15 | ✓ |
| **RQ-17** | **CA-14** - No se permiten renovaciones de préstamos aprobados o entregados | No existe una operación explícita de renovación; debe verificarse mediante pruebas | TC-17 | ✓ |
| **RQ-16** | **CA-15** - Registro de eventos relevantes mediante logs | `logging` y archivo `app.log` | TC-18 | ✓ |
| **RQ-05** | **CA-16** - Creación correcta de una solicitud válida | `solicitante.solicitud_prestamo()` y `PrestamoService.crear_solicitud()` | TC-03 | ✓ |
| **RQ-04** | **CA-17** - Consulta del catálogo de equipos | `solicitante.consultar_catalogo()` | TC-19 | ✓ |
| **RQ-15** | **CA-18** - Consulta de préstamos asociados al usuario autenticado | `solicitante.mis_prestamos()` | TC-20 | ✓ |
| **RQ-08** | **CA-19** - Rechazo de una solicitud en estado SOLICITADA | `PrestamoService.rechazar_solicitud()` y `encargado.solicitudes()` | TC-13 | ✓ |
