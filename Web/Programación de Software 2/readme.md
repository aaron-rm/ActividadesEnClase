# Programación de Software 2 🌐

Prácticas de desarrollo web procedentes de `PROG SOFT 2` de TrabajosEnClase. Reúnen etiquetas HTML, formularios, maquetación con Flexbox y páginas dinámicas con JSP/JDBC.

| Trabajo | Contenido | Inicio |
| --- | --- | --- |
| [TAGS.html](TAGS.html) | Ejemplos comentados de etiquetas, enlaces, tablas y multimedia. | Abrir el archivo en el navegador. |
| [FORMS.html](FORMS.html) | Controles de formulario HTML. | Abrir el archivo en el navegador. |
| [PRÁCTICA2](PR%C3%81CTICA2/readme.md) | Recetas de desayuno, almuerzo y cena; formulario de registro. | `PRÁCTICA2/HOME.html`. |
| [PracticaFlex](PracticaFlex/readme.md) | Página de comida rápida con tarjetas y Flexbox. | `PracticaFlex/index.html`. |
| [DynamicWeb](DynamicWeb/readme.md) | Registro de usuarios con JSP y MySQL. | `Web1/HOME.html` en Tomcat. |
| [Taller4 Remarchuk](Taller4%20Remarchuk/readme.md) | Portal universitario con estudiantes, profesores y calendario. | `Taller4/HOME.jsp` en Tomcat. |

## Recursos y ejecución

`audios/vaca.mp3` y `videos/vaca.mp4` se utilizan desde `TAGS.html`; conserva esas rutas. Varias páginas también referencian imágenes externas.

Las prácticas estáticas no requieren compilación. Para los proyectos dinámicos, importa cada carpeta como proyecto existente de Eclipse y configura Tomcat. Sus metadatos originales especifican Tomcat 9.0.100 y Servlet 4.0, con Java 21 para DynamicWeb y Java 25 para Taller4. El controlador MySQL está disponible dentro de `WEB-INF/lib` de cada proyecto.

Las bases de datos y tablas se deben preparar por separado: la entrega no incluye un archivo SQL de creación o exportación.

[← Volver al portafolio](../../readme.md)
