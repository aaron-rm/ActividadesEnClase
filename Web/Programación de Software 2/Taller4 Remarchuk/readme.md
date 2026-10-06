# Taller 4: Universidad del Pueblo 🎓

Portal académico desarrollado con JSP, HTML, CSS y MySQL. Incluye inicio, registro de estudiantes y profesores, calendario de actividades y página de soporte. El nombre del proyecto y contexto de Eclipse son **Taller4**.

| Página | Función |
| --- | --- |
| [HOME.jsp](src/main/webapp/HOME.jsp) | Inicio, navegación y noticias. |
| [ESTUDIANTES.jsp](src/main/webapp/ESTUDIANTES.jsp) | Formulario de estudiantes y cursos de interés. |
| [procesar_estudiante.jsp](src/main/webapp/procesar_estudiante.jsp) | Inserción de estudiantes y confirmación del registro. |
| [PROFESORES.jsp](src/main/webapp/PROFESORES.jsp) | Formulario de profesores. |
| [procesar_profesor.jsp](src/main/webapp/procesar_profesor.jsp) | Inserción de profesores y confirmación. |
| [CALENDARIO.jsp](src/main/webapp/CALENDARIO.jsp) | Consulta de actividades y generación de días del mes. |
| [SOPORTE.jsp](src/main/webapp/SOPORTE.jsp) | Información del equipo de soporte. |

## Entorno y ejecución

Los metadatos de Eclipse especifican Java 25, Tomcat 9.0.100 y Servlet 4.0. MySQL Connector/J 9.7.0 se conserva en `src/main/webapp/WEB-INF/lib`, y `.classpath` utiliza esa ruta relativa.

1. Importa esta carpeta como proyecto existente de Eclipse con soporte web.
2. Configura el JDK y el runtime Tomcat del proyecto.
3. Prepara MySQL con la base `taller4` y las tablas que consulta el código.
4. Revisa las conexiones JDBC de los procesadores y del calendario: los valores originales son `localhost:3306`, usuario `root` y contraseña vacía.
5. Despliega en Tomcat y abre `http://localhost:8080/Taller4/HOME.jsp`, ajustando el puerto del servidor cuando corresponda.

## Datos requeridos por las páginas

| Tabla | Columnas utilizadas por el código |
| --- | --- |
| `estudiante` | `nombre`, `cedula`, `anio`, `centroEDU`, `indice`, `cursos`. |
| `profesor` | `nombre`, `cedula`, `materia`, `centroEDU`, `expVIR`. |
| `programacion`, `soldadura`, `electronica` | `fecha`, `horario`; utilizadas para el calendario. |

La entrega contiene capturas de tablas, pero no un script SQL con tipos, restricciones o datos iniciales. El encabezado del calendario dice «Junio», mientras que la generación de días usa el mes actual mediante `YearMonth.now()`.

## Documentación y recursos

[.Archivos](src/main/webapp/.Archivos/) conserva el wireframe en PDF y las capturas de tablas en PDF y Word. Las carpetas `css`, `html` e `img` contienen estilos, encabezado/pie compartidos e imágenes.

[← Volver al portafolio](../../../readme.md)
