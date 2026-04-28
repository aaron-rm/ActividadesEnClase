//Grupo:
//Aaron Remarchuk   8-1042-134
//Luis King         8-1017-548
//Edwin Rodriguez   8-975-208

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int opcion=0;
        while (true){
            try {
                System.out.printf("\nMenú de opciones\n");
                System.out.println("1- Calcular factorial");
                System.out.println("2- Calcular suma de digitos");
                System.out.println("3- Contar números primos");
                System.out.println("4- Encontrar el número más grande");
                System.out.println("5- Salir");
                System.out.print("Selecciones una opción (ingrese el número): ");
                opcion = Integer.parseInt(reader.readLine());

                if (opcion <= 0 || opcion > 5) {
                    System.err.println("Error: Ingrese un número entre 1 y 5");
                    continue;
                }
                if (opcion == 5) {
                    break;
                }

                switch (opcion){
                    case 1:{
                        int num=0;
                        Problema1 problema1 = new Problema1();

                        while(true){
                            System.out.printf("\nCálculo de factorial\n");
                            System.out.print("Ingrese el número: ");
                            num=Integer.parseInt(reader.readLine());

                            if(num<0){
                                System.err.println("Error: El número no puede ser negativo");
                                continue;
                            }

                            problema1.setNum(num);
                            System.out.printf("Factorial de " +problema1.getNum() + " = " +problema1.calcularFactorial());
                            System.out.println();
                            break;
                        }
                    }break;
                    case 2:{
                        Problema2 problema2 = new Problema2();
                        int num=0;

                        while (true){
                            System.out.printf("\nCálculo de suma de sus digitos\n");
                            System.out.print("Ingrese el número: ");
                            num=Integer.parseInt(reader.readLine());

                            if(num<0){
                                System.err.println("Error: El número no puede ser negativo");
                                continue;
                            }

                            problema2.setNum(num);
                            System.out.println("Suma de los digitos: "+problema2.calcularSuma());
                            System.out.println();
                            break;
                        }
                    }break;
                    case 3:{
                        Problema3 problema3 = new Problema3();
                        int numInf=0,numSup=0;


                        while (true){
                            System.out.printf("\nContar números primos\n");

                            System.out.print("Ingrese el número menor: ");
                            numInf=Integer.parseInt(reader.readLine());
                            if(numInf<0){
                                System.err.println("Error: El número no puede ser negativo");
                                continue;
                            }

                            System.out.print("Ingrese el número mayor: ");
                            numSup=Integer.parseInt(reader.readLine());
                            if(numSup<0){
                                System.err.println("Error: El número no puede ser negativo");
                                continue;
                            }

                            if(numInf>numSup){
                                System.err.println("Error: El segundo número no puede ser menor al primero");
                                continue;
                            }

                            problema3.setNuminf(numInf);
                            problema3.setNumsup(numSup);

                            problema3.mostrarNumPrimos();
                            System.out.println();
                            break;
                        }
                    }break;
                    case 4:{
                        Problema4 problema4 = new Problema4();
                        boolean condicion=true;
                        double num=0;
                        System.out.printf("\nEncontrar el número mas grande\n");
                        do{
                            System.out.print("Ingrese un número (negativo para salir): ");
                            num = Double.parseDouble(reader.readLine());
                            problema4.setNumMayor(num);
                        }while (num>=0);
                        System.out.println("El número más grande fue: "+problema4.getNumMayor());
                    }break;
                    default:{
                        System.err.println("Error");
                    }
                }


            }catch (NumberFormatException e){
                System.err.println("Ingrese un dato númerico: "+e.getMessage());
            }catch (IOException e){
                System.err.println("Error de entrada/salida: "+e.getMessage());
            }
        }
    }
}
