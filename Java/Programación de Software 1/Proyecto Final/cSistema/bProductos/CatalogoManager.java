package cSistema.bProductos;

import javax.swing.*;

// Clase CatalogoManager
public class CatalogoManager {
    public Producto[] productos;
    private int totalProductos;
    private final int MAX_PRODUCTOS = 10;

    // Constructor
    public CatalogoManager() {
        productos = new Producto[MAX_PRODUCTOS];
        totalProductos = 0;
        inicializarProductos();
    }

    // Inicializar productos del catálogo
    private void inicializarProductos() {
        productos[0] = new Producto(1, "Shampoo Premium para Autos",
                "Shampoo concentrado con fórmula pH balanceado, elimina suciedad sin dañar la pintura",
                15.99, "Limpieza");

        productos[1] = new Producto(2, "Cera Protectora",
                "Cera natural de carnauba que brinda protección UV y brillo duradero por 6 meses",
                24.50, "Protección");

        productos[2] = new Producto(3, "Kit de Microfibras Professional",
                "Set de 5 paños de microfibra de alta calidad para secado y pulido sin rayones",
                18.75, "Accesorios");

        productos[3] = new Producto(4, "Descontaminante de Llantas",
                "Limpiador especializado para llantas, elimina grasa, polvo de frenos y suciedad",
                12.30, "Limpieza");

        totalProductos = 4;
    }

    // Mostrar todos los productos
    public void mostrarTodosLosProductos() {
        System.out.println("\n📋 TODOS LOS PRODUCTOS DISPONIBLES:");
        System.out.println("=".repeat(60));

        for (int i = 0; i < totalProductos; i++) {
            System.out.println(productos[i]);
        }

        System.out.printf("\nTotal de productos: %d\n", totalProductos);
    }
    public String infoProducto(int n){
        return  productos[n].toString();
    }

    // Buscar producto por ID
    public Producto buscarProductoPorId(int id) throws ProductoNoEncontradoException {
        if (id < 1 || id > totalProductos) {
            throw new ProductoNoEncontradoException("ID fuera de rango válido (1-" + totalProductos + ")");
        }

        for (int i = 0; i < totalProductos; i++) {
            if (productos[i].getId() == id) {
                return productos[i];
            }
        }

        throw new ProductoNoEncontradoException("Producto no encontrado con ID: " + id);
    }

    // Filtrar productos por categoría
    public Producto[] filtrarPorCategoria(String categoria) {
        Producto[] productosFiltrados = new Producto[totalProductos];
        int contador = 0;

        for (int i = 0; i < totalProductos; i++) {
            if (productos[i].getCategoria().equalsIgnoreCase(categoria)) {
                productosFiltrados[contador] = productos[i];
                contador++;
            }
        }

        // Crear array del tamaño exacto
        Producto[] resultado = new Producto[contador];
        for (int i = 0; i < contador; i++) {
            resultado[i] = productosFiltrados[i];
        }

        return resultado;
    }

    // Obtener producto más caro
    public String productoMasCaro(){
        try {
            return obtenerProductoMasCaro().toString();
        }catch (Exception e){
            JOptionPane.showMessageDialog(null, "No se encontro el producto mas caro");
        }
        return "";
    }
    public Producto obtenerProductoMasCaro() throws ProductoNoEncontradoException {
        if (totalProductos == 0) {
            throw new ProductoNoEncontradoException("No hay productos disponibles");
        }

        Producto masCaro = productos[0];
        for (int i = 1; i < totalProductos; i++) {
            if (productos[i].getPrecio() > masCaro.getPrecio()) {
                masCaro = productos[i];
            }
        }

        return masCaro;
    }

    // Obtener producto más barato
    public String productoMasBarato(){
        try {
        return obtenerProductoMasBarato().toString();
        }catch (Exception e){
            JOptionPane.showMessageDialog(null, "No se encontro el producto mas caro");
        }
        return "";
    }
    public Producto obtenerProductoMasBarato() throws ProductoNoEncontradoException {
        if (totalProductos == 0) {
            throw new ProductoNoEncontradoException("No hay productos disponibles");
        }

        Producto masBarato = productos[0];
        for (int i = 1; i < totalProductos; i++) {
            if (productos[i].getPrecio() < masBarato.getPrecio()) {
                masBarato = productos[i];
            }
        }

        return masBarato;
    }

    // Obtener categorías disponibles
    public String[] obtenerCategorias() {
        String[] categorias = new String[totalProductos];
        int contador = 0;

        for (int i = 0; i < totalProductos; i++) {
            String categoria = productos[i].getCategoria();
            boolean existe = false;

            // Verificar si la categoría ya existe
            for (int j = 0; j < contador; j++) {
                if (categorias[j].equalsIgnoreCase(categoria)) {
                    existe = true;
                    break;
                }
            }

            if (!existe) {
                categorias[contador] = categoria;
                contador++;
            }
        }

        // Crear array del tamaño exacto
        String[] resultado = new String[contador];
        for (int i = 0; i < contador; i++) {
            resultado[i] = categorias[i];
        }

        return resultado;
    }

    // Getter para total de productos
    public int getTotalProductos() {
        return totalProductos;
    }
}