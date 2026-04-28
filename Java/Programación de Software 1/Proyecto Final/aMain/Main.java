package aMain;

import bInterfaz.InterfazCuenta;
import bInterfaz.InterfazPrincipal;
import cSistema.aUsuario.Cliente;
import cSistema.aUsuario.Cuenta;
import cSistema.cServicios.Agenda;
import cSistema.cServicios.Cita;

import javax.swing.*;
import java.awt.*;

//Grupo:
//Aaron Remarchuk   8-1042-134
//Luis King         8-1017-548
//Edwin Rodriguez   8-975-208
//Kevin Kakiyama    8-1025-1743

public class Main extends JFrame {


    private JPanel JPanelInicio;
    private JButton iniciarButton;
    private JLabel logoUTP;
    private JLabel logoFISC;
    private JButton salirButton;
    private JLabel txtLABEL;
    private JLabel textoSuperior;
    private int cantUsuariosActuales = 0;


    public Main(){
        //frame principal
        JFrame frame = new JFrame("Proyecto Final");
        frame.setVisible(true);
        frame.setContentPane(getJPanelInicio());
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        frame.setSize(720,480);
        frame.setResizable(true);
        frame.setLocationRelativeTo(null);

        //ir a la pantalla principal
        iniciarButton.addActionListener(ActionListener->{
            Cita c;
            Cuenta[] cuenta=new Cuenta[10];
            frame.dispose();
            //datos de ejemplos
            cuenta[0] = new Cuenta("usuario","1234",new Cliente("1","Cuenta Ejemplo",111111,"correoEjemplo@gmail.com"));
            cantUsuariosActuales++;

            cSistema.cServicios.Cliente cliente = new cSistema.cServicios.Cliente("Cliente de Ejemplo");
            c = new Cita(cliente,"Detailing de Interiores","Taller","26 de Julio de 2025","9-11 AM");
            Agenda agenda = new Agenda();
            agenda.agendarCita(c);

            new InterfazPrincipal(cuenta,agenda,cantUsuariosActuales);
        });

        salirButton.addActionListener(ActionListener->{
            System.exit(0);
        });


        ImageIcon iconFisc = new ImageIcon(getClass().getResource("/images/FISC logo.png"));
        ImageIcon iconUTP = new ImageIcon(getClass().getResource("/images/UTP logo.png"));
        logoFISC.setIcon(new ImageIcon(iconFisc.getImage().getScaledInstance(100,100,Image.SCALE_SMOOTH)));
        logoUTP.setIcon(new ImageIcon(iconUTP.getImage().getScaledInstance(100,100,Image.SCALE_SMOOTH)));
    }

    public static void main(String[] args) {
        new Main();
    }

    private JPanel getJPanelInicio() {
        return JPanelInicio;
    }
}
