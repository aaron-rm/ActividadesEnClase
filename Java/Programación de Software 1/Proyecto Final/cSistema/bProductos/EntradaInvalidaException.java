package cSistema.bProductos;

class EntradaInvalidaException extends Exception {
    public EntradaInvalidaException() {
        super("Entrada inválida");
    }

    public EntradaInvalidaException(String mensaje) {
        super(mensaje);
    }

    public EntradaInvalidaException(String mensaje, Throwable causa) {
        super(mensaje, causa);
    }

    public EntradaInvalidaException(Throwable causa) {
        super(causa);
    }
}
