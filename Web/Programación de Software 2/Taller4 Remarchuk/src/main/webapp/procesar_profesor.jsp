<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registro de Profesor Completado</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <%@ include file="html/header.html" %>
        
        <%
            // Conexión a la base de datos
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/taller4", "root", "");
            Statement dbstatement = conexion.createStatement();

            // Recolección de datos del formulario
            String nombre = request.getParameter("nombre").toUpperCase(); // Convertir a mayúsculas
            String cedula = request.getParameter("cedula").toUpperCase(); // Convertir a mayúsculas
            String materia = request.getParameter("materia").toUpperCase(); // Convertir a mayúsculas
            String centro = request.getParameter("centro_regional").toUpperCase(); // Convertir a mayúsculas
            String exp = request.getParameter("experiencia"); // Será "SI", "NO" o null
            
            // Si el checkbox/radio no se seleccionó, asignar un valor por defecto
            if(exp == null) exp = "NO";

            // Inserción en la base de datos
            String insertQuery = "INSERT INTO profesor (nombre, cedula, materia, centroEDU, expVIR) VALUES ('" 
                                + nombre + "', '" 
                                + cedula + "', '" 
                                + materia + "', '" 
                                + centro + "', '" 
                                + exp + "')";
                                
            dbstatement.executeUpdate(insertQuery);
            dbstatement.close();
            conexion.close();
        %>
        <section class="registro-exitoso">
            <h1>Registro Exitoso</h1>
            
            <main class="registro-info">
                <div class="info">
                    <h2>Datos del Profesor:</h2>
                    <p><strong>Nombre:</strong> <%= nombre %></p>
                    <p><strong>Cédula:</strong> <%= cedula %></p>
                    <p><strong>Materia:</strong> <%= materia %></p>
                    <p><strong>Centro Regional:</strong> <%= centro %></p>
                    <p><strong>Experiencia en clases virtuales:</strong> <%= exp %></p>
                </div>
            </main>

            <div class="registro-volver">
                <a href="HOME.jsp">Volver al inicio</a>
            </div>
        </section>

        <%@ include file="html/footer.html" %>
    </body>
</html>