package problema1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


//Integrantes:
//Aaron Remarchuk   8-1042-134
//Edwin Rodriguez   8-975-208
//Luis King         8-1017-548

public class Main {
    public static void main(String[] args) {
        BufferedReader buffer = new BufferedReader(new InputStreamReader(System.in));
        String id="", nombre="";
        int velocidad=0,tipoVia=0;
        boolean bool1;


        try{
            System.out.print("Nombre del Conductor: ");
            nombre = buffer.readLine();
            System.out.print("ID del Conductor: ");
            id = buffer.readLine();
        }   catch(IOException e){
            e.printStackTrace();
            }

        do{
            bool1=false;
            try{
                do{
                    System.out.print("Velocidad del vehículo en km/h: ");
                    velocidad = Integer.parseInt(buffer.readLine());
                    if(velocidad<0 || velocidad>300){
                        System.out.println("Inserte una velocidad válida");
                    }
                }while(velocidad<0|| velocidad>300);

                System.out.println("Tipo de via que transitaba");
                System.out.printf("1-Residencial \n2-Escolar\n3-Autopista\n");
                do{
                    System.out.print("Inserte el número: ");
                    tipoVia = Integer.parseInt(buffer.readLine());
                    if(tipoVia<1 || tipoVia>3){
                        System.out.println("Inserte una via válida");
                    }
                }while(tipoVia<1 || tipoVia>3);

            }   catch(NumberFormatException e){
                    System.out.println("Error " +e.getMessage()+", Ingrese un valor numérico válido");
                    bool1 = true;
                }
                catch (IOException e){
                e.printStackTrace();
                }
        } while(bool1);

        Multa multa1 = new Multa(nombre,id,tipoVia,velocidad);
        multa1.informacionMulta();
    }
}