package Problema2;

public class Matricula {
    private Curso[] cursosMatriculados;

    public Matricula(Curso[] cursos) {
        this.cursosMatriculados = cursos;
    }

    public double calcularCostoTotal(){
        double total = 0;
        for (int i = 0; i < cursosMatriculados.length; i++) {
            total += cursosMatriculados[i].getCosto();
        }
        return total;
    }

    public void mostrarResumen(){
        System.out.println("Cursos Matriculados:");
        for (int i = 0; i < cursosMatriculados.length; i++) {
            cursosMatriculados[i].mostrarCurso();
        }
        System.out.println("Precio final: " + calcularCostoTotal());
    }
}
