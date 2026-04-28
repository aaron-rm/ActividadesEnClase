package Problema2;

public class Curso {
    private double  costo;
    private String titulo;

    public Curso(double costo, String titulo) {
        this.costo = costo;
        this.titulo = titulo;
    }

    public double getCosto() {
        return costo;
    }

    public void mostrarCurso(){
        System.out.println("Curso: " + titulo);
        System.out.println("Precio: " + costo);
    }
}
