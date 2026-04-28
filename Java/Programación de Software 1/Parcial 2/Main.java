
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        int cantEmpleados=0;
        while (true){
            try {
                BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
                System.out.printf("\nInserte la cantidad de empleados: ");
                cantEmpleados=numPositivo(Integer.parseInt(reader.readLine()));


                for (int i=1;i<=cantEmpleados;i++){
                    Empleado empleado = new Empleado();
                    System.out.printf("\n\nDatos del empleado %d\n",i);

                    while (true){
                        System.out.println("Nombre completo:");
                        String nombreCompleto = reader.readLine().trim();
                        if (nombreCompleto.matches(".*\\d.*")||nombreCompleto.matches("")) {
                            System.err.printf("\nError: ingrese un nombre válido\n");
                            continue;
                        }else {
                            empleado.setNombreCompleto(nombreCompleto);
                            break;
                        }
                    }


                    while (true){
                        System.out.println("Cédula:");
                        String cedula = reader.readLine().trim();
                        if (cedula.length()>15||cedula.length()<7){
                            System.err.println("Error: ingrese una cédula válida");
                            continue;
                        }else if (cedula.matches("[A-Z]")||cedula.matches("")){
                            System.err.println("Error: ingrese una cédula válida");
                            continue;
                        }else {
                            empleado.setCedula(cedula);
                            break;
                        }
                    }

                    while (true){
                        System.out.printf("\nFecha de nacimiento (dd/mm/aaaa):\t");
                        String fecha = reader.readLine();
                        if (fecha.length()!=10){
                            System.err.println("Error: ingrese el formato adecuado (dd/mm/AAAA), puede incluir '/' o '-'");
                            System.err.println("De ser necesario, poner 0 antes del dia o mes");
                            continue;
                        }

                        int dia,mes,anio;
                        boolean bisiesto=false;
                        anio=Integer.parseInt(fecha.substring(6,10));
                        if (anio>2006 || anio<1960){
                            System.err.println("Error: ingrese un año correcto");
                            continue;
                        }
                        if ((anio % 4 == 0) && ((anio % 100 != 0) || (anio % 400 == 0))){
                            bisiesto=true;
                        }

                        mes=Integer.parseInt(fecha.substring(3,5));
                        if (mes<1 || mes>12){
                            System.err.println("Error: ingrese un año correcto");
                            continue;
                        }

                        dia=Integer.parseInt(fecha.substring(0,2));
                        if (dia<1){
                            System.err.println("Error: ingrese un día correcto");
                            continue;
                        }

                        if (mes == 2){
                            if (bisiesto){
                                if (dia>29){
                                    System.err.println("Error: ingrese un día correcto");
                                    continue;
                                }
                            }else if (dia>28){
                                System.err.println("Error: ingrese un día correcto");
                                continue;
                            }
                        }

                        if (mes%2 == 0){
                            if (dia>31){
                                System.err.println("Error: ingrese un día correcto");
                                continue;
                            }
                        }else {
                            if (dia>30){
                                System.err.println("Error: ingrese un día correcto");
                                continue;
                            }
                        }
                        empleado.setFechaNacimiento(fecha,dia,mes,anio);
                        break;
                    }


                    while (true){
                        System.out.printf("\n\nCargo \n1-Empacador\n2-Maquinista\n3-supervisor\nCargo:\t");
                        int eleccionCargo = numPositivo(Integer.parseInt(reader.readLine()));
                        if (eleccionCargo>3){
                            System.err.println("Error: elegir una opción válida");
                            continue;
                        }
                        switch (eleccionCargo){
                            case 1:{
                                empleado.setCargo("Empacador");
                                empleado.sistema.setSalarioBruto(500.00);
                                break;
                            }

                            case 2:{
                                empleado.setCargo("Maquinista");
                                empleado.sistema.setSalarioBruto(600.00);
                                break;
                            }

                            case 3:{
                                empleado.setCargo("Supervisor");
                                empleado.sistema.setSalarioBruto(700.00);
                                break;
                            }

                            default:{
                                System.err.println("Error: elegir una opción válida");
                                continue;
                            }
                        }
                        break;
                    }


                    while (true){
                        System.out.printf("\n\nTurno\n1-(7:00am-2:59pm)\n2-(3:00pm-10:59pm)\n3-(11:00pm-6:59am)\nTurno:\t");
                        int eleccionCargo = numPositivo(Integer.parseInt(reader.readLine()));
                        if (eleccionCargo>3){
                            System.err.println("Error: elegir una opción válida");
                            continue;
                        }
                        switch (eleccionCargo){
                            case 1:{
                                empleado.setTurno("(7:00am-2:59pm)");
                                break;
                            }

                            case 2:{
                                empleado.setTurno("(3:00pm-10:59pm)");
                                break;
                            }

                            case 3:{
                                empleado.setTurno("(11:00pm-6:59am)");
                                empleado.sistema.setSalarioBruto(empleado.sistema.getSalarioBruto()+(empleado.sistema.getSalarioBruto()*0.05));
                                break;
                            }

                            default:{
                                System.err.println("Error: elegir una opción válida");
                                continue;
                            }
                        }
                        break;
                    }

                    empleado.mostrarInformacion(i);
                }
                break;
            }
            catch (RuntimeException e) {
                System.err.println("Error: " + e.getMessage());
                continue;
            }
            catch (IOException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }
        }
    }

    static int numPositivo(int n) throws numeroPositivo{
        if (n<=0){
            throw new numeroPositivo("inserte un número positivo");
        }
        return n;
    }
}
