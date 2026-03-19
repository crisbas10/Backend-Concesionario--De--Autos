#  Backend Concesionario de Autos

##  Descripción del Proyecto

Este proyecto consiste en el desarrollo de un backend para la gestión de un concesionario de autos, implementado en Python utilizando SQLAlchemy como ORM y una base de datos relacional (Neon/PostgreSQL o SQLite).

El sistema permite administrar la información relacionada con usuarios, clientes, empleados, vehículos, ventas, métodos de pago y mantenimientos, aplicando operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre cada entidad.

---

##  Objetivo

Desarrollar una aplicación backend estructurada y modular que permita simular el funcionamiento de un concesionario, cumpliendo con los requisitos del examen 3:

* Modelado de entidades
* Relaciones entre tablas
* Implementación de CRUD
* Uso de ORM (SQLAlchemy)
* Conexión a base de datos
* Buenas prácticas de organización del código

---

##  Estructura del Proyecto

```
src/
 ├── entities/        # Modelos de la base de datos
 ├── databases/       # Conexión a la base de datos
 ├── crud/            # Operaciones CRUD
 └── main.py          # Ejecución principal
```

---

##  Entidades del Sistema

El sistema está compuesto por las siguientes entidades:

*  Usuario (control de acceso y auditoría)
*  Cliente
*  Empleado
*  Vehículo
*  Venta
*  Método de Pago
*  Mantenimiento

---

##  Relaciones

* Un cliente puede realizar varias ventas
* Un vehículo puede ser vendido
* Una venta está asociada a un cliente, vehículo y método de pago
* Los registros incluyen auditoría mediante usuario de creación y edición

---

##  Tecnologías Utilizadas

* Python 
* SQLAlchemy
* PostgreSQL (Neon) / SQLite
* dotenv
* Alembic (opcional para migraciones)

---

##  Instalación y Ejecución

1. Clonar el repositorio:

```
git clone <URL_DEL_REPOSITORIO>
```

2. Instalar dependencias:

```
python -m pip install sqlalchemy psycopg2-binary python-dotenv
```

3. Crear archivo `.env` en la raíz:

```
DATABASE_URL=tu_url_de_base_de_datos
```

4. Ejecutar el proyecto:

```
python -m src.entities.main
```

---

## Funcionalidades (CRUD)

El sistema permite:

*  Crear registros
*  Consultar datos
*  Actualizar información
*  Eliminar registros

---

##  Pruebas

Las operaciones CRUD se ejecutan desde el archivo `main.py`, donde se:

* Insertan datos de prueba
* Se actualizan registros
* Se eliminan datos
* Se muestran resultados en consola

---

## Resultados Esperados

* Creación automática de tablas en la base de datos
* Persistencia de datos
* Correcta ejecución de operaciones CRUD


##  Notas Finales

Este proyecto cumple con los requisitos establecidos en el examen 3, aplicando conceptos de bases de datos, programación orientada a objetos y desarrollo backend con Python.
##  Video de Demostración

Puedes ver la explicación del proyecto en el siguiente enlace:

 https://www.youtube.com/tu-video
