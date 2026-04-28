//Grupo:
//Aaron Remarchuk   8-1042-134
//Luis King         8-1017-548
//Edwin Rodriguez   8-975-208

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) {
        String cedula=null, nombre=null, departamento=null;
        double salarioBruto=0,deducciones=0;
        boolean verificar=true;
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        Empleado empleado1 = new Empleado();
        Salario salarioEmpleado1 = new Salario();
        do {
            try {
                System.out.println("Datos del empleado");
                System.out.print("Nombre: ");
                nombre = reader.readLine();
                empleado1.setNombre(nombre);


                System.out.print("Departamento: ");
                departamento = reader.readLine();
                empleado1.setDepartamento(departamento);

                System.out.print("ID del empleado: ");
                cedula = reader.readLine();
                empleado1.setCedula(cedula);
                verificar=false;

            } catch (Excepciones e) {
                System.out.println("Error: " + e.getMessage());
                verificar = true;
            } catch (IOException e) {
                System.out.println(e.getMessage());
                verificar = true;
            }
        }while (verificar);

        do {
            try{
                System.out.print("Salario bruto mensual: $");
                salarioBruto = Double.parseDouble(reader.readLine());
                salarioEmpleado1.setSalario(salarioBruto);
                System.out.print("Deducciones adicionales: $");
                deducciones= Double.parseDouble(reader.readLine());
                salarioEmpleado1.setDeducciones(deducciones);

                verificar = false;
            }catch (ExcepcionesSalario e){
                System.out.println("Error: "+e.getMessage());
                verificar=true;
            }
            catch (NumberFormatException e){
                System.out.println("Error: Ingrese solo números " + e.getMessage());
                verificar = true;
            }
            catch (IOException e){
                System.out.println(e.getMessage());
                verificar = true;
            }
        }while (verificar);


        empleado1.setSalarioBruto(salarioEmpleado1.getSalarioBruto());
        empleado1.setSalarioNeto(salarioEmpleado1.getSalarioNeto());

        System.out.printf("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s\n","Nombre", "Cédula", "Departamento", "Salario Bruto","Seguro Educativo", "Seguro Social", "Deducciones","Salario Neto");
        System.out.printf("%-15s %-15s %-15s $%-15.2f $%-15.2f $%-15.2f $%-15.2f $%-15.2f",empleado1.getNombre(),empleado1.getCedula(),empleado1.getDepartamento(),empleado1.getSalarioBruto(),salarioEmpleado1.getSeguroEducativo(),salarioEmpleado1.getSeguroSocial(),salarioEmpleado1.getDeducciones(),empleado1.getSalarioNeto());
        
    }

}
