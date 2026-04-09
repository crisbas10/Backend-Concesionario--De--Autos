#  Proyecto API REST con FastAPI

##  Descripción

Este proyecto consiste en la integración de una API REST utilizando **FastAPI** sobre un proyecto base que ya cuenta con ORM. La aplicación está diseñada para exponer endpoints que permiten realizar operaciones CRUD completas sobre las entidades del sistema.

La ejecución principal de la aplicación está orientada a la API desde el archivo `main`.

---

##  Objetivo

Integrar una API REST con FastAPI sobre el proyecto existente con ORM, permitiendo la gestión de entidades mediante endpoints documentados y probados.

---

##  Tecnologías utilizadas

* Python
* FastAPI
* Uvicorn
* ORM (del proyecto base)
* Swagger (documentación automática)

---

##  Requerimientos implementados

 Uso del proyecto base con ORM

 Implementación de API con FastAPI

 Ejecución del servidor con Uvicorn

 Configuración principal centralizada en `main`

 Documentación automática con Swagger

 Implementación de endpoints CRUD por cada entidad:

* GET lista
* GET por ID
* POST (crear)
* PUT (actualizar)
* DELETE (eliminar)

---

##  Ejecución del proyecto

1. Instalar dependencias:

```bash
pip install fastapi uvicorn
```

2. Ejecutar el servidor:

```bash
uvicorn main:app --reload
```

3. Acceder a la documentación Swagger:

```
http://127.0.0.1:8000/docs
```

---

##  Funcionalidades principales

* Creación de registros
* Consulta de registros
* Actualización de información
* Eliminación de registros
* Persistencia de datos mediante ORM

---

##  Pruebas

Las pruebas se realizaron mediante Swagger, verificando:

* Creación correcta de registros
* Edición de datos
* Eliminación de registros
* Consulta por ID y listado general

---

##  Evidencia en video

El video evidencia:

* Ejecución del servidor con Uvicorn
* Uso de Swagger para pruebas
* Funcionamiento de todos los endpoints
* Verificación de operaciones en base de datos (Neon):

  * Registro creado
  * Registro actualizado
  * Registro eliminado


---

##  Estructura del proyecto (general)

```
project/
│── main.py
│── models/
│── routes/
│── schemas/
│── database/
```

---

##  Conclusión

Se logró integrar correctamente una API REST con FastAPI sobre un proyecto existente con ORM, permitiendo la gestión completa de entidades mediante endpoints bien definidos y documentados automáticamente con Swagger.

El sistema cumple con todos los requerimientos del taller y permite validar las operaciones directamente sobre la base de datos.

---

##  Autores

* Sebastian Chavarria Rojas
* Alejandro Patiño Rendón
* Daniela Giraldo Gino
Link del video (Canva):
https://canva.link/rgfhu5cwfcuwyj0

