package cSistema.bProductos;

// Clase ValidadorEntrada
class ValidadorEntrada {

    // Validar opción del menú principal
    public static int validarOpcionMenu(String entrada) throws EntradaInvalidaException {
        if (entrada == null || entrada.trim().isEmpty()) {
            throw new EntradaInvalidaException("La entrada no puede estar vacía");
        }

        try {
            int opcion = Integer.parseInt(entrada.trim());

            if (opcion < 1 || opcion > 9) {
                throw new EntradaInvalidaException("La opción debe estar entre 1 y 9");
            }

            return opcion;

        } catch (NumberFormatException e) {
            throw new EntradaInvalidaException("Por favor, ingrese un número válido");
        }
    }

    // Validar opción del menú de carrito
    public static int validarOpcionCarrito(String entrada) throws EntradaInvalidaException {
        if (entrada == null || entrada.trim().isEmpty()) {
            throw new EntradaInvalidaException("La entrada no puede estar vacía");
        }

        try {
            int opcion = Integer.parseInt(entrada.trim());

            if (opcion < 1 || opcion > 6) {
                throw new EntradaInvalidaException("La opción debe estar entre 1 y 6");
            }

            return opcion;

        } catch (NumberFormatException e) {
            throw new EntradaInvalidaException("Por favor, ingrese un número válido");
        }
    }

    // Validar ID de producto
    public static int validarId(String entrada, int maxId) throws EntradaInvalidaException {
        if (entrada == null || entrada.trim().isEmpty()) {
            throw new EntradaInvalidaException("El ID no puede estar vacío");
        }

        try {
            int id = Integer.parseInt(entrada.trim());

            if (id < 1 || id > maxId) {
                throw new EntradaInvalidaException("El ID debe estar entre 1 y " + maxId);
            }

            return id;

        } catch (NumberFormatException e) {
            throw new EntradaInvalidaException("Por favor, ingrese un número válido para el ID");
        }
    }

    // Validar cantidad
    public static int validarCantidad(String entrada) throws EntradaInvalidaException {
        if (entrada == null || entrada.trim().isEmpty()) {
            throw new EntradaInvalidaException("La cantidad no puede estar vacía");
        }

        try {
            int cantidad = Integer.parseInt(entrada.trim());

            if (cantidad <= 0) {
                throw new EntradaInvalidaException("La cantidad debe ser mayor a 0");
            }

            if (cantidad > 100) {
                throw new EntradaInvalidaException("La cantidad no puede ser mayor a 100");
            }

            return cantidad;

        } catch (NumberFormatException e) {
            throw new EntradaInvalidaException("Por favor, ingrese un número válido para la cantidad");
        }
    }

    // Validar opción de categoría
    public static int validarOpcionCategoria(String entrada) throws EntradaInvalidaException {
        if (entrada == null || entrada.trim().isEmpty()) {
            throw new EntradaInvalidaException("La selección de categoría no puede estar vacía");
        }

        try {
            int opcion = Integer.parseInt(entrada.trim());

            if (opcion < 1 || opcion > 3) {
                throw new EntradaInvalidaException("La opción de categoría debe estar entre 1 y 3");
            }

            return opcion;

        } catch (NumberFormatException e) {
            throw new EntradaInvalidaException("Por favor, ingrese un número válido para la categoría");
        }
    }

    // Convertir opción de categoría a string
    public static String convertirOpcionACategoria(int opcion) throws EntradaInvalidaException {
        switch (opcion) {
            case 1:
                return "Limpieza";
            case 2:
                return "Protección";
            case 3:
                return "Accesorios";
            default:
                throw new EntradaInvalidaException("Opción de categoría no válida");
        }
    }
}