
public class Sistema {
    private double salarioBruto,seguroSocial,seguroEducativo,salarioNeto;

    public Sistema(){
        this.salarioBruto=0;
        this.seguroEducativo=0;
        this.seguroSocial=0;
        this.salarioNeto=0;
    }

    public void setSalarioBruto(double salarioBruto) {
        this.salarioBruto = salarioBruto;
    }

    public double getSalarioBruto() {
        return salarioBruto;
    }

    public double getSalarioNeto() {
        return (getSalarioBruto()-getSeguroEducativo()-getSeguroSocial());
    }

    public double getSeguroEducativo() {
        return (getSalarioBruto()*0.0125);
    }

    public double getSeguroSocial() {
        return (getSalarioBruto()*0.0975);
    }
}
