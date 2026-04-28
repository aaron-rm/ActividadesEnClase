# Actividad 4: Objetos Abstractos y Lógicos 🏗️

Este repositorio contiene la resolución de una serie de mini ejercicios prácticos enfocados en el modelado de clases y relaciones de objetos dentro de sistemas administrativos y lógicos.

## 🎯 Objetivo
El propósito de esta actividad es practicar el diseño de software orientado a objetos, diferenciando entre representaciones de conceptos administrativos y objetos físicos, además de definir tipos de relaciones (agregación, composición, dependencia).

## 🛠️ Ejercicios Desarrollados

### 1. Factura Electrónica 📄
* **Descripción:** Modelado de una factura para un sistema contable.
* **Componentes:**
    * Atributos de identificación y cálculo de totales.
    * Método `generarResumen()` para visualizar datos principales.
    * Relación con la clase `DetalleFactura`.
* **Análisis:** Justificación técnica sobre si la relación es una **agregación** o una **composición**.

### 2. Matrícula Académica 🎓
* **Descripción:** Diseño de un sistema de inscripción universitaria.
* **Componentes:**
    * Clase `Matricula` que gestiona una lista de objetos `Curso`.
    * Método `calcularCostoTotal()` para la suma de aranceles.
    * Método `mostrarResumen()` para listar cursos y costos finales.

### 3. Programa y Sesión 🖥️
* **Descripción:** Modelado lógico del ciclo de vida de un software y el acceso de usuarios.
* **Componentes:**
    * Clase `Programa` con atributos de versión y estado, y métodos `iniciar()` y `detener()`.
    * Clase `Sesion` con información de usuario y marcas de tiempo.
* **Análisis:** Representación de la dependencia entre el programa y la sesión activa.

### 4. Gestor de Notificaciones 🔔
* **Descripción:** Diseño de un backend para la administración de alertas.
* **Componentes:**
    * Clase `Notificacion` con estados y métodos de envío/lectura.
    * Clase `GestorNotificaciones` para la administración del conjunto de alertas.
* **Análisis:** Reflexión sobre la naturaleza del objeto (abstracto vs. lógico) según el dominio del sistema.

## 📋 Requisitos de Entrega
* Modelado de clases con sus respectivos atributos y métodos.
* Justificaciones teóricas para cada tipo de relación propuesta.
* Implementación de la lógica solicitada para el cálculo y resumen de datos.

---
**Asignatura:** Análisis y Diseño de Algoritmos / Programación Orientada a Objetos  
**Temática:** Modelado de Sistemas Administrativos