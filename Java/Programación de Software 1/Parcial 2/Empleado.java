
public class Empleado {
    private String nombreCompleto,cedula,fechaNacimiento,cargo,turno;
    public Sistema sistema;
    private int edad;

    public Empleado(){
        this.sistema=new Sistema();
        this.nombreCompleto="";
        this.cedula="";
        this.fechaNacimiento="";
        this.cargo="";
        this.turno="";
        this.edad=0;
    }

    public void mostrarInformacion(int i){
        System.out.printf("\n\nInformación del empleado %d\n",i);
        System.out.println("Nombre completo: " + getNombreCompleto());
        System.out.println("Cédula: " + getCedula());
        System.out.println("Edad: " + getEdad());
        System.out.println("Cargo: " + getCargo());
        System.out.println("Turno: " + getTurno());
        System.out.printf("Salario bruto: %.2f\n", sistema.getSalarioBruto());
        System.out.printf("Descuento por seguro social: %.2f\n", sistema.getSeguroSocial());
        System.out.printf("Descuento por seguro educativo: %.2f\n", sistema.getSeguroEducativo());
        System.out.printf("Salario neto: %.2f\n", sistema.getSalarioNeto());
    }


    public int getEdad() {
        return edad;
    }

    public String getCargo() {
        return cargo;
    }

    public String getCedula() {
        return cedula;
    }

    public String getFechaNacimiento() {
        return fechaNacimiento;
    }

    public String getNombreCompleto() {
        return nombreCompleto;
    }

    public String getTurno() {
        return turno;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public void setCedula(String cedula) {
        this.cedula = cedula;
    }

    public void setFechaNacimiento(String fechaNacimiento, int dia, int mes, int anio) {
        int edad;

        edad=2025-anio;

        if (mes == 06 && dia>11){
            edad-=1;
        }
        if (mes>06){
            edad-=1;
        }

        setEdad(edad);
        this.fechaNacimiento = fechaNacimiento;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public void setNombreCompleto(String nombreCompleto) {
        this.nombreCompleto = nombreCompleto;
    }

    public void setTurno(String turno) {
        this.turno = turno;
    }
}
