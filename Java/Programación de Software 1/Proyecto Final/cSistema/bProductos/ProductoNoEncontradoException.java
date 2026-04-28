package cSistema.bProductos;

// Excepción personalizada para productos no encontrados
class ProductoNoEncontradoException extends Exception {
    public ProductoNoEncontradoException() {
        super("Producto no encontrado");
    }

    public ProductoNoEncontradoException(String mensaje) {
        super(mensaje);
    }

    public ProductoNoEncontradoException(String mensaje, Throwable causa) {
        super(mensaje, causa);
    }

    public ProductoNoEncontradoException(Throwable causa) {
        super(causa);
    }
}
