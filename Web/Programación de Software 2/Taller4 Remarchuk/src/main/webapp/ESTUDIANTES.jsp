<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registro de Estudiantes | La Universidad del Pueblo</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body class="formulario">
        <%@ include file="html/header.html" %>

        <h1>Registro de Estudiantes</h1>
        <p>Bienvenido al sistema de registro de estudiantes. Por favor, complete el formulario para inscribirse en los cursos técnicos disponibles.</p>
        <a class="button-link" href="PROFESORES.jsp">Soy profesor</a>

        <section>
            <div class="form-content">
                <form action="procesar_estudiante.jsp">
                    <label>Nombre Completo:</label>
                    <input type="text" name="nombre" required>

                    <label>Cédula:</label>
                    <input type="text" name="cedula" required>

                    <label>Año lectivo:</label>
                    <input type="text" name="anio" required>

                    <label>Centro Regional:</label>
                    <select name="centro_regional">
                        <option value="Panamá">Panamá</option>
                        <option value="Coclé">Coclé</option>
                        <option value="Colón">Colón</option>
                        <option value="Veraguas">Veraguas</option>
                        <option value="Los Santos">Los Santos</option>
                        <option value="Bocas del Toro">Bocas del Toro</option>
                        <option value="Chiriquí">Chiriquí</option>
                    </select>

                    <label>Cursos de interés:</label>
                    <div style="text-align: left; max-width: 300px; margin: 0 auto; margin-bottom: 20px;">
                        <input type="checkbox" name="cursos" value="Soldadura"> Soldadura<br>
                        <input type="checkbox" name="cursos" value="Electrónica"> Electrónica<br>
                        <input type="checkbox" name="cursos" value="Cocina"> Cocina<br>
                        <input type="checkbox" name="cursos" value="Programación"> Programación<br>
                        <input type="checkbox" name="cursos" value="Robótica"> Robótica<br>
                        <input type="checkbox" name="cursos" value="Ciberseguridad"> Ciberseguridad<br>
                        <input type="checkbox" name="cursos" value="Diseño Web"> Diseño Web<br>
                        <input type="checkbox" name="cursos" value="Bases de Datos"> Bases de Datos<br>
                    </div><br>

                    <label>Índice Académico: <output name="valIndice" for="indice">1.5</output></label>
                    <input type="range" name="indice" min="0" max="3" step="0.01" value="1.5" 
                        oninput="valIndice.value=parseFloat(this.value).toFixed(2)" style="width: 100%;">
                    <br><br>

                    <input type="submit" value="Registrar Estudiante">
                </form>
            </div>
        </section>
        
        <%@ include file="html/footer.html" %>
    </body>
</html>