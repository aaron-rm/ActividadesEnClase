# Actividad 4: Objetos Abstractos y Lógicos 🏗️

Mini ejercicios de **Arquitectura y Diseño de Software** que representan conceptos administrativos y lógicos mediante clases Java. El [enunciado de la actividad](Actividad%204.pdf) plantea relaciones entre objetos y su justificación.

| Ejercicio | Clases | Comportamiento implementado |
| --- | --- | --- |
| [Factura electrónica](Problema1/) | `Factura`, `DetalleFactura`, `Main` | Resumen de factura, precio e ITBMS del 7%; consulta del detalle. |
| [Matrícula académica](Problema2/) | `Matricula`, `Curso`, `Main` | Registro de un arreglo de cursos, cálculo del costo total y resumen. |
| [Programa y sesión](Problema3/) | `Programa`, `Sesion`, `Main` | Inicio y detención del programa; sesión asociada y hora de inicio. |
| [Gestor de notificaciones](Problema4/) | `Notificacion`, `GestorNotificaciones`, `Main` | Administración de un arreglo de notificaciones, envío y cambio de estado. |

## Ejecución

Desde esta carpeta, compila y ejecuta cada paquete por separado. Ejemplo para el primer ejercicio:

```powershell
javac -encoding UTF-8 -d out Problema1/*.java
java -cp out Problema1.Main
```

Sustituye `Problema1` por `Problema2`, `Problema3` o `Problema4` para los demás ejercicios. El enunciado pide analizar agregación, composición y dependencia; el código disponible contiene las clases y sus demostraciones.

[← Volver al portafolio](../../readme.md)
