# Análisis del requerimiento

## 1. Ambigüedades, vacíos, riesgos y conflictos detectados

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


## 2. Supuestos
Se generan preguntas y supuestos para avanzar en el análisis.

**¿Cómo se ingresarán los equipos al sistema?**
    
  - **SUP-01:** Se asume que cada equipo físico será registrado individualmente en el sistema, permitiendo identificar de manera única cada unidad.

**¿El Encargado es la máxima autoridad del sistema?**
    
  - **SUP-02:** Se asume que el encargado tiene autoridad total para administrar usuarios, equipos y solicitudes, sin necesidad de crear roles administrativos adicionales.
    
**¿La aplicación debe sincronizarse con algún servidor de hora externo?**
    
  - **SUP-03:** Al ser una aplicación local, se asume que la fecha y hora del sistema operativo donde se ejecuta son correctas y no serán manipuladas para evitar atrasos.
    
**Si alguien pide más de un equipo, ¿debe devolverlos todos juntos?**
    
  - **SUP-04:** Se asume que los préstamos que incluyen un conjunto de equipos se tratan como una unidad indivisible y deben devolverse al mismo tiempo (no hay devoluciones parciales).

## 3. Requerimiento Mejorado

El laboratorio universitario necesita una aplicación, protegida mediante inicio de sesión, para gestionar el préstamo de equipos tecnológicos. 
El sistema deberá soportar dos roles: **Solicitantes**  y **Encargados**.

Los **Solicitantes** podrán consultar el catálogo de equipos, crear solicitudes (por un máximo de 3 equipos y una duración límite de 7 días), consultar sus préstamos y cancelar solicitudes siempre y cuando el equipo no haya sido entregado. El sistema bloqueará la creación de nuevas solicitudes a usuarios que posean devoluciones atrasadas.

Los **Encargados** administrarán a los usuarios y el estado del inventario (incluyendo equipos en mantenimiento). Además, serán los responsables de aprobar o rechazar las solicitudes entrantes, registrar las entregas físicas y las devoluciones. Todas las operaciones críticas generarán un log de eventos. No se contemplan notificaciones por correo ni renovaciones de préstamos.

## 4. Regla de negocios, alcance y exclusiones

### Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Un solicitante podrá mantener como máximo 3 equipos simultáneamente. |
| RN-02 | La duración máxima de un préstamo será de 7 días. |
| RN-03 | Un solicitante con préstamos atrasados no podrá realizar nuevas solicitudes. |
| RN-04 | Una solicitud con varios equipos será tratada como una unidad completa. |
| RN-05 | Una solicitud podrá cancelarse mientras se encuentre solicitada o aprobada. |
| RN-06 | Una solicitud entregada no podrá cancelarse y deberá finalizar mediante devolución. |
| RN-07 | Un equipo en mantenimiento o fuera de servicio no podrá ser solicitado. |
| RN-08 | No se permitirán renovaciones de préstamos. |

### Alcance
La aplicación podrá permitir:

- Registrar personas autorizadas.
- Registrar y consultar equipos.
- Crear solicitudes de préstamo.
- Aprobar o rechazar solicitudes.
- Cancelar solicitudes cuando corresponda.
- Registrar entrega y devolución de equipos.
- Consultar préstamos vigentes, futuros y atrasados.
- Registrar eventos relevantes mediante logs.

### Exclusiones
La aplicación no podrá:

- Notificar por correo electrónico
- Renovar equipos
- Hacer una reserva parcial con múltiples equipos

## 5. Criterios de aceptación


| **CA-ID** | **Descripción**|
| --- | --- |
| CA-01     | **Dado** que un usuario intenta realizar una operación en el sistema, **Cuando** no ha iniciado sesión con credenciales válidas y un rol definido, **Entonces** el sistema debe denegar el acceso y solicitar la autenticación.                                                                 |
| CA-02     | **Dado** que un solicitante está creando una nueva reserva, **Cuando** la solicitud excede los 7 días de duración o incluye más de 3 equipos, **Entonces** el sistema debe rechazar la creación y mostrar un mensaje indicando el límite excedido.                                              |
| CA-03     | **Dado** que un solicitante posee al menos un préstamo en estado "ATRASADO", **Cuando** intente acceder a la opción de crear nuevas solicitudes, **Entonces** el sistema debe bloquear la acción advirtiendo que aun tiene entregas atrasadas pendientes.                                                           |
| CA-04     | **Dado** que un encargado intenta aprobar una solicitud que incluye múltiples equipos, **Cuando** al menos uno de los equipos solicitados no se encuentra disponible, **Entonces** el sistema debe impedir la acción y rechazar la solicitud por completo, sin permitir aprobaciones parciales. |
| CA-05     | **Dado** que una solicitud de préstamo ha pasado al estado "ENTREGADO", **Cuando** el usuario (solicitante o encargado) revise las acciones disponibles para dicha solicitud, **Entonces** el sistema debe ocultar o bloquear la opción de "Cancelar".                                          |
| CA-06     | **Dado** que un encargado ha marcado el estado físico de un equipo como "En mantenimiento", **Cuando** el sistema calcule la disponibilidad general para nuevas solicitudes, **Entonces** ese equipo será removido automáticamente del conteo de unidades disponibles.                          |

