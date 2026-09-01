# Reflexion

## Benjamin

Aquí tienes una propuesta estructurada para responder las preguntas de tu reflexión final, basándonos directamente en los documentos de tu repositorio y en los desafíos técnicos que resolvimos al programar las pruebas.

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



### 2. La prueba más útil y mitigación de riesgos



### 3. Fallos detectados y correcciones



### 4. Aporte del compañero/a


### 5. Riesgos latentes en el sistema



### 6. Aprendizaje sobre Verificar vs. Validar

