package Lab8;

import Lab8.problema1.InterfazProblema1;
import Lab8.problema2.Problema2;
import Lab8.problema3.Problema3;

import javax.swing.*;
import java.awt.event.ActionListener;

public class panelPrincipal extends JFrame{
    private JPanel JPpanelPrincipal;
    private JRadioButton botonProblema1;
    private JRadioButton botonProblema2;
    private JRadioButton botonProblema3;
    private JButton botonSiguiente;
    private JButton botonSalir;

    public panelPrincipal () {

        botonProblema1.addActionListener(ActionListener->{
           if(botonProblema1.isSelected()){
               botonProblema2.setSelected(false);
               botonProblema3.setSelected(false);
           }
        });

        botonProblema2.addActionListener(ActionListener->{
            if(botonProblema2.isSelected()){
                botonProblema3.setSelected(false);
                botonProblema1.setSelected(false);
            }
        });

        botonProblema3.addActionListener(ActionListener->{
            if(botonProblema3.isSelected()){
                botonProblema1.setSelected(false);
                botonProblema2.setSelected(false);
            }
        });

        botonSiguiente.addActionListener(ActionListener-> {
            try {
                if (botonProblema1.isSelected()) {
                    //menu problema 1
                    InterfazProblema1 interfazProblema1 = new InterfazProblema1();
                    interfazProblema1.setVisible(true);
                }
                else if (botonProblema2.isSelected()) {
                    //menu problema 2
                    Problema2 problema2 = new Problema2();
                    problema2.setVisible(true);
                }
                else if (botonProblema3.isSelected()) {
                    //menu problema 3
                    Problema3 problema3 = new Problema3();
                    problema3.setVisible(true);
                }
                else throw new RuntimeException();


            }
            catch (RuntimeException ex) {
                JOptionPane.showMessageDialog(null, "Seleccione una opción");
            }


        });


        botonSalir.addActionListener(ActionListener->{
            int opcion = JOptionPane.showConfirmDialog(
                    null,
                    "¿Estás seguro de que deseas cerrar el programa?",
                    "Cerrar Programa",
                    JOptionPane.YES_NO_OPTION
            );
            if (opcion == JOptionPane.YES_OPTION){
                System.exit(0);
            }
            else return;
        });

    }


    public JPanel getJPpanelPrincipal() {
        return JPpanelPrincipal;
    }
}
