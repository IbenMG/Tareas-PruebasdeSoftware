# Diferencia

## Verificación:

"**¿Estamos construyendo correctamente el producto especificado?**" 
Comprobar que el código y la lógica de la aplicación cumplen con nuestras Reglas de Negocio (RN) y Criterios de Aceptación (CA). Por ejemplo, asegurarnos de que si una variable sobrepasa el número 3, el código lance un error (cumpliendo la RN-01), o que los datos persistan correctamente en un archivo.

## Validación: 
 **"¿Estamos construyendo el producto que realmente se necesita?"**
 Comprobar que nuestra aplicación resuelve el problema real. Por más que el código esté perfecto, si el _Encargado_ encuentra que la interfaz de la consola es confusa o muy lenta para registrar una entrega rápida entre clases, el producto fracasó. Validar es simular el entorno y confirmar que la solución es verdaderamente funcional para los usuarios finales.

# Actividades
## Verificación

| **ID**     | **Objetivo**                                                                                                                              | **Responsable** | **Evidencia**                                                                   | **Resultado** | **Conclusión** |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------- | ------------- | -------------- |
| **VER-01** | Comprobar mediante pruebas unitarias que la lógica rechaza préstamos de > 3 equipos o > 7 días.                                           |                 | Captura de pantalla mostrando el mensaje de error al exceder el límite. |               |                |
| **VER-02** | Verificar el correcto manejo de excepciones ante ingresos inválidos en la terminal (ej. escribir letras en vez de IDs numéricos).         |                 | Captura del mensaje de error controlado (sin que el programa sufra un error. |               |                |
| **VER-03** | Verificar, mediante revisión de código estático, que la solicitud se trata como indivisible y no existen métodos de "devolución parcial". |                 | Enlace al fragmento de código revisado. |               |                |
| **VER-04** | Comprobar que los datos (usuarios, equipos, estados) se guardan y recuperan íntegramente desde el archivo local de persistencia.          |                 | Archivo local antes y después de cerrar el programa.                 |               |                |
| **VER-05** | Asegurar que los logs registran correctamente los eventos de inicio de sesión fallidos sin exponer contraseñas.                           |                 | Archivo `.log` generado.                             |               |                |

## Validación

| **ID**     | **Objetivo**                                                                                                                                                  | **Responsable** | **Evidencia**                                                                  | **Resultado** | **Conclusión** |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------ | ------------- | -------------- |
| **VAL-01** | Comprobar si el sistema es lo suficientemente rápido y ágil para el Encargado cuando hay varios estudiantes seguidos esperando retirar equipos.                            |                 | Registro del tiempo que toma entregar 5 equipos seguidos.                      |               |                |
| **VAL-02** | Confirmar que cualquier usuario nuevo pueda usar el programa y entender qué hacer solo leyendo la pantalla, sin necesitar un manual de instrucciones.                      |                 | Capturas mostrando mensajes claros como "Presione 1 para volver".              |               |                |
| **VAL-03** | Asegurar que, si queda solo 1 equipo disponible en el laboratorio, el sistema impida que varios estudiantes lo reserven al mismo tiempo.                                   |                 | Demostración de que la primera reserva es exitosa y las demás rebotan.         |               |                |
| **VAL-04** | Comprobar que la pantalla de "Atrasos" le entregue al Encargado exactamente la información que necesita rápido (quién tiene el equipo y cuántos días de atraso).           |                 | Pantallazo del listado de deudores mostrándose ordenado.                       |               |                |
| **VAL-05** | Simular el ciclo de vida de un equipo real en el laboratorio (se presta, se daña, se arregla, se vuelve a prestar) para confirmar que el programa sirve para el día a día. |                 | Historial de un equipo pasando por todos los estados posibles en la vida real. |               |                |
