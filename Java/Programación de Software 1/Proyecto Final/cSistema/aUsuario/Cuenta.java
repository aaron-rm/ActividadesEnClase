package cSistema.aUsuario;

import cSistema.bProductos.Carrito;

public class Cuenta {
    private String idCuenta;
    private String password;
    public Cliente cliente;
    private boolean activa;
    public Carrito carrito;

    public Cuenta(String idCuenta, String password, Cliente cliente) {
        //cuenta nueva
        this.idCuenta = idCuenta;
        this.password = password;
        this.cliente = cliente;
        this.carrito = new Carrito();
    }

    public Cuenta(String idCuenta, String password) {
        //cuenta existente
        this.idCuenta = idCuenta;
        this.password = password;
    }

    public String getIdCuenta() {
        return idCuenta;
    }

    public String getPassword() {
        return password;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public boolean isActiva() {
        return activa;
    }
  
    //Activar cuenta
    public void activarCuenta() {
        if (!activa) {
            activa = true;
            System.out.println("Cuenta activada exitosamente.");
        } else {
            System.out.println("La cuenta ya está activa.");
        }
    }

    //Cerrar cuenta
    public void cerrarCuenta() {
        if (activa) {
            activa = false;
            System.out.println("Cuenta cerrada exitosamente.");
        } else {
            System.out.println("La cuenta ya está cerrada.");
        }
    }

}
