
public class Salario {
    private double deducciones, salarioBruto, salarioNeto, seguroSocial, seguroEducativo;
    public Salario(){
        this.salarioBruto=0;
        this.salarioNeto=0;
        this.deducciones=0;
        this.seguroSocial=0.0975;
        this.seguroEducativo=0.0125;
    }


    public void setSalario(double salario) throws ExcepcionesSalario{
        if(salario<0){
            throw new ExcepcionesSalario("Salario no puede ser negativo");
        }else this.salarioBruto = salario;
    }

    public void setDeducciones(double deducciones) throws ExcepcionesSalario{
        if(deducciones<0){
            throw new ExcepcionesSalario("Deducciones no puede ser negativo");
        }else this.deducciones = deducciones;
    }

    public double getSalarioNeto(){
        return (getSalarioBruto()-getSeguroEducativo()-getSeguroSocial()-getDeducciones());
    }

    public double getDeducciones() {
        return deducciones;
    }

    public double getSalarioBruto() {
        return salarioBruto;
    }

    public double getSeguroEducativo() {
        return (seguroEducativo*salarioBruto);
    }

    public double getSeguroSocial() {
        return (seguroSocial*salarioBruto);
    }

}
