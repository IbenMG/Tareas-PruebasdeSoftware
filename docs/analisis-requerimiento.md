# Análisis del requerimiento

## 1. Contexto

En esta tarea, desarrollada en parejas, deberán analizar, implementar y probar una aplicación wpara gestionar el préstamo de equipos tecnológicos de un laboratorio universitario (Tipo FabLab).

El requerimiento se encuentra incompleto. Por lo tanto, deberán identificar ambigüedades, definir reglas de negocio y justificar sus decisiones. Luego tendrán que implementar la solución y demostrar, mediante actividades de verificación, validción y casos de prueba, que el sistema fue construido correctamente y responde a la necesidad planteada.

La entrega considera el código fuente, documentación, matriz de trazabilidad, ejecución de pruebas, evidencias del trabajo colaborativo en GitHub.

Revisen el documento completo de la tarea para conocer todos los requisitos, entregables y criterios de evaluación. Las consultas deberán realizarse en el foro habilitado.

## 2. Ambigüedades, vacíos, riesgos y conflictos detectados

| ID | Tipo | Situación detectada | Riesgo o problema asociado | Pregunta al cliente |
|---|---|---|---|---|
| ANA-01 | Vacío | No se especifican los datos obligatorios necesarios para registrar a una persona autorizada. | Podrían registrarse usuarios sin información suficiente para identificarlos correctamente. | ¿Qué datos son obligatorios para registrar a una persona autorizada? |
| ANA-02 | Vacío | No se especifican los datos obligatorios de los equipos ni la forma de identificarlos de manera única. | Podrían existir equipos difíciles de diferenciar o identificar dentro del sistema. | ¿Qué información debe almacenarse de cada equipo y cada equipo debe poseer un identificador único? |
| ANA-03 | Vacío | No se establece una cantidad máxima de equipos que puede solicitar o mantener una persona simultáneamente. | Un solicitante podría concentrar una cantidad excesiva de equipos y afectar su disponibilidad para otros usuarios. | ¿Existe una cantidad máxima de equipos que una persona puede solicitar o mantener simultáneamente? |
| ANA-04 | Vacío | No se establece una duración máxima para los préstamos. | Un equipo podría permanecer prestado durante un período excesivamente largo. | ¿Cuál es la duración máxima permitida para un préstamo? |
| ANA-05 | Riesgo | Se contempla la existencia de préstamos atrasados, pero no se especifican las consecuencias para el solicitante. | Una persona con equipos atrasados podría continuar generando nuevas solicitudes sin restricciones. | ¿Un solicitante que mantiene un préstamo atrasado puede realizar nuevas solicitudes? |
| ANA-06 | Ambigüedad | No se establecen claramente los estados en los cuales una solicitud puede ser cancelada. | Podrían permitirse cancelaciones cuando el equipo ya fue entregado o cuando el préstamo se encuentra en una etapa que no debería admitir cancelación. | ¿Hasta qué momento puede cancelarse una solicitud y qué roles están autorizados para hacerlo? |
| ANA-07 | Vacío | No se especifica cómo deben manejarse los equipos dañados, en mantenimiento o temporalmente fuera de servicio. | Un equipo que físicamente no puede utilizarse podría aparecer como disponible para préstamo. | ¿El sistema debe considerar estados especiales para equipos en mantenimiento, dañados o fuera de servicio? |
| ANA-08 | Vacío | No se indica si un préstamo puede extender o modificar su fecha de devolución una vez aprobado o entregado. | No existe un comportamiento definido ante una solicitud de renovación o extensión de un préstamo. | ¿Está permitido renovar o extender la duración de un préstamo? |
| ANA-09 | Ambigüedad | Se permiten solicitudes de uno o más equipos, pero no se indica qué pasa si solo algunos están disponibles | No está claro si se aprueba parcialmente o se rechaza todo | ¿Qué debe ocurrir cuando una solicitud contiene varios equipos y alguno de ellos no se encuentra disponible? |


## 3. Supuestos

| Supuesto | Descripción |
|---|---|
|SUP-01| Se define un máximo de X días que se puede tener el equipo |
|SUP-02| Se define un máximo de X equipos que se pueden pedir prestados |
|SUP-03| Solo se puede reservar un equipo cuando el equipo este disponible |
|SUP-04| Si un usuario se atrasa, habrá algún tipo de penalización |
|SUP-05| La solicitud se comportara como una unidad completa |
