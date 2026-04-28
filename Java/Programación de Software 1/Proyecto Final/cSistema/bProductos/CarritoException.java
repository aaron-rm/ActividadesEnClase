package cSistema.bProductos;

// Excepción personalizada para carrito
class CarritoException extends Exception {
    public CarritoException() {
        super("Error en el carrito");
    }

    public CarritoException(String mensaje) {
        super(mensaje);
    }

    public CarritoException(String mensaje, Throwable causa) {
        super(mensaje, causa);
    }

    public CarritoException(Throwable causa) {
        super(causa);
    }
}
