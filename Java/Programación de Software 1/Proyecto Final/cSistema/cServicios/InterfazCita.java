package cSistema.cServicios;

import bInterfaz.InterfazPrincipal;
import cSistema.aUsuario.Cuenta;

import javax.swing.*;
import java.awt.*;
import java.time.LocalDate;

public class InterfazCita extends JFrame {
    private JTextField txtNombre;
    private JComboBox<String> cmbDia, cmbMes, cmbAño; // cambio aquí
    private JButton btnAgendar;
    private JButton btnMenuPrincipal;
    private JLabel lblMensaje, lblGracias;

    private JButton btnInterior, btnExterior, btnCeramico, btnCompleto;
    private JButton btnTaller, btnDomicilio;
    private JButton btnH1, btnH2, btnH3;

    private String servicioSeleccionado = null;
    private String metodoSeleccionado = null;
    private String horarioSeleccionado = null;

    private JPanel contenedor, panelMenu, panelConfirmacion;
    private CardLayout cardLayout;
    private Agenda agenda;

    private int cantUsuariosActuales;
    private Cuenta[] usuarios;
    private Agenda citas;
    private final String[] nombresMeses = {
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    };

    public InterfazCita(Cuenta[] usuarios, Agenda citas,int cantUsuariosActuales) {
        super("Agendamiento de Servicios de Detailing");

        this.usuarios=usuarios;
        this.citas=citas;
        this.cantUsuariosActuales=cantUsuariosActuales;

        agenda = citas;
        contenedor = new JPanel();
        cardLayout = new CardLayout();
        contenedor.setLayout(cardLayout);

        crearPanelMenu();
        crearPanelConfirmacion();

        contenedor.add(panelMenu, "menu");
        contenedor.add(panelConfirmacion, "confirmacion");

        JPanel panelCentrado = new JPanel(new GridBagLayout());
        panelCentrado.add(contenedor);

        setContentPane(panelCentrado);
        setSize(500, 550);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    private void crearPanelMenu() {
        panelMenu = new JPanel();
        panelMenu.setLayout(new BoxLayout(panelMenu, BoxLayout.Y_AXIS));
        panelMenu.setBorder(BorderFactory.createEmptyBorder(20, 40, 20, 40));

        txtNombre = new JTextField();

        String[] dias = new String[31];
        for (int i = 1; i <= 31; i++) {
            dias[i - 1] = String.format("%02d", i);
        }
        cmbDia = new JComboBox<>(dias);

        cmbMes = new JComboBox<>(nombresMeses);

        String[] años = new String[6]; // cambio aquí
        for (int i = 0; i < 6; i++) {
            años[i] = String.valueOf(2025 + i);
        }
        cmbAño = new JComboBox<>(años); // cambio aquí

        btnAgendar = new JButton("Agendar");
        btnMenuPrincipal = new JButton("Volver al menú principal");
        lblMensaje = new JLabel("");
        lblMensaje.setAlignmentX(Component.CENTER_ALIGNMENT);

        // Servicio
        JPanel panelServicio = new JPanel(new GridLayout(2, 2, 10, 10));
        panelServicio.setAlignmentX(Component.CENTER_ALIGNMENT);
        btnInterior = crearBotonSeleccion("Detailing de Interiores", () -> servicioSeleccionado = "Detailing de Interiores", panelServicio);
        btnExterior = crearBotonSeleccion("Detailing de Exterior", () -> servicioSeleccionado = "Detailing de Exterior", panelServicio);
        btnCeramico = crearBotonSeleccion("Recubrimiento Ceramico", () -> servicioSeleccionado = "Recubrimiento Ceramico", panelServicio);
        btnCompleto = crearBotonSeleccion("Paquete Completo", () -> servicioSeleccionado = "Paquete Completo", panelServicio);

        // Método
        JPanel panelMetodo = new JPanel(new FlowLayout());
        panelMetodo.setAlignmentX(Component.CENTER_ALIGNMENT);
        btnTaller = crearBotonSeleccion("Taller", () -> metodoSeleccionado = "Taller", panelMetodo);
        btnDomicilio = crearBotonSeleccion("Domicilio", () -> metodoSeleccionado = "Domicilio", panelMetodo);

        // Horario
        JPanel panelHorario = new JPanel(new FlowLayout());
        panelHorario.setAlignmentX(Component.CENTER_ALIGNMENT);
        btnH1 = crearBotonSeleccion("9-11 AM", () -> horarioSeleccionado = "9-11 AM", panelHorario);
        btnH2 = crearBotonSeleccion("12-2 PM", () -> horarioSeleccionado = "12-2 PM", panelHorario);
        btnH3 = crearBotonSeleccion("2-4 PM", () -> horarioSeleccionado = "2-4 PM", panelHorario);

        // Campos
        panelMenu.add(labelConCentrado("Nombre del Cliente:"));
        panelMenu.add(campoConCentrado(txtNombre));

        panelMenu.add(labelConCentrado("Fecha (día - mes - año):"));
        JPanel panelFecha = new JPanel(new FlowLayout(FlowLayout.CENTER, 5, 0));
        panelFecha.add(cmbDia);
        panelFecha.add(cmbMes);
        panelFecha.add(cmbAño); // cambio aquí
        panelMenu.add(panelFecha);

        panelMenu.add(labelConCentrado("Servicio:"));
        panelMenu.add(panelServicio);
        panelMenu.add(labelConCentrado("Método de Servicio:"));
        panelMenu.add(panelMetodo);
        panelMenu.add(labelConCentrado("Horario:"));
        panelMenu.add(panelHorario);

        btnAgendar.setAlignmentX(Component.CENTER_ALIGNMENT);
        btnAgendar.addActionListener(e -> agendar());
        btnMenuPrincipal.setAlignmentX(Component.CENTER_ALIGNMENT);
        btnMenuPrincipal.addActionListener(e -> {
            dispose();
           new InterfazPrincipal(usuarios,citas,cantUsuariosActuales);
        });

        panelMenu.add(Box.createVerticalStrut(10));
        panelMenu.add(btnAgendar);
        panelMenu.add(lblMensaje);
        panelMenu.add(btnMenuPrincipal);
    }

    private void crearPanelConfirmacion() {
        panelConfirmacion = new JPanel(new GridBagLayout());

        lblGracias = new JLabel();
        lblGracias.setFont(new Font("Arial", Font.BOLD, 16));
        lblGracias.setHorizontalAlignment(SwingConstants.CENTER);

        JButton btnVolver = new JButton("Volver al menú principal");
        btnVolver.addActionListener(e -> {
            limpiarFormulario();
            dispose();
            new InterfazPrincipal(usuarios,citas,cantUsuariosActuales);
        });

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(10, 10, 20, 10);
        gbc.anchor = GridBagConstraints.CENTER;
        panelConfirmacion.add(lblGracias, gbc);

        gbc.gridy++;
        panelConfirmacion.add(btnVolver, gbc);
    }

    private void agendar() {
        try {
            String nombre = txtNombre.getText().trim();

            if (nombre.isEmpty() ||
                    servicioSeleccionado == null ||
                    metodoSeleccionado == null ||
                    horarioSeleccionado == null ||
                    cmbDia.getSelectedItem() == null ||
                    cmbMes.getSelectedItem() == null ||
                    cmbAño.getSelectedItem() == null) { // cambio aquí
                lblMensaje.setText("Debes completar todos los campos y seleccionar una opción por grupo.");
                return;
            }

            String dia = (String) cmbDia.getSelectedItem();
            int mesIndex = cmbMes.getSelectedIndex(); // Enero = 0
            String año = (String) cmbAño.getSelectedItem(); // cambio aquí

            LocalDate fechaSeleccionada;
            try {
                fechaSeleccionada = LocalDate.of(
                        Integer.parseInt(año),
                        mesIndex + 1,
                        Integer.parseInt(dia)
                );
            } catch (Exception ex) {
                lblMensaje.setText("Fecha inválida.");
                return;
            }

            // Validar que sea al menos desde mañana
            LocalDate hoy = LocalDate.now();
            if (!fechaSeleccionada.isAfter(hoy)) {
                lblMensaje.setText("La fecha debe ser al menos desde mañana.");
                return;
            }

            String fechaFormateada = String.format("%02d de %s de %d",
                    fechaSeleccionada.getDayOfMonth(),
                    nombresMeses[fechaSeleccionada.getMonthValue() - 1],
                    fechaSeleccionada.getYear());

            String fechaISO = fechaSeleccionada.toString();

            // Crear cita
            Cliente cliente = new Cliente(nombre);
            Cita cita = new Cita(cliente, servicioSeleccionado, metodoSeleccionado, fechaISO, horarioSeleccionado);
            boolean agendada = agenda.agendarCita(cita);

            if (agendada) {
                lblGracias.setText("<html><div style='text-align:center;'>Muchas gracias!<br>Tu cita fue registrada con éxito<br>para el día <b>"
                        + fechaFormateada + "</b> de <b>" + horarioSeleccionado + "</b></div></html>");
                cardLayout.show(contenedor, "confirmacion");
            } else {
                lblMensaje.setText("Horario lleno para ese servicio y método.");
            }
        } catch (Exception ex) {
            lblMensaje.setText("Error inesperado: " + ex.getMessage());
        }
    }

    private JButton crearBotonSeleccion(String texto, Runnable accion, Container grupo) {
        JButton boton = new JButton(texto);
        boton.setPreferredSize(new Dimension(160, 40));
        boton.setBackground(Color.LIGHT_GRAY);
        boton.addActionListener(e -> {
            resetearGrupoBotones(grupo);
            boton.setBackground(new Color(100, 149, 237));
            accion.run();
        });
        grupo.add(boton);
        return boton;
    }

    private void resetearGrupoBotones(Container contenedor) {
        for (Component c : contenedor.getComponents()) {
            if (c instanceof JButton) {
                c.setBackground(Color.LIGHT_GRAY);
            }
        }
    }

    private JLabel labelConCentrado(String texto) {
        JLabel lbl = new JLabel(texto);
        lbl.setAlignmentX(Component.CENTER_ALIGNMENT);
        return lbl;
    }

    private Component campoConCentrado(JComponent campo) {
        campo.setMaximumSize(new Dimension(250, 30));
        campo.setAlignmentX(Component.CENTER_ALIGNMENT);
        return campo;
    }

    private void limpiarFormulario() {
        txtNombre.setText("");
        servicioSeleccionado = null;
        metodoSeleccionado = null;
        horarioSeleccionado = null;
        lblMensaje.setText("");
        resetearGrupoBotones(btnInterior.getParent());
        resetearGrupoBotones(btnTaller.getParent());
        resetearGrupoBotones(btnH1.getParent());

        cmbDia.setSelectedIndex(0);
        cmbMes.setSelectedIndex(0);
        cmbAño.setSelectedIndex(0); // cambio aquí
    }
}

