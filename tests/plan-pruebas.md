# Plan de Pruebas

## Iben Muñoz

| ID | Descripción | Estado | Link a la prueba |
|---|---|---|---|
| **TC-01** | Verificar inicio de sesión correcto con credenciales válidas de un solicitante. |  ✓ |[Ver evidencia](evidencias-testing1-10/TC-01.png/)|
| **TC-02** | Verificar que se rechace el inicio de sesión con contraseña incorrecta. |  ✓ |[Ver evidencia](evidencias-testing1-10/TC-02.png/)|
| **TC-03** | Verificar la creación correcta de una solicitud válida con equipos disponibles. | ✓ |[Ver evidencia](evidencias-testing1-10/TC-03.png/)|
| **TC-04** | Verificar que se rechace una solicitud de más de 3 equipos simultáneos. |  ✓ |[Ver evidencia](evidencias-testing1-10/TC-04.png/)|
| **TC-05** | Verificar que un usuario con 2 equipos activos no pueda solicitar otros 2, ya que superaría el máximo permitido. | ✓ |[Ver evidencia](evidencias-testing1-10/TC-05.png/)|
| **TC-06** | Verificar que un equipo en estado `MANTENIMIENTO` no pueda ser incluido en una nueva solicitud de préstamo. | ✓ |[Ver evidencia](evidencias-testing1-10/TC-06.png/)|
| **TC-07** | Verificar que un usuario con un préstamo atrasado no pueda crear una nueva solicitud. | ✓ |[Ver evidencia](evidencias-testing1-10/TC-07.png/)|
| **TC-08** | Verificar que una solicitud múltiple sea rechazada completamente si uno de los equipos está en mantenimiento o no disponible. | ✓ |[Ver evidencia](evidencias-testing1-10/TC-08.png/)|
| **TC-09** | Verificar que un encargado pueda registrar correctamente un nuevo usuario SOLICITANTE o ENCARGADO. | ✓ |[Ver evidencia](evidencias-testing1-10/TC-09.png/)|
| **TC-10** | Verificar que se rechace el registro de un usuario cuando faltan datos obligatorios. | ✓ |[Ver evidencia](evidencias-testing1-10/TC-10.png/)|

## Benjamin Araos

El archivo [Ver captura](../tests/validacion.py) contiene pruebas automatizadas construida con **Pytest** para validar los casos **TC-11 al TC-20**. Su objetivo es comprobar que el código cumple con las reglas de negocio. Aisla las pruebas, evitando modificar los datos del entorno real.

**Instrucciones de Ejecución** Asegúrate de tener Pytest instalado. Ubícate en la carpeta raíz del proyecto desde tu terminal y utiliza los siguientes comandos:

- **Para ejecutar todas las pruebas a la vez:**
    ```
    py -m pytest tests/test.py -v
    ```
- **Para ejecutar una prueba específica (ej. test_11):** 
    ```
    py -m pytest "tests/test.py::test_11" -v
    ```


| ID | Descripción | Estado |Link a la prueba |
|---|---|---|---|
| **TC-11** | Verificar que un encargado pueda registrar correctamente un nuevo equipo y que este quede inicialmente disponible.       | PASSED     | [Ver captura](../tests/evidencias-testing11-20/test11.jpg)       |
| **TC-12** | Verificar que una solicitud válida en estado `SOLICITADA` pueda ser aprobada.                                            | PASSED     | [Ver captura](../tests/evidencias-testing11-20/test12.jpg)       |
| **TC-13** | Verificar que una solicitud en estado `SOLICITADA` pueda ser rechazada por el encargado.                                 | PASSED     | [Ver captura](../tests/evidencias-testing11-20/test13_14_15.jpg) |
| **TC-14** | Verificar que una solicitud pueda cancelarse únicamente en los estados permitidos y no después de ser entregada.         | PASSED     | [Ver captura](../tests/evidencias-testing11-20/test13_14_15.jpg) |
| **TC-15** | Verificar el flujo completo `SOLICITADA → APROBADA → ENTREGADA → DEVUELTA` y la actualización del estado de los equipos. | PASSED     | [Ver captura](../tests/evidencias-testing11-20/test13_14_15.jpg) |
| **TC-16** | Verificar que no pueda aprobarse una solicitud si uno de sus equipos pasa a mantenimiento antes de la aprobación.        | PASSED     | [Ver captura](../tests/evidencias-testing11-20/test16_17_18.jpg) |
| **TC-17** | Verificar que no sea posible renovar o extender la fecha de devolución de un préstamo aprobado o entregado.              | PASSED     | [Ver captura](../tests/evidencias-testing11-20/test16_17_18.jpg) |
| **TC-18** | Verificar que las operaciones relevantes del sistema queden registradas en `app.log`.                                    | PASSED     | [Ver captura](../tests/evidencias-testing11-20/test16_17_18.jpg) |
| **TC-19** | Verificar que el solicitante pueda consultar el catálogo mostrando ID, nombre y estado de los equipos.                   | PASSED     | [Ver captura](../tests/evidencias-testing11-20/test19_20.jpg)    |
| **TC-20** | Verificar que un solicitante pueda consultar únicamente sus propios préstamos y solicitudes.                             | PASSED     | [Ver captura](../tests/evidencias-testing11-20/test19_20.jpg)    |