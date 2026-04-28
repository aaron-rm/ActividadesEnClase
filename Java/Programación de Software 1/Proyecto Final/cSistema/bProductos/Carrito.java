package cSistema.bProductos;

// Clase Carrito
public class Carrito {
    private ItemCarrito[] items;
    private int totalItems;
    private final int MAX_ITEMS = 50;

    public Carrito() {
        items = new ItemCarrito[MAX_ITEMS];
        totalItems = 0;
    }

    // Agregar producto al carrito
    public void agregarProducto(Producto producto, int cantidad) throws CarritoException {
        if (cantidad <= 0) {
            throw new CarritoException("La cantidad debe ser mayor a 0");
        }

        // Buscar si el producto ya existe en el carrito
        for (int i = 0; i < totalItems; i++) {
            if (items[i].getProducto().getId() == producto.getId()) {
                // Si existe, aumentar la cantidad
                items[i].setCantidad(items[i].getCantidad() + cantidad);
                return;
            }
        }

        // Si no existe y hay espacio, agregar nuevo item
        if (totalItems >= MAX_ITEMS) {
            throw new CarritoException("El carrito está lleno. Máximo " + MAX_ITEMS + " productos diferentes");
        }

        items[totalItems] = new ItemCarrito(producto, cantidad);
        totalItems++;
    }

    // Eliminar producto del carrito
    public void eliminarProducto(int idProducto) throws CarritoException {
        for (int i = 0; i < totalItems; i++) {
            if (items[i].getProducto().getId() == idProducto) {
                // Mover todos los elementos hacia atrás
                for (int j = i; j < totalItems - 1; j++) {
                    items[j] = items[j + 1];
                }
                items[totalItems - 1] = null;
                totalItems--;
                return;
            }
        }
        throw new CarritoException("Producto no encontrado en el carrito");
    }

    // Modificar cantidad de un producto
    public void modificarCantidad(int idProducto, int nuevaCantidad) throws CarritoException {
        if (nuevaCantidad <= 0) {
            throw new CarritoException("La cantidad debe ser mayor a 0");
        }

        for (int i = 0; i < totalItems; i++) {
            if (items[i].getProducto().getId() == idProducto) {
                items[i].setCantidad(nuevaCantidad);
                return;
            }
        }
        throw new CarritoException("Producto no encontrado en el carrito");
    }

    // Vaciar carrito
    public void vaciarCarrito() {
        for (int i = 0; i < totalItems; i++) {
            items[i] = null;
        }
        totalItems = 0;
    }

    // Calcular total del carrito
    public double calcularTotal() {
        double total = 0;
        for (int i = 0; i < totalItems; i++) {
            total += items[i].getSubtotal();
        }
        return total;
    }

    // Obtener cantidad total de productos
    public int getCantidadTotalProductos() {
        int total = 0;
        for (int i = 0; i < totalItems; i++) {
            total += items[i].getCantidad();
        }
        return total;
    }

    // Verificar si el carrito está vacío
    public boolean estaVacio() {
        return totalItems == 0;
    }

    // Mostrar contenido del carrito
    public void mostrarCarrito() {
        if (estaVacio()) {
            System.out.println("\n🛒 El carrito está vacío");
            return;
        }

        System.out.println("\n🛒 CONTENIDO DEL CARRITO:");
        System.out.println("=".repeat(60));

        for (int i = 0; i < totalItems; i++) {
            System.out.println(items[i]);
        }

        System.out.printf("📊 RESUMEN:\n");
        System.out.printf("• Productos diferentes: %d\n", totalItems);
        System.out.printf("• Cantidad total de productos: %d\n", getCantidadTotalProductos());
        System.out.printf("• TOTAL A PAGAR: $%.2f\n", calcularTotal());
        System.out.println("=".repeat(60));
    }
    //impresion en grafico
    public String imprimirCarrito(){
        if (estaVacio()) {
            return "\n🛒 El carrito está vacío";
        }else {
            String inicio = String.format("\n🛒 CONTENIDO DEL CARRITO:","=".repeat(60));
            String contenido = "\n\n";
            for (int i = 0; i < totalItems; i++) {
                contenido += items[i].toString();
                contenido += "\n";
            }
            String fin = String.format("\n• TOTAL A PAGAR: $%.2f\n", calcularTotal(),"=".repeat(60));

            return (inicio+contenido+fin);
        }
    }

    // Procesar compra
    public void procesarCompra() throws CarritoException {
        if (estaVacio()) {
            throw new CarritoException("No se puede procesar una compra con el carrito vacío");
        }

        System.out.println("\n💳 PROCESANDO COMPRA...");
        System.out.println("=".repeat(60));
        mostrarCarrito();

        System.out.println("\n✅ ¡COMPRA PROCESADA EXITOSAMENTE!");
        System.out.println("🎉 Gracias por su compra. Sus productos serán enviados pronto.");

        // Vaciar carrito después de la compra
        vaciarCarrito();
    }

    // Getter para totalItems
    public int getTotalItems() {
        return totalItems;
    }

    // Obtener item por índice
    public ItemCarrito getItem(int indice) {
        if (indice >= 0 && indice < totalItems) {
            return items[indice];
        }
        return null;
    }
}
