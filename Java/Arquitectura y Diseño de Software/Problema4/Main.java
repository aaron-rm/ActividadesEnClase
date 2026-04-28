package Problema4;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        try {
            System.out.print("Cant de notif: ");
            int cantidad = Integer.parseInt(in.readLine());
            Notificacion[] notificacion = new Notificacion[cantidad];

            for(int i = 0; i < cantidad; i++){
                System.out.println("Notificación" + (i + 1) + ":");
                System.out.println("Mensaje: ");
                String mensaje = in.readLine();
                notificacion[i] = new Notificacion(mensaje);
            }

            GestorNotificaciones gestor = new GestorNotificaciones(notificacion);
            System.out.printf("Seleccione una opción \n" +
                    "1- Enviar notificación\n" +
                    "2- Mostrar notificaciones\n" +
                    "3- Salir\n");
            int opcion = Integer.parseInt(in.readLine());
            switch (opcion){
                case 1:{
                    gestor.enviarNotificacion(opcion);
                    break;
                }
                case 2:{
                    gestor.marcarComoLeida(opcion);
                    break;
                }
                case 3:{
                    System.out.println("Saliendo...");
                    break;
                }
                default:{
                    System.err.println("Error");
                }
            }
        }catch(Exception e){
            System.err.println(e.getMessage());
        }
    }
}
