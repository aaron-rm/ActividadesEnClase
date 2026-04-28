package Lab8.problema1;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

    public class InterfazProblema1 extends JFrame {

        private JTextField campoPalabra;
        private JButton botonProcesar, botonReintentar, botonMenu;
        private JList<String> listaVocales;
        private DefaultListModel<String> modeloLista;

        public InterfazProblema1() {
            setTitle("Problema 1 - Contar Vocales");
            setSize(500, 350);
            setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
            setLayout(new BorderLayout());

            // Panel superior con el campo de texto
            JPanel panelSuperior = new JPanel();
            panelSuperior.setLayout(new FlowLayout());
            panelSuperior.add(new JLabel("Ingrese una palabra:"));
            campoPalabra = new JTextField(20);
            panelSuperior.add(campoPalabra);

            botonProcesar = new JButton("Procesar");
            panelSuperior.add(botonProcesar);

            add(panelSuperior, BorderLayout.NORTH);

            // Panel central con la lista
            modeloLista = new DefaultListModel<>();
            listaVocales = new JList<>(modeloLista);
            JScrollPane scrollPane = new JScrollPane(listaVocales);
            add(scrollPane, BorderLayout.CENTER);

            // Panel inferior con botones adicionales
            JPanel panelInferior = new JPanel();
            panelInferior.setLayout(new FlowLayout());

            botonReintentar = new JButton("Limpiar");
            botonMenu = new JButton("Regresar al menú principal");

            panelInferior.add(botonReintentar);
            panelInferior.add(botonMenu);

            add(panelInferior, BorderLayout.SOUTH);

            // Acciones
            botonProcesar.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    procesarPalabra();
                }
            });

            botonReintentar.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    campoPalabra.setText("");
                    modeloLista.clear();
                    campoPalabra.requestFocus();
                }
            });

            botonMenu.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    dispose(); // cerrar esta ventana
                }
            });

            setLocationRelativeTo(null); // Centrar ventana
        }

        private void procesarPalabra() {
            modeloLista.clear();
            String palabra = campoPalabra.getText().trim();

            if (!palabra.matches("[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\\s]+")) {
                JOptionPane.showMessageDialog(this,
                        "Por favor ingrese solo letras y espacios. No se permiten números ni símbolos.",
                        "Entrada inválida",
                        JOptionPane.ERROR_MESSAGE);
                return;
            }

            // Eliminar espacios para contar solo letras reales
            String palabraSinEspacios = palabra.replaceAll("\\s+", "");

            char[] vocales = ProcesadorVocales.obtenerVocales(palabraSinEspacios);

            if (vocales.length == 0) {
                JOptionPane.showMessageDialog(this,
                        "No se encontraron vocales.",
                        "Resultado",
                        JOptionPane.INFORMATION_MESSAGE);
            } else {
                StringBuilder resultado = new StringBuilder();
                for (int i = 0; i < vocales.length; i++) {
                    modeloLista.addElement(String.valueOf(vocales[i]));
                    resultado.append(vocales[i]);
                    if (i != vocales.length - 1) {
                        resultado.append(", ");
                    }
                }

                JOptionPane.showMessageDialog(this,
                        "Se encontraron " + vocales.length + " vocales, las cuales son las siguientes:\n" + resultado.toString(),
                        "Resultado",
                        JOptionPane.INFORMATION_MESSAGE);
            }
        }
    }

