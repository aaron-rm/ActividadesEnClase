
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int i=0, cantClientes=0, contClientes=0, contHombres=0, contMujeres=0, sexo=0;
        boolean aplicaPrestamo=true;
        double salario=0, prestamo=0, prestamoTotal=0;
        String nombre="";

        while (true){
            try {
                System.out.print("Inserte la cantidad de clientes: ");
                cantClientes = Integer.parseInt(reader.readLine());
                if (cantClientes <=0){
                    throw new RuntimeException("Clientes debe ser mayor a 0");
                }

                for (i=1;i<=cantClientes;i++) {
                    System.out.println("Datos del Cliente " + i);
                    do {
                        System.out.print("Nombre: ");
                        nombre = reader.readLine().trim();
                        if (nombre.matches("")){
                            System.out.println("Ingrese un nombre correcto");
                        }
                    }while (nombre.matches(""));

                    do{
                        System.out.printf("1-Hombre\n2-Mujer\n");
                        System.out.print("Sexo: ");
                        sexo = Integer.parseInt(reader.readLine());
                        if (sexo < 1 || sexo > 2){
                            System.out.println("Ingrese un sexo correcto");
                        }
                    }while (sexo < 1 || sexo > 2);

                    System.out.print("Salario: ");
                    salario = Double.parseDouble(reader.readLine());
                    if (salario < 800.00) {
                        System.out.println("Cliente no aplica para préstamo");
                        aplicaPrestamo = false;
                    }else aplicaPrestamo = true;

                    if (aplicaPrestamo) {
                        if (prestamoTotal >= 1000000.00){
                            System.out.println("Límite diario superado");
                            System.out.println("El préstamo no fue aprobado");
                            continue;
                        }else
                        while (true){
                            System.out.print("Monto del préstamo: ");
                            prestamo = Double.parseDouble(reader.readLine());
                            if (prestamo>=25000.00 && prestamo<=400000.00){
                                prestamoTotal+=prestamo;
                                if(prestamoTotal<=1000000.00){
                                    contClientes++;
                                    if (sexo == 1){
                                        contHombres++;
                                    }else contMujeres++;
                                    System.out.println("El préstamo fue aprobado");
                                    break;
                                }else {
                                    System.out.println("El préstamo sobrepasa el límite diario");
                                    System.out.println("Ingrese una cantidad menor a " + (prestamoTotal-1000000));
                                    prestamoTotal-=prestamo;
                                    continue;
                                }
                            }else{
                                System.out.println("Ingrese un préstamo entre 25mil y 400mil B/.");
                                continue;
                            }
                        }
                    }
                }
                System.out.println("Cantidad de clientes tramitados: " + cantClientes);
                System.out.println("Cantidad de clientes con préstamo aprobado: " + contClientes);
                System.out.println("Cantidad de hombres con préstamo aprobado: "+ contHombres);
                System.out.println("Cantidad de mujeres con préstamo aprobado: "+ contMujeres);
            }
            catch (NumberFormatException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }
            catch (RuntimeException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }
            catch (IOException e){
                System.err.println("Error: " + e.getMessage());
                continue;
            }
            break;
        }
    }
}
