# Tareas-PruebasdeSoftware

# Sistema de Gestión de Préstamos de Equipos

## Tarea 1: Verificación y Validación de Software

Sistema desarrollado en Python para gestionar el préstamo de equipos tecnológicos de un laboratorio universitario.

El proyecto fue realizado como parte de la asignatura **Pruebas de Software**, con énfasis en el análisis de requerimientos, definición de reglas de negocio, trazabilidad, verificación, validación y ejecución sistemática de casos de prueba.

---

## Integrantes

| Integrante | Rol |
|---|---|
| Iben Muñoz | 202204674-0 |
| Benjamín Araos | Por completar |

---

## Descripción del proyecto

El sistema permite administrar el ciclo de préstamo de equipos de un laboratorio mediante una aplicación ejecutada desde terminal.

La solución contempla dos tipos de usuario:

- **Solicitante:** puede consultar equipos, generar solicitudes de préstamo, consultar sus préstamos y cancelar solicitudes cuando corresponda.
- **Encargado:** administra usuarios y equipos, evalúa solicitudes y registra entregas y devoluciones.

El sistema incorpora reglas de negocio para controlar aspectos como disponibilidad de equipos, duración máxima de préstamos, cantidad máxima de equipos simultáneos, atrasos, estados de solicitudes y restricciones de operación.

Los datos se almacenan localmente mediante un archivo JSON y las operaciones relevantes son registradas mediante logs.

---

### Objetivo general

Desarrollar y evaluar un sistema de gestión de préstamos que permita aplicar de manera práctica los conceptos de **verificación y validación de software**, asegurando trazabilidad entre requerimientos, criterios de aceptación, implementación y casos de prueba.

## Arquitectura del proyecto

El sistema fue dividido en componentes con responsabilidades diferenciadas:

```text
Tareas-PruebasdeSoftware/
|
|-- code/
|   |-- database/
|   |   |-- database.py
|   |   `-- datos.json
|   |
|   |-- models/
|   |   |-- equipo.py
|   |   |-- solicitud.py
|   |   `-- usuario.py
|   |
|   |-- services/
|   |   |-- autenticacion.py
|   |   |-- encargado.py
|   |   |-- prestamo_service.py
|   |   `-- solicitante.py
|   |
|   |-- app.log
|   `-- main.py
|
|-- docs/
|   |-- analisis-requerimiento.md
|   |-- estado-reglas.md
|   |-- matriz-trazabilidad.md
|   `-- verficacion-validacion.md
|
|-- tests/
|   |-- plan-pruebas.md
|   `-- test_prestamos_service.py
|
`-- README.md
```

### Responsabilidad de los componentes

| Componente | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada de la aplicación y control de autenticación por rol. |
| `autenticacion.py` | Validación de credenciales y registro de accesos. |
| `solicitante.py` | Operaciones disponibles para usuarios solicitantes. |
| `encargado.py` | Administración de usuarios, inventario y solicitudes. |
| `prestamo_service.py` | Reglas y lógica principal del proceso de préstamo. |
| `database.py` | Lectura y escritura de los datos persistentes. |
| `datos.json` | Persistencia local de usuarios, equipos y solicitudes. |
| `models/` | Representación de las entidades principales del dominio. |
| `tests/` | Planificación y ejecución de pruebas. |
| `docs/` | Documentación del proceso de análisis, trazabilidad y V&V. |

---

## Tecnologías utilizadas

- **Python 3**
- **JSON** para persistencia local
- **Logging de Python** para trazabilidad de eventos
- **Pytest** para pruebas automatizadas
- **Git** para control de versiones
- **GitHub** para colaboración, ramas, Pull Requests e historial del desarrollo
- **Markdown** para documentación técnica

La aplicación principal utiliza módulos incluidos en la biblioteca estándar de Python y no necesita una base de datos externa.

---

## Requisitos

Para ejecutar el sistema se requiere:

- Python 3.14.4 instalado.
- Git, en caso de clonar el repositorio.
- Una terminal compatible con Python.

Para las pruebas automatizadas se requiere adicionalmente `pytest`.

Se recomienda comprobar la instalación de Python mediante:

```bash
python --version
```

o:

```bash
python3 --version
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/IbenMG/Tareas-PruebasdeSoftware.git
```

### 2. Ingresar al proyecto

```bash
cd Tareas-PruebasdeSoftware
```

No es necesario instalar una base de datos ni configurar servicios externos para ejecutar la aplicación.

---

## Ejecución

Se recomienda ejecutar la aplicación desde la carpeta `code`:

```bash
cd code
```

En Windows:

```bash
python main.py
```

En sistemas donde Python se encuentre registrado como `python3`:

```bash
python3 main.py
```

Al iniciar, se mostrará el menú principal:

```text
===================================
 SISTEMA DE PRÉSTAMOS DE EQUIPOS
===================================
1. Iniciar sesión
2. Salir
```

---

## Usuarios de demostración

El repositorio incluye datos de demostración para facilitar la ejecución y las pruebas.

### Encargado

```text
Correo: encargado@lab.cl
Contraseña: admin
Rol: ENCARGADO
```

### Solicitante

```text
Correo: alumno@lab.cl
Contraseña: 1234
Rol: SOLICITANTE
```
---

## Persistencia de datos

La persistencia local se realiza en:

```text
code/database/datos.json
```

El archivo contiene tres colecciones principales:

```text
usuarios
equipos
solicitudes
```

Las modificaciones realizadas mediante la aplicación se almacenan en este archivo, permitiendo conservar el estado del sistema entre distintas ejecuciones.

No se requiere instalar un motor de base de datos externo.

---

## Registro de eventos

La aplicación utiliza el módulo `logging` de Python para registrar operaciones relevantes.

Al ejecutar el programa desde la carpeta `code`, los eventos son almacenados en:

```text
code/app.log
```

---

## Flujo general de funcionamiento

El funcionamiento general puede representarse de la siguiente forma:

```text
Inicio
  |
  v
Autenticación
  |
  +-----------------------+
  |                       |
  v                       v
SOLICITANTE            ENCARGADO
  |                       |
  |                       +--> Administración de usuarios
  |                       |
  |                       +--> Administración de equipos
  |                       |
  +--> Consultar catálogo +--> Aprobar/Rechazar solicitudes
  |
  +--> Crear solicitud    +--> Registrar entrega
  |
  +--> Mis préstamos      +--> Registrar devolución
  |
  +--> Cancelar
```

La lógica central de préstamo es gestionada por `PrestamoService`.

---

## Flujo de una solicitud

Un flujo exitoso típico corresponde a:

```text
Usuario autenticado
        |
        v
Selecciona equipos
        |
        v
Validación de reglas
        |
        v
    SOLICITADA
        |
        v
     APROBADA
        |
        v
     ENTREGADA
        |
        v
     DEVUELTA
```

Si las reglas de negocio no se cumplen, la operación debe ser rechazada y el sistema debe informar el motivo correspondiente.

---

Proyecto desarrollado para la asignatura **Pruebas de Software**.
