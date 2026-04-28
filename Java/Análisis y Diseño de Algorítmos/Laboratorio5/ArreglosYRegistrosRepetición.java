
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Empleado{
    String nombre;
    int horas;
    float pago;

    Empleado (String nombre, int horas, float pago){
        this.nombre=nombre;
        this.horas=horas;
        this.pago=pago;
    }

    public String getNombre() {
        return nombre;
    }

    public float getSalario() {
        return pago*horas;
    }
}

public class ArreglosYRegistrosRepetición {
    public static void main(String[] args) throws IOException {
        Empleado[] empleados = new Empleado[10];
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        for (int i=0;i<10;i++){
            System.out.printf("Empleado %d: \n",i+1);
            System.out.print("Nombre: ");
            String nombre = reader.readLine();
            System.out.print("Horas: ");
            int horas = Integer.parseInt(reader.readLine());
            System.out.print("Pago por hora: ");
            float pago = Float.parseFloat(reader.readLine());
            empleados[i] = new Empleado(nombre, horas, pago);
        }

        float salarioTotal = 0;
        for (int i=0;i<10;i++){
            System.out.printf("Empleado %d: \n",i+1);
            System.out.println("Nombre: " + empleados[i].getNombre());
            System.out.println("Salario: " + empleados[i].getSalario());
            salarioTotal += empleados[i].getSalario();
            }
        System.out.println("Salario Total: " + salarioTotal);
    }
}
