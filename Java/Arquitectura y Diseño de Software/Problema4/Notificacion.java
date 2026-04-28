package Problema4;

import java.time.LocalDateTime;

public class Notificacion {
    private String mensaje;
    private LocalDateTime fecha;
    private int estado;

    //Para estado
    // 1- pendiente
    // 2- enviada
    // 3- recibida

    public Notificacion(String mensaje) {
        this.mensaje = mensaje;
        estado = 1;
    }

    public void getEstado(){
        if(estado == 1){
            System.out.println("Pendiente por enviar");
        }else if(estado == 2){
            System.out.println("Envianda");
        }else if(estado == 3){
            System.out.println("Recibida");
        }
    }
    public void enviar(){
        estado = 2;
        System.out.println("Enviando notificacion...");
    }

    public void marcarComoLeida(){
        if(estado == 2){
            estado = 3;
            System.out.println("Notificación marcada como leida");
        }else{
            System.out.println("No se ha encontrado notificación");
        }
    }
}
