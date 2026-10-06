# DynamicWeb: registro de usuarios

Proyecto web de Eclipse cuyo nombre y contexto de despliegue son **Web1**. El formulario envía sus datos a una página JSP que los inserta en MySQL y muestra la respuesta.

| Archivo o carpeta | Función |
| --- | --- |
| [HOME.html](src/main/webapp/HOME.html) | Página de inicio. |
| [REGISTRO.html](src/main/webapp/REGISTRO.html) | Formulario de datos del usuario. |
| [RESPUESTA.jsp](src/main/webapp/RESPUESTA.jsp) | Lectura de parámetros, inserción JDBC y presentación de resultados. |
| [CSS](src/main/webapp/CSS/) | Estilos de página, formulario y respuesta. |
| [WEB-INF/lib](src/main/webapp/WEB-INF/lib/) | Controlador MySQL Connector/J incluido. |

## Entorno y ejecución

Los metadatos de la entrega especifican Java 21, Tomcat 9.0.100 y Servlet 4.0.

1. Importa esta carpeta como proyecto existente de Eclipse con soporte para aplicaciones web.
2. Configura el JDK y el runtime Tomcat del proyecto.
3. Prepara MySQL y la base `prueba1`, con una tabla `usuario` que admita las columnas `nombre`, `direccion`, `contrasenia`, `provincia` y `herramientas`.
4. Revisa la conexión de `RESPUESTA.jsp`: `localhost:3306`, usuario `root` y contraseña vacía son los valores originales.
5. Despliega el proyecto en Tomcat y abre `http://localhost:8080/Web1/HOME.html`, ajustando el puerto si tu servidor usa otro.

El JAR de MySQL se incorporó desde el controlador existente en Taller4; `.classpath` lo referencia mediante una ruta local al proyecto. No se incluye un script SQL de creación de la base de datos.

[← Volver al portafolio](../../../readme.md)
