package Lab8.problema2;

import javax.swing.*;

public class Problema2 extends JFrame{
    private JButton botonVolver;
    private JPanel JPProblema2;
    private JButton botonSiguiente;
    private JList<Integer> list1;
    private JTextField txtInferior;
    private JTextField txtSuperior;
    private JTextArea indicaciones;
    private JLabel resultado;
    private JScrollPane JSPResultado;
    private JCheckBox checkBoxExtra;
    private DefaultListModel<Integer> listModel;

    public Problema2(){
        setTitle("Problema 2");
        setSize(720,480);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setContentPane(getJPProblema2());
        list1.setVisible(false);
        listModel = new DefaultListModel<>();
        resultado.setVisible(false);
        JSPResultado.setVisible(false);
        checkBoxExtra.setVisible(false);


        botonSiguiente.addActionListener(ActionListener->{
            listModel.clear();
            resultado.setVisible(false);
            JSPResultado.setVisible(false);


            Problema2Logica problema2Logica = new Problema2Logica(txtInferior.getText(),txtSuperior.getText());
            problema2Logica.getLista(listModel,checkBoxExtra);

            resultado.setVisible(true);
            list1.setModel(listModel);
            list1.setVisible(true);
            JSPResultado.setVisible(true);
            checkBoxExtra.setVisible(true);

        });

        botonVolver.addActionListener(ActionListener->{
            this.dispose();
        });


    }

    public JPanel getJPProblema2() {
        return JPProblema2;
    }



}
