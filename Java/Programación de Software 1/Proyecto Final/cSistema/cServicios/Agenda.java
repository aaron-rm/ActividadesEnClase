package cSistema.cServicios;

public class Agenda {
    private Cita[] citas;
    private int contador;

    public Agenda() {
        citas = new Cita[100];  // Capacidad máxima de 100 citas
        contador = 0;
    }

    public boolean agendarCita(Cita nueva) {
        // Verificar si ya existe una cita con la misma fecha, horario y método
        for (int i = 0; i < contador; i++) {
            Cita existente = citas[i];
            if (existente.getFecha().equals(nueva.getFecha()) &&
                    existente.getHorario().equals(nueva.getHorario()) &&
                    existente.getMetodoServicio().equals(nueva.getMetodoServicio())) {
                return false; // Cita duplicada para ese horario y método
            }
        }

        // Agregar la cita si no está duplicada y hay espacio
        if (contador < citas.length) {
            citas[contador] = nueva;
            contador++;
            return true;
        }

        return false; // No hay espacio
    }

    public Cita[] getCitas() {
        return citas;
    }
}

