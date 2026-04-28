package Lab8;

//Grupo:
//Aaron Remarchuk   8-1042-134
//Luis King         8-1017-548
//Edwin Rodriguez   8-975-208
//Kevin Kakiyama    8-1025-1743

import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Laboratorio 8");
        frame.setContentPane(new panelPrincipal().getJPpanelPrincipal());
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        frame.setSize(720,480);
        frame.setResizable(true);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);

    }
}
