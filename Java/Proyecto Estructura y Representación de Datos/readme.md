# Administrador de Biblioteca Universitaria 📚

Este proyecto consiste en el desarrollo de un programa para la administración del catálogo de libros de una biblioteca universitaria. [cite_start]Fue desarrollado como el **Proyecto 1** para la asignatura de **Estructura y Representación de Datos** en la **Universidad Tecnológica de Panamá**[cite: 1, 2, 3].

## 🎯 Objetivo
[cite_start]El objetivo principal es aplicar conceptos fundamentales de programación y estructuras de datos para gestionar un inventario de libros[cite: 5, 7, 8]:
* [cite_start]Manejo de **Cadenas de caracteres**[cite: 9].
* [cite_start]Uso de **Arreglos**[cite: 10].
* [cite_start]Implementación de **Registros (estructuras de datos)**[cite: 11].

## 🛠️ Especificaciones Técnicas

### Estructura del Registro (Libro)
[cite_start]Cada libro está representado por la siguiente estructura de datos[cite: 13, 14]:

| Campo | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| **Título** | Cadena | [cite_start]Nombre del libro[cite: 15]. |
| **Autor** | Cadena | [cite_start]Nombre del autor[cite: 16]. |
| **Año** | Entero | [cite_start]Año de publicación[cite: 17]. |
| **Categoría** | Cadena | [cite_start]Género o área del conocimiento[cite: 18]. |
| **ISBN** | Cadena | [cite_start]Código de hasta 13 dígitos[cite: 19]. |

[cite_start]*El sistema tiene una capacidad máxima de almacenamiento de **50 libros** mediante un arreglo de registros[cite: 20].*

### Funcionalidades del Programa
1. [cite_start]**Agregar libro:** Permite el registro de nuevos ejemplares en el sistema[cite: 23, 24].
2. [cite_start]**Buscar libro:** Búsqueda por título o autor (coincidencias exactas o parciales)[cite: 25, 26].
3. [cite_start]**Listar libros:** Visualización de todos los libros registrados en formato tabular[cite: 27, 28].
4. [cite_start]**Filtrar:** Clasificación de libros por año específico o por categoría[cite: 29, 30].
5. [cite_start]**Editar:** Modificación de los campos de un libro existente mediante su ISBN[cite: 31, 32].

## 📋 Requisitos de Validación
[cite_start]Para garantizar la integridad de los datos, el programa realiza las siguientes validaciones[cite: 33]:
* [cite_start]**Campos obligatorios:** El título, autor, categoría e ISBN no pueden estar vacíos[cite: 34].
* [cite_start]**Validación de año:** El año de publicación debe ser un número entero dentro de un rango lógico[cite: 35].
* [cite_start]**Mensajería:** El sistema emite mensajes claros de éxito, error o advertencia según el resultado de las operaciones[cite: 37].

## 📂 Entrega y Formato
* [cite_start]**Lenguajes permitidos:** C (.c), C++ (.cpp) o Java (.java)[cite: 39].
* [cite_start]**Documentación:** Incluye un informe en PDF con el código debidamente documentado[cite: 39].
* [cite_start]**Fecha de entrega:** Segunda semana de junio de 2025[cite: 40].

---
[cite_start]**Profesor:** Crispina Ramos S. [cite: 4]  
[cite_start]**Periodo:** I Semestre de 2025 [cite: 6]  
[cite_start]**Institución:** Universidad Tecnológica de Panamá [cite: 1]