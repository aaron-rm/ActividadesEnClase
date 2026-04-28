package cSistema.bProductos;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// Clase Principal
public class Main {
    private static CatalogoManager catalogoManager;
    private static Carrito carrito;
    private static BufferedReader reader;

    public static void main(String[] args) {
        catalogoManager = new CatalogoManager();
        carrito = new Carrito();
        reader = new BufferedReader(new InputStreamReader(System.in));

        try {
            mostrarMenuPrincipal();
        } catch (IOException e) {
            System.err.println("❌ Error crítico de entrada/salida: " + e.getMessage());
        } finally {
            cerrarRecursos();
        }
    }

    private static void mostrarMenuPrincipal() throws IOException {
        boolean continuar = true;

        while (continuar) {
            try {
                mostrarMenu();
                String entrada = reader.readLine();
                int opcion = ValidadorEntrada.validarOpcionMenu(entrada);

                switch (opcion) {
                    case 1:
                        catalogoManager.mostrarTodosLosProductos();
                        break;
                    case 2:
                        buscarProductoPorId();
                        break;
                    case 3:
                        filtrarPorCategoria();
                        break;
                    case 4:
                        mostrarProductoMasCaro();
                        break;
                    case 5:
                        mostrarProductoMasBarato();
                        break;
                    case 6:
                        agregarProductoAlCarrito();
                        break;
                    case 7:
                        gestionarCarrito();
                        break;
                    case 8:
                        carrito.mostrarCarrito();
                        break;
                    case 9:
                        System.out.println("\n¡Gracias por usar nuestro catálogo! 🚗✨");
                        continuar = false;
                        break;
                }

                if (continuar) {
                    esperarEnter();
                }

            } catch (EntradaInvalidaException e) {
                System.out.println("\n❌ " + e.getMessage());
                esperarEnter();
            } catch (IOException e) {
                System.err.println("❌ Error de lectura: " + e.getMessage());
                throw e;
            } catch (Exception e) {
                System.err.println("❌ Error inesperado: " + e.getMessage());
                esperarEnter();
            }
        }
    }

    private static void mostrarMenu() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("🚗 CATÁLOGO DE PRODUCTOS PARA LAVADO DE AUTOS 🚗");
        System.out.println("=".repeat(60));
        System.out.println("📋 CATÁLOGO:");
        System.out.println("1. Ver todos los productos");
        System.out.println("2. Buscar producto por ID");
        System.out.println("3. Filtrar por categoría");
        System.out.println("4. Ver producto más caro");
        System.out.println("5. Ver producto más barato");
        System.out.println("\n🛒 CARRITO DE COMPRAS:");
        System.out.println("6. Agregar producto al carrito");
        System.out.println("7. Gestionar carrito");
        System.out.println("8. Ver carrito");
        System.out.println("\n9. Salir");
        System.out.println("=".repeat(60));

        // Mostrar indicador del carrito
        if (!carrito.estaVacio()) {
            System.out.printf("🛒 Carrito: %d productos | Total: $%.2f\n",
                    carrito.getCantidadTotalProductos(), carrito.calcularTotal());
        }

        System.out.print("Seleccione una opción (1-9): ");
    }


    private static void buscarProductoPorId() throws IOException {
        try {
            System.out.print("\n🔍 Ingrese el ID del producto a buscar (1-" +
                    catalogoManager.getTotalProductos() + "): ");
            String entrada = reader.readLine();

            int id = ValidadorEntrada.validarId(entrada, catalogoManager.getTotalProductos());
            Producto producto = catalogoManager.buscarProductoPorId(id);

            System.out.println("\n✅ PRODUCTO ENCONTRADO:");
            System.out.println("=".repeat(60));
            System.out.println(producto);

        } catch (EntradaInvalidaException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (ProductoNoEncontradoException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (IOException e) {
            System.err.println("❌ Error de lectura: " + e.getMessage());
            throw e;
        }
    }





    private static void filtrarPorCategoria() throws IOException {
        try {
            System.out.println("\n📂 CATEGORÍAS DISPONIBLES:");
            System.out.println("1. Limpieza");
            System.out.println("2. Protección");
            System.out.println("3. Accesorios");
            System.out.print("Seleccione una categoría (1-3): ");

            String entrada = reader.readLine();
            int opcionCategoria = ValidadorEntrada.validarOpcionCategoria(entrada);
            String categoria = ValidadorEntrada.convertirOpcionACategoria(opcionCategoria);

            Producto[] productosFiltrados = catalogoManager.filtrarPorCategoria(categoria);

            System.out.println("\n🏷️ PRODUCTOS DE LA CATEGORÍA: " + categoria.toUpperCase());
            System.out.println("=".repeat(60));

            if (productosFiltrados.length == 0) {
                System.out.println("No se encontraron productos en esta categoría.");
            } else {
                for (int i = 0; i < productosFiltrados.length; i++) {
                    System.out.println(productosFiltrados[i]);
                }
                System.out.printf("\nProductos encontrados: %d\n", productosFiltrados.length);
            }

        } catch (EntradaInvalidaException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (IOException e) {
            System.err.println("❌ Error de lectura: " + e.getMessage());
            throw e;
        }
    }



    private static void mostrarProductoMasCaro() {
        try {
            Producto masCaro = catalogoManager.obtenerProductoMasCaro();

            System.out.println("\n💰 PRODUCTO MÁS CARO:");
            System.out.println("=".repeat(60));
            System.out.println(masCaro);

        } catch (ProductoNoEncontradoException e) {
            System.err.println("❌ " + e.getMessage());
        }
    }

    private static void mostrarProductoMasBarato() {
        try {
            Producto masBarato = catalogoManager.obtenerProductoMasBarato();

            System.out.println("\n💸 PRODUCTO MÁS BARATO:");
            System.out.println("=".repeat(60));
            System.out.println(masBarato);

        } catch (ProductoNoEncontradoException e) {
            System.err.println("❌ " + e.getMessage());
        }
    }

    private static void agregarProductoAlCarrito() throws IOException {
        try {
            System.out.print("\n🛒 Ingrese el ID del producto a agregar (1-" +
                    catalogoManager.getTotalProductos() + "): ");
            String entradaId = reader.readLine();
            int id = ValidadorEntrada.validarId(entradaId, catalogoManager.getTotalProductos());

            Producto producto = catalogoManager.buscarProductoPorId(id);

            System.out.print("📦 Ingrese la cantidad: ");
            String entradaCantidad = reader.readLine();
            int cantidad = ValidadorEntrada.validarCantidad(entradaCantidad);

            carrito.agregarProducto(producto, cantidad);

            System.out.println("\n✅ ¡Producto agregado al carrito exitosamente!");
            System.out.printf("• %s (Cantidad: %d)\n", producto.getNombre(), cantidad);
            System.out.printf("• Subtotal: $%.2f\n", producto.getPrecio() * cantidad);
            System.out.printf("• Total del carrito: $%.2f\n", carrito.calcularTotal());

        } catch (EntradaInvalidaException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (ProductoNoEncontradoException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (CarritoException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (IOException e) {
            System.err.println("❌ Error de lectura: " + e.getMessage());
            throw e;
        }
    }

    private static void gestionarCarrito() throws IOException {
        boolean continuar = true;

        while (continuar) {
            try {
                mostrarMenuCarrito();
                String entrada = reader.readLine();
                int opcion = ValidadorEntrada.validarOpcionCarrito(entrada);

                switch (opcion) {
                    case 1:
                        carrito.mostrarCarrito();
                        break;
                    case 2:
                        eliminarProductoDelCarrito();
                        break;
                    case 3:
                        modificarCantidadEnCarrito();
                        break;
                    case 4:
                        vaciarCarritoCompleto();
                        break;
                    case 5:
                        procesarCompraCarrito();
                        break;
                    case 6:
                        continuar = false;
                        break;
                }

                if (continuar) {
                    esperarEnter();
                }

            } catch (EntradaInvalidaException e) {
                System.out.println("\n❌ " + e.getMessage());
                esperarEnter();
            } catch (IOException e) {
                System.err.println("❌ Error de lectura: " + e.getMessage());
                throw e;
            } catch (Exception e) {
                System.err.println("❌ Error inesperado: " + e.getMessage());
                esperarEnter();
            }
        }
    }

    private static void mostrarMenuCarrito() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("🛒 GESTIÓN DEL CARRITO DE COMPRAS");
        System.out.println("=".repeat(60));
        System.out.println("1. Ver contenido del carrito");
        System.out.println("2. Eliminar producto del carrito");
        System.out.println("3. Modificar cantidad de un producto");
        System.out.println("4. Vaciar carrito completo");
        System.out.println("5. Procesar compra");
        System.out.println("6. Volver al menú principal");
        System.out.println("=".repeat(60));

        if (!carrito.estaVacio()) {
            System.out.printf("🛒 Estado: %d productos | Total: $%.2f\n",
                    carrito.getCantidadTotalProductos(), carrito.calcularTotal());
        } else {
            System.out.println("🛒 Estado: Carrito vacío");
        }

        System.out.print("Seleccione una opción (1-6): ");
    }

    private static void eliminarProductoDelCarrito() throws IOException {
        try {
            if (carrito.estaVacio()) {
                System.out.println("\n❌ El carrito está vacío");
                return;
            }

            carrito.mostrarCarrito();
            System.out.print("\n🗑️ Ingrese el ID del producto a eliminar: ");
            String entrada = reader.readLine();
            int id = ValidadorEntrada.validarId(entrada, catalogoManager.getTotalProductos());

            carrito.eliminarProducto(id);
            System.out.println("\n✅ ¡Producto eliminado del carrito exitosamente!");

        } catch (EntradaInvalidaException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (CarritoException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (IOException e) {
            System.err.println("❌ Error de lectura: " + e.getMessage());
            throw e;
        }
    }

    private static void modificarCantidadEnCarrito() throws IOException {
        try {
            if (carrito.estaVacio()) {
                System.out.println("\n❌ El carrito está vacío");
                return;
            }

            carrito.mostrarCarrito();
            System.out.print("\n📝 Ingrese el ID del producto a modificar: ");
            String entradaId = reader.readLine();
            int id = ValidadorEntrada.validarId(entradaId, catalogoManager.getTotalProductos());

            System.out.print("📦 Ingrese la nueva cantidad: ");
            String entradaCantidad = reader.readLine();
            int cantidad = ValidadorEntrada.validarCantidad(entradaCantidad);

            carrito.modificarCantidad(id, cantidad);
            System.out.println("\n✅ ¡Cantidad modificada exitosamente!");

        } catch (EntradaInvalidaException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (CarritoException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (IOException e) {
            System.err.println("❌ Error de lectura: " + e.getMessage());
            throw e;
        }
    }

    private static void vaciarCarritoCompleto() throws IOException {
        try {
            if (carrito.estaVacio()) {
                System.out.println("\n❌ El carrito ya está vacío");
                return;
            }

            System.out.print("\n⚠️ ¿Está seguro de que desea vaciar todo el carrito? (s/n): ");
            String confirmacion = reader.readLine().trim().toLowerCase();

            if (confirmacion.startsWith("s")) {
                carrito.vaciarCarrito();
                System.out.println("\n✅ ¡Carrito vaciado exitosamente!");
            } else {
                System.out.println("\n❌ Operación cancelada");
            }

        } catch (IOException e) {
            System.err.println("❌ Error de lectura: " + e.getMessage());
            throw e;
        }
    }

    private static void procesarCompraCarrito() throws IOException {
        try {
            if (carrito.estaVacio()) {
                System.out.println("\n❌ No se puede procesar una compra con el carrito vacío");
                return;
            }

            System.out.print("\n💳 ¿Confirma que desea procesar la compra? (s/n): ");
            String confirmacion = reader.readLine().trim().toLowerCase();

            if (confirmacion.startsWith("s")) {
                carrito.procesarCompra();
                System.out.println("\n🎊 ¡Su pedido ha sido procesado exitosamente!");
                System.out.println("📧 Recibirá un email de confirmación en breve");
                System.out.println("🚚 El tiempo estimado de entrega es de 3-5 días hábiles");
            } else {
                System.out.println("\n❌ Compra cancelada");
            }

        } catch (CarritoException e) {
            System.out.println("❌ " + e.getMessage());
        } catch (IOException e) {
            System.err.println("❌ Error de lectura: " + e.getMessage());
            throw e;
        }
    }

    private static void esperarEnter() throws IOException {
        System.out.print("\nPresione Enter para continuar...");
        reader.readLine();
    }

    private static void cerrarRecursos() {
        try {
            if (reader != null) {
                reader.close();
            }
        } catch (IOException e) {
            System.err.println("❌ Error al cerrar recursos: " + e.getMessage());
        }
    }
}