# Reflexion

## Benjamin

### 1. Ambigüedades en el diseño

La ambigüedad que más influyó en el diseño fue la **ANA-09**, ya que no indicaba qué hacer si una solicitud contenía varios equipos y solo algunos estaban disponibles. por lo que se realizo luego un supuesto para poder trabajar en base a la ambigüedad.

### 2. La prueba más útil y mitigación de riesgos

La prueba más útil fue la automatización del **TC-16**, la cual verifica que no se pueda aprobar una solicitud si uno de sus equipos pasa a mantenimiento antes de la aprobación. Esta prueba permitió que no se produzcan errores, como prestar un equipo que esta inhabilitado.

### 3. Fallos detectados y correcciones

Durante la etapa de validación, específicamente hacer la **VAL-04**, se detecto que aunque el código cumplía las reglas, carecía de una vista que le entregara  información de los atrasos de manera rápida. Corregimos esto desarrollando e integrando la nueva función `consultar_atrasos` directamente en la vista del menú del Encargado.

### 4. Aporte del compañero/a

El trabajo de Iben fue muy importante para establecer la base del control de calidad. Iben ejecutó los Casos de Prueba manuales **TC-01 al TC-10**, y definió las actividades de verificación estructurales (VER-01 a VER-05). Lo que permitio conluir que el sistema manejaba correctamente las excepciones (VER-02). Esto permitio automatizar los flujos avanzados (TC-11 al TC-20) con Pytest.

### 5. Riesgos latentes en el sistema

El sistema actual es vulnerable a fallos de concurrencia. Debido a que la persistencia se maneja leyendo y sobreescribiendo un archivo local (`datos.json`), si varios Solicitantes y Encargados intentan registrar operaciones exactamente en el mismo milisegundo, el archivo podría sufrir pérdida de datos o sobrescrituras.

### 6. Aprendizaje sobre Verificar vs. Validar

Aprendí que **Verificar** esta ligado con que el software se construyó correctamente cumpliendo los requisitos y reglas de negocio. En cambio, **Validar** es comprobar si ese producto es verdaderamente útil para lo que realiza el cliente. 

## Iben

### 1. Ambigüedades en el diseño

Se presentó con la regla de duración máxima de 7 días. Desde la interfaz el sistema asignaba automáticamente una duración de 7 días, por lo que no existía una forma manual de intentar solicitar un préstamo de más de 7 días. Esto hizo necesario diferenciar entre las pruebas que podían realizarse desde la interfaz y aquellas que debían comprobarse directamente sobre la lógica del sistema. Otra ambiguedad presente fue la **ANA-09** también tuvo importancia durante las pruebas, ya que inicialmente no estaba definido qué debía ocurrir cuando una solicitud contenía varios equipos y solamente algunos de ellos estaban disponibles. Se decidió tratar cada solicitud como una unidad completa, de modo que si un equipo no cumple las condiciones, la solicitud completa debe ser rechazada.

### 2. La prueba más útil y mitigación de riesgos
La prueba más útil fue el **TC-03**, ya que permitió detectar que un equipo seguía `DISPONIBLE` después de ser solicitado. Esto permitió corregir su estado y evitar que pudiera ser solicitado nuevamente.

### 3. Fallos detectados y correcciones
Durante la ejecución de los casos de prueba y las actividades de validación se detectaron distintos problemas que permitieron mejorar la implementación:

1. **Estado incorrecto del equipo después de crear una solicitud.**  
   Durante el **TC-03** se detectó que la solicitud se registraba en estado `SOLICITADA`, pero el equipo continuaba apareciendo como `DISPONIBLE`. Esto generaba el riesgo de que el mismo equipo pudiera ser solicitado nuevamente. Se corrigió el manejo de estados para que el equipo reflejara correctamente que se encontraba solicitado.
 2.**Validación del límite de equipos simultáneos.**  
   Durante las pruebas relacionadas con el máximo de tres equipos, especialmente los escenarios de **TC-04 y TC-05**, se revisó que el sistema no solamente considerara los equipos de la nueva solicitud, sino también los préstamos activos que ya poseía el usuario. Esto permitió reforzar la lógica encargada de controlar el límite máximo permitido.


### 4. Aporte del compañero/a

El aporte de Benjamín fue importante para mejorar el enfoque general del desarrollo. Durante una etapa del proyecto se revisó nuevamente la forma en que estaba estructurado el sistema y Benjamín realizó mejoras sobre distintas partes del código, permitiendo que la implementación quedara mejor orientada hacia las reglas de negocio y las pruebas que posteriormente debíamos ejecutar.

Este trabajo ayudó a ordenar y mejorar la base del código antes de continuar con la etapa principal de testing.

Posteriormente, mientras yo me enfoqué principalmente en la ejecución manual de los casos **TC-01 al TC-10** y en las actividades de verificación **VER-01 a VER-05**, Benjamín trabajó en los casos **TC-11 al TC-20**, incluyendo la automatización de pruebas mediante `pytest` y parte de las actividades de validación.

Esta división permitió combinar pruebas manuales del funcionamiento del sistema con pruebas automatizadas de escenarios más específicos y avanzados.
### 5. Riesgos latentes en el sistema

Uno de los principales riesgos que todavía presenta el sistema es el mecanismo de persistencia mediante el archivo local `datos.json`.

Para el alcance académico del proyecto esta solución es suficiente, pero en un sistema utilizado simultáneamente por varias personas podrían producirse problemas de concurrencia. Por ejemplo, si dos usuarios realizan operaciones al mismo tiempo, ambas podrían leer una versión anterior del archivo y posteriormente sobrescribir los cambios realizados por la otra operación.

También existe el riesgo de que una inconsistencia entre el estado de una solicitud y el estado de sus equipos produzca comportamientos incorrectos. Por esta razón fue importante reforzar durante las pruebas las transiciones entre estados como `DISPONIBLE`, `SOLICITADO` y `PRESTADO`.

En una implementación destinada a un entorno real sería recomendable utilizar una base de datos con mecanismos de transacción y control de concurrencia.

### 6. Aprendizaje sobre Verificar vs. Validar

Aprendí que **verificar** consiste en comprobar que el sistema cumple correctamente los requerimientos y reglas definidas, mientras que **validar** busca comprobar que el sistema realmente sea útil y adecuado para las necesidades del usuario.
