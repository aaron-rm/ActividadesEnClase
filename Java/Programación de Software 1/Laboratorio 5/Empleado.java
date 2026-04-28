
public class Empleado {
    private String cedula, nombre, departamento;
    double salarioBruto,salarioNeto;

    public Empleado(){
        this.cedula="";
        this.nombre="";
        this.departamento="";
        this.salarioBruto=0;
        this.salarioNeto=0;
    }

    public void setNombre(String nombre) throws Excepciones{
        if(nombre.matches("[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+")){
            this.nombre=nombre;
        }else throw new Excepciones("Nombre no puede tener números o carácteres especiales");
    }

    public void setDepartamento(String departamento) throws Excepciones{
        if(departamento.matches("[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+")){
            this.departamento=departamento;
        }else throw new Excepciones("Departamento no puede tener números o carácteres especiales");
    }

    public void setSalarioBruto(double salarioBruto) {
        this.salarioBruto = salarioBruto;
    }

    public void setSalarioNeto(double salarioNeto) {
        this.salarioNeto = salarioNeto;
    }

    public void setCedula(String cedula) throws Excepciones{
        if(cedula.matches("[a-zA-Z0-9\\-]+")){
            this.cedula = cedula;
        }else throw new Excepciones("La cédula no puede contener caracteres especiales");

    }

    public String getNombre() {
        return nombre;
    }

    public double getSalarioBruto() {
        return salarioBruto;
    }

    public double getSalarioNeto() {
        return salarioNeto;
    }

    public String getCedula() {
        return cedula;
    }

    public String getDepartamento() {
        return departamento;
    }
}
