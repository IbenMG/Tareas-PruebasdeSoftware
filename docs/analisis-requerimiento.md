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

El sistema deberá permitir gestionar, mediante una aplicación ejecutada por terminal, el préstamo de equipos tecnológicos pertenecientes a un laboratorio universitario. El acceso estará protegido mediante autenticación, existiendo al menos dos roles: **Solicitantes** y **Encargados**.

Los **Solicitantes** podrán consultar el catálogo de equipos, gestionar sus propias solicitudes y consultar sus préstamos (vigentes, futuros y atrasados). Podrán crear solicitudes por un máximo de 3 equipos simultáneos y una duración límite de 7 días, las cuales serán tratadas siempre como una unidad completa indivisible. Podrán cancelar solicitudes mientras estén en estado SOLICITADA o APROBADA. El sistema bloqueará automáticamente la creación de nuevas solicitudes a los usuarios que posean devoluciones atrasadas.

Los **Encargados** administrarán a los usuarios y el inventario. Cada equipo será registrado individualmente con un identificador único y un estado operativo (los equipos en mantenimiento o fuera de servicio no podrán ser solicitados). Además, serán responsables de aprobar o rechazar solicitudes entrantes, registrar entregas físicas y devoluciones. Una vez registrada la entrega, el ciclo deberá finalizar obligatoriamente mediante devolución.

El sistema registrará mediante logs los eventos relevantes y errores ocurridos durante su ejecución. No se permitirán renovaciones de préstamos, notificaciones por correo electrónico, ni aprobaciones parciales de solicitudes con múltiples equipos.

### Desglose

Los siguientes requisitos funcionales descomponen el requerimiento mejorado con el objetivo de facilitar su implementación, verificación, validación y trazabilidad.

|**ID**|**Requisito funcional**|
|---|---|
|**RQ-01**|El sistema deberá autenticar a los usuarios mediante sus credenciales.|
|**RQ-02**|El encargado deberá poder registrar personas autorizadas.|
|**RQ-03**|El encargado deberá poder registrar equipos individualmente.|
|**RQ-04**|El sistema deberá permitir consultar los equipos y su estado.|
|**RQ-05**|El solicitante deberá poder crear solicitudes para uno o más equipos.|
|**RQ-06**|El sistema deberá impedir superar el máximo de tres equipos simultáneos.|
|**RQ-07**|El sistema deberá impedir préstamos cuya duración supere siete días.|
|**RQ-08**|El encargado deberá poder aprobar o rechazar solicitudes.|
|**RQ-09**|El sistema deberá permitir cancelar solicitudes únicamente en los estados permitidos.|
|**RQ-10**|El encargado deberá poder registrar la entrega de una solicitud aprobada.|
|**RQ-11**|El encargado deberá poder registrar la devolución de un préstamo entregado.|
|**RQ-12**|El sistema deberá impedir nuevas solicitudes de usuarios con préstamos atrasados.|
|**RQ-13**|El sistema deberá impedir solicitar equipos en mantenimiento o fuera de servicio.|
|**RQ-14**|Las solicitudes con varios equipos deberán procesarse como una unidad completa.|
|**RQ-15**|El sistema deberá permitir consultar préstamos vigentes, futuros y atrasados.|
|**RQ-16**|El sistema deberá registrar eventos relevantes y errores mediante logs.|
|**RQ-17**|El sistema no deberá permitir renovar o extender un préstamo aprobado o entregado.|


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

| **ID**    | **Descripción**                                                                                                                                                                                                                                                                                           |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CA-01** | **Dado** un usuario registrado en el sistema, **Cuando** ingrese credenciales válidas, **Entonces** el sistema deberá permitir el acceso según su rol (Solicitante o Encargado).                                                                                                                          |
| **CA-02** | **Dado** que un usuario intenta realizar una operación, **Cuando** no ha iniciado sesión o ingresa credenciales inválidas, **Entonces** el sistema debe denegar el acceso, solicitar autenticación e informar el error.                                                                                   |
| **CA-03** | **Dado** que un encargado necesita habilitar a una persona, **Cuando** registre a un nuevo usuario con los datos requeridos, **Entonces** este quedará almacenado y disponible para posteriores operaciones.                                                                                              |
| **CA-04** | **Dado** que un encargado ingresa nuevo inventario, **Cuando** registre un nuevo equipo, **Entonces** el sistema deberá asignarle un identificador único y almacenarlo correctamente.                                                                                                                     |
| **CA-05** | **Dado** que un solicitante está creando una reserva, **Cuando** la solicitud provoque que supere el máximo de 3 equipos simultáneos, **Entonces** el sistema debe rechazar la creación e indicar el límite excedido.                                                                                     |
| **CA-06** | **Dado** que un solicitante está creando una reserva, **Cuando** la solicitud exceda los 7 días de duración, **Entonces** el sistema debe rechazar la creación e indicar el límite excedido.                                                                                                              |
| **CA-07** | **Dado** que un solicitante posee al menos un préstamo en estado "ATRASADO", **Cuando** intente acceder a la opción de crear nuevas solicitudes, **Entonces** el sistema debe bloquear la acción advirtiendo que se encuentra moroso.                                                                     |
| **CA-08** | **Dado** que un equipo ha sido marcado como "En mantenimiento" o "Fuera de servicio", **Cuando** el sistema calcule la disponibilidad para nuevas solicitudes, **Entonces** ese equipo será removido automáticamente e impedirá su reserva.                                                               |
| **CA-09** | **Dado** que un encargado intenta aprobar una solicitud que incluye múltiples equipos, **Cuando** al menos uno no se encuentre disponible, **Entonces** el sistema debe impedir la acción y rechazar la solicitud por completo (sin aprobaciones parciales).                                              |
| **CA-10** | **Dado** que una solicitud se encuentra en estado "SOLICITADA", **Cuando** un encargado intente evaluarla, **Entonces** solo podrá aprobarla si cumple estrictamente todas las reglas de negocio.                                                                                                         |
| **CA-11** | **Dado** que una solicitud ha pasado al estado "ENTREGADO", **Cuando** el usuario revise las acciones disponibles, **Entonces** el sistema debe ocultar o bloquear la opción de "Cancelar" (solo permitida en estado SOLICITADA o APROBADA).                                                              |
| **CA-12** | **Dado** que un encargado intenta registrar la entrega física de los equipos, **Cuando** la solicitud asociada no esté previamente "APROBADA", **Entonces** el sistema impedirá el registro.                                                                                                              |
| **CA-13** | **Dado** que un encargado intenta registrar una devolución, **Cuando** los préstamos correspondientes no hayan sido previamente "ENTREGADOS", **Entonces** el sistema deberá impedir la operación.                                                                                                        |
| **CA-14** | **Dado** que un préstamo ya se encuentra "APROBADO" o "ENTREGADO", **Cuando** un usuario intente modificar la fecha de devolución, **Entonces** el sistema no deberá permitir la renovación.                                                                                                              |
| **CA-15** | **Dado** que un usuario o el sistema ejecuta una operación errónea (ej. inicio de sesión fallido, aprobación, entrega o devolución), **Cuando** la transacción finalice, **Entonces** el sistema deberá registrar automáticamente el evento mediante logs para asegurar la trazabilidad de los registros. |
| **CA-16** | **Dado** que un solicitante autenticado selecciona uno o más equipos disponibles y cumple todas las reglas de negocio, **Cuando** cree una solicitud de préstamo, **Entonces** el sistema deberá registrarla correctamente en estado "SOLICITADA". |
| **CA-17** | **Dado** que un solicitante autenticado desea conocer los equipos del laboratorio, **Cuando** consulte el catálogo, **Entonces** el sistema deberá mostrar los equipos registrados junto con su identificador, nombre y estado actual. |
| **CA-18** | **Dado** que un solicitante autenticado posee solicitudes o préstamos registrados, **Cuando** consulte sus préstamos, **Entonces** el sistema deberá mostrar únicamente los registros asociados a dicho usuario, incluyendo equipos, fechas y estado. |
