package Problema3;

public class Programa {
    private String nombre;
    private String version;
    private boolean estado;

    public Programa(String nombre, String version) {
        this.nombre = nombre;
        this.version = version;
        this.estado = false;
    }

    public void iniciar(){
        System.out.println("Iniciando programa...");
        this.estado = true;
    }

    public void detener(){
        System.out.println("Deteniendo programa...");
        this.estado = false;
    }

    public void getInfoPrograma() {
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Version: " + this.version);
    }
}
