# SpeedLab 🚗

Proyecto final de Programación de Software 1: aplicación de escritorio en Java Swing para una empresa de servicios y productos de lavado de autos.

| Carpeta | Responsabilidad |
| --- | --- |
| [aMain](aMain/) | Ventana de entrada; clase principal `aMain.Main`. |
| [bInterfaz](bInterfaz/) | Pantallas de cuentas, registro, menú, productos y carrito. |
| [cSistema/aUsuario](cSistema/aUsuario/) | Clientes y cuentas. |
| [cSistema/bProductos](cSistema/bProductos/) | Catálogo, productos, carrito, validadores y excepciones. |
| [cSistema/cServicios](cSistema/cServicios/) | Clientes de servicios, citas, agenda e interfaz de reserva. |
| [images](images/) | Logotipos e iconos utilizados por la interfaz. |

## Funciones

Creación y acceso a cuentas, consulta de productos, administración del carrito y reserva de citas. El paquete de productos también incluye una entrada de consola: `cSistema.bProductos.Main`.

## Preparación y ejecución

1. Configura esta carpeta como raíz de fuentes de un proyecto Java en IntelliJ IDEA.
2. Conserva los archivos `.form` vinculados a sus clases y habilita su procesamiento mediante el diseñador de interfaces.
3. Coloca `images` en la raíz de recursos del classpath para resolver referencias como `/images/UTP logo.png`.
4. Ejecuta `aMain.Main` para la aplicación gráfica.

El catálogo utiliza `String.repeat`, por lo que ese código requiere Java 11 o superior. Los datos de cuentas, productos y citas se gestionan en memoria.

## Recursos pendientes

Los archivos originales `images/calendario.png` e `images/productos.png` están vacíos. Se conservan como parte de la entrega, pero esos iconos necesitan imágenes válidas para mostrarse.

[← Volver al portafolio](../../../readme.md)
