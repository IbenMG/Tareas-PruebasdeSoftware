# Matriz de trazabilidad

La presente matriz de trazabilidad relaciona el requerimiento mejorado con las reglas de negocio y los criterios de aceptación definidos para el sistema.

Las columnas correspondientes a la evidencia de implementación, casos de prueba y resultados serán completadas durante las etapas de implementación y ejecución de pruebas.

| ID Requerimiento | Regla relacionada | Criterio de aceptación | Evidencia de implementación | Caso de prueba | Resultado |
|---|---|---|---|---|---|
| RQ-01 | - | CA-01 - Inicio de sesión correcto | Pendiente | Pendiente | Pendiente |
| RQ-01 | - | CA-02 - Inicio de sesión incorrecto | Pendiente | Pendiente | Pendiente |
| RQ-01 | - | CA-03 - Registro de usuarios | Pendiente | Pendiente | Pendiente |
| RQ-01 | - | CA-04 - Registro de equipos | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-07 | CA-05 - Equipo no disponible | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-01 | CA-06 - Límite máximo de equipos | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-01 | CA-07 - Solicitud dentro del límite | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-02 | CA-08 - Duración máxima permitida | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-02 | CA-09 - Duración excedida | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-03 | CA-10 - Préstamo atrasado | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-04 | CA-11 - Solicitud con múltiples equipos | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-01, RN-02, RN-03, RN-04, RN-07 | CA-12 - Aprobación de solicitud | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-05, RN-06 | CA-13 - Cancelación de solicitud | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-06 | CA-14 - Entrega de equipos | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-06 | CA-15 - Devolución | Pendiente | Pendiente | Pendiente |
| RQ-01 | RN-08 | CA-16 - Renovaciones | Pendiente | Pendiente | Pendiente |

## Estado de la matriz

En esta etapa del proyecto, la matriz contiene la trazabilidad entre:

- El requerimiento mejorado (`RQ-01`).
- Las reglas de negocio (`RN-01` a `RN-08`).
- Los criterios de aceptación (`CA-01` a `CA-16`).

Las siguientes relaciones serán incorporadas durante el desarrollo:

- Evidencia de implementación.
- Casos de prueba (`TC-XX`).
- Resultado obtenido durante la ejecución de cada prueba.

Por ejemplo, una vez implementada y probada la duración máxima de los préstamos, la trazabilidad podrá representarse de la siguiente forma:

`RQ-01 → RN-02 → CA-09 → implementación → TC-XX → PASS/FAIL`