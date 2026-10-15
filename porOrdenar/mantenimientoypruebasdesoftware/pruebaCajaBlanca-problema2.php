if ($rolSesion === null) {
    // No hay sesion -> lo mandamos al login
    header('Location: ' . APP_URL . 'login.php');
    exit;
}

// Si la pagina definio una lista de roles permitidos, validamos
if (isset($rolesPermitidos) && is_array($rolesPermitidos)) {
    if (!in_array($rolSesion, $rolesPermitidos, true)) {
        $_SESSION['mensajeError'] = 'No tienes permiso para acceder a esa seccion.';
        // El rol "comandas" no tiene acceso a orders.php; si lo mandamos ahi
        // se genera un bucle de redireccion infinito. Va a su propia pantalla.
        $destino = ($rolSesion === 'comandas') ? 'pages/comandas.php' : 'pages/orders.php';
        header('Location: ' . APP_URL . $destino);
        exit;
    }
}
