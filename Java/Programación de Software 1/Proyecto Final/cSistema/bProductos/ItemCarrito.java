package cSistema.bProductos;

// Clase ItemCarrito para manejar productos con cantidad
class ItemCarrito {
    private Producto producto;
    private int cantidad;

    public ItemCarrito(Producto producto, int cantidad) {
        this.producto = producto;
        this.cantidad = cantidad;
    }

    // Getters
    public Producto getProducto() {
        return producto;
    }

    public int getCantidad() {
        return cantidad;
    }

    // Setters
    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }

    // Calcular subtotal
    public double getSubtotal() {
        return producto.getPrecio() * cantidad;
    }

    @Override
    public String toString() {
        return String.format("• %s\n  Cantidad: %d | Precio unitario: $%.2f | Subtotal: $%.2f\n%s",
                producto.getNombre(), cantidad, producto.getPrecio(), getSubtotal(), "-".repeat(50));
    }
}
