# Administrador de Biblioteca Universitaria 📚

Este proyecto consiste en el desarrollo de un programa para la administración del catálogo de libros de una biblioteca universitaria. Fue desarrollado como el **Proyecto 1** para la asignatura de **Estructura y Representación de Datos** en la **Universidad Tecnológica de Panamá**.

## 🎯 Objetivo
El objetivo principal es aplicar conceptos fundamentales de programación y estructuras de datos para gestionar un inventario de libros:
* Manejo de **Cadenas de caracteres**.
* Uso de **Arreglos**.
* Implementación de **Registros (estructuras de datos)**.

## 🛠️ Especificaciones Técnicas

### Estructura del Registro (Libro)
Cada libro está representado por la siguiente estructura de datos:

| Campo | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| **Título** | Cadena | Nombre del libro. |
| **Autor** | Cadena | Nombre del autor. |
| **Año** | Entero | Año de publicación. |
| **Categoría** | Cadena | Género o área del conocimiento. |
| **ISBN** | Cadena | Código de hasta 13 dígitos. |

*El sistema tiene una capacidad máxima de almacenamiento de **50 libros** mediante un arreglo de registros.*

### Funcionalidades del Programa
1. **Agregar libro:** Permite el registro de nuevos ejemplares en el sistema.
2. **Buscar libro:** Búsqueda por título o autor (coincidencias exactas o parciales).
3. **Listar libros:** Visualización de todos los libros registrados en formato tabular.
4. **Filtrar:** Clasificación de libros por año específico o por categoría.
5. **Editar:** Modificación de los campos de un libro existente mediante su ISBN.

## 📋 Requisitos de Validación
Para garantizar la integridad de los datos, el programa realiza las siguientes validaciones:
* **Campos obligatorios:** El título, autor, categoría e ISBN no pueden estar vacíos.
* **Validación de año:** El año de publicación debe ser un número entero dentro de un rango lógico.
* **Mensajería:** El sistema emite mensajes claros de éxito, error o advertencia según el resultado de las operaciones.

## 📂 Entrega y Formato
* **Lenguajes permitidos:** C (.c), C++ (.cpp) o Java (.java).
* **Documentación:** Incluye un informe en PDF con el código debidamente documentado.
* **Fecha de entrega:** Segunda semana de junio de 2025.

---
**Profesora:** Crispina Ramos S.  
**Periodo:** I Semestre de 2025  
**Institución:** Universidad Tecnológica de Panamá