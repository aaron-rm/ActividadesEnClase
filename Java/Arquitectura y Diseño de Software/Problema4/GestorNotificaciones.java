package Problema4;


public class GestorNotificaciones {
    private Notificacion[] notificacion;

    public GestorNotificaciones(Notificacion[] notif){
        this.notificacion = notif;
    }

    public void enviarNotificacion(int opcion){
        notificacion[opcion].enviar();
    }

    public void marcarComoLeida(int opcion){
        notificacion[opcion].marcarComoLeida();
    }
}
