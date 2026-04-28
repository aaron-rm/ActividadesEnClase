//Aaron Remarchuk 8-1042-134


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        int n=0, nuevaCant=0, opcion;
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        Productos[] listaProductos = new Productos[0];

        while(true){

            try {
                System.out.println("Menú de Opciones");
                System.out.println("1. Ingresar productos iniciales");
                System.out.println("2. Ingresar nuevos productos");
                System.out.println("3. Ver Productos");
                System.out.println("4. Verificar fecha de Vencimiento");
                System.out.println("5. Salir");

                do {
                    System.out.print("Ingrese una opción: ");
                    opcion = Integer.parseInt(reader.readLine());
                    if(opcion < 1 || opcion > 5){
                        throw new NumberFormatException();
                    }
                }while (opcion < 1 || opcion > 5);

                switch (opcion){
                    case 1:{
                        System.out.print("Ingrese la cantidad de productos: ");
                        n = Integer.parseInt(reader.readLine());
                        listaProductos = new Productos[n];
                        for (int i = 0; i < n; i++) {
                            System.out.println("Ingrese información del producto "+ (i+1));
                            listaProductos[i] = new Productos();

                        }
                        nuevaCant=n;
                        continue;
                    }
                    case 2:{
                        Productos[] listaTemporal;
                        System.out.print("Cantidad de productos a agregar: ");
                        nuevaCant = n + Integer.parseInt(reader.readLine());
                        listaTemporal = new Productos[nuevaCant];

                        for (int i = 0; i < listaProductos.length; i++) {
                            listaTemporal[i] = new Productos(listaProductos[i]);
                        }

                        listaProductos = listaTemporal.clone();

                        for (int i = n; i < nuevaCant; i++) {
                            System.out.println("Ingrese información del producto "+ (i+1));
                            listaProductos[i] = new Productos();
                        }


                        continue;
                    }
                    case 3:{
                        if(nuevaCant == 0){
                            System.err.println("No hay productos en existencia");
                        }else for (int i = 0; i < nuevaCant; i++) {
                            System.out.println("Producto " + (i+1));
                            listaProductos[i].imprimirInformacion();
                        }


                        continue;
                    }
                    case 4:{
                        if(nuevaCant == 0){
                            System.err.println("No hay productos en existencia");
                        }else{
                            int c;
                            do {
                            System.out.print("Ingrese el producto que desea verificar: ");
                                c = Integer.parseInt(reader.readLine())-1;
                                if(c<0 || c>nuevaCant){
                                    System.out.println("El producto que desea verificar no existe");
                                    continue;
                                }
                                break;
                            }while (true);

                            listaProductos[c].verificarGarantia();
                        }

                            continue;
                    }
                    case 5:{
                        break;
                    }
                    default:{
                        throw new RuntimeException("Ingrese un número correcto");
                    }
                }
            }
            catch (NumberFormatException e) {
                System.out.println();
                System.err.println("Ingrese un valor válido");
                continue;
            }
            catch(IOException e){
                System.out.println();
                System.err.println(e.getMessage());
                continue;
            }
            catch (RuntimeException e){
                System.out.println();
                System.err.println(e.getMessage());
                continue;
            }
            catch (Exception e) {
                System.out.println();
                System.err.println(e.getMessage());
                continue;
            }
            finally{
                System.out.println();
                System.out.println("Volviendo al menú...");
                System.out.println();
                System.out.println();
                System.out.println();
            }
            break;
        }
        System.out.println("Saliendo del sistema...");
    }
}
