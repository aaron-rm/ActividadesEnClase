package problema4;

public class Estudiantes {
    private String nombre,apellido,numMatricula,carrera;
    private int calif1,calif2,calif3;

    Estudiantes(String nombre,String apellido,String numMatricula, String carrera, int calif1, int calif2, int calif3){
        this.nombre=nombre;
        this.apellido=apellido;
        this.numMatricula=numMatricula;
        this.carrera=carrera;
        this.calif1=calif1;
        this.calif2=calif2;
        this.calif3=calif3;
    }

    public double calcularPromedio(){
        return((calif1+calif2+calif3)/3);
    }

    public void mostrarInformacion(){
        System.out.println();
        System.out.println("Nombre completo del estudiante: "+nombre+" "+apellido);
        System.out.println("Carrera que cursa: "+carrera);
        System.out.println("Número de matricula: "+numMatricula);
        System.out.println("Promedio del estudiante: "+calcularPromedio());
    }
}
