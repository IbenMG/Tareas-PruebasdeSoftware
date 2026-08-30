# Criterios de aceptación

## CA-01 - Inicio de sesión correcto

Dado un usuario registrado,
cuando ingrese credenciales validas,
el sistema deberá permitir el acceso segun su rol.

## CA-02 - Inicio de sesión incorrecto

Dado un usuario registrado,
cuando ingrese credenciales invalidas,
el sistema debera rechazar el acceso e informar el error.

## CA-03 - Registro de usuarios

Cuando un encargado registre una nueva persona autorizada con los datos requeridos,
el usuario deberá quedar almacenado y disponible para posteriores operaciones.

## CA-04 - Registro de equipos

Cuando un encargado registre un nuevo equipo,
el sistema debera asignarlo o asociarlo a un identificador unico
y almacenarlo correctamente.

## CA-05 - Equipo no disponible

Si un equipo se encuentra en mantenimiento o fuera de servicio,
el sistema debera impedir que sea incluido en una nueva solicitud.

## CA-06 - Limite máximo de equipos

Si un solicitante mantiene tres equipos simultaneamente,
el sistema debera impedir que obtenga un equipo adicional.

## CA-07 - Solicitud dentro del limite

Si un solicitante mantiene menos de tres equipos
y la nueva solicitud no provoca superar el maximo permitido,
el sistema debera permitir continuar con la solicitud
si se cumplen las demas reglas.

## CA-08 - Duracion maxima permitida

Una solicitud cuya duración sea igual o inferior a siete dias
podrá ser registrada si cumple las demas condiciones.

## CA-09 - Duracion excedida

Si una solicitud tiene una duracion superior a siete dias,
el sistema debera rechazarla.

## CA-10 - Prestamo atrasado

Si un solicitante mantiene al menos un prestamo atrasado,
el sistema debera impedir que genere una nueva solicitud.

## CA-11 - Solicitud con multiples equipos

Cuando una solicitud contenga varios equipos,
todos ellos deberan cumplir las condiciones necesarias para que la solicitud
pueda continuar. Si al menos uno no puede ser prestado,
la solicitud completa deberá ser rechazada.

## CA-12 - Aprobacion de solicitud

Una solicitud en estado SOLICITADA podra ser aprobada
únicamente por un encargado y siempre que cumpla las reglas de negocio.

## CA-13 - Cancelacion de solicitud

Una solicitud podra cancelarse unicamente mientras se encuentre
en estado SOLICITADA o APROBADA.

## CA-14 - Entrega de equipos

El encargado solamente podra registrar la entrega de equipos
asociados a una solicitud previamente APROBADA.

## CA-15 - Devolucion

El sistema debera permitir registrar la devolucion
únicamente de prestamos que hayan sido previamente entregados.

## CA-16 - Renovaciones

El sistema no debera permitir modificar la fecha de devolucion
con el objetivo de extender un prestamo ya aprobado o entregado.
