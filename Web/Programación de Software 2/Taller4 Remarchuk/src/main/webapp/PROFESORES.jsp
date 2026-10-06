<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registro de Profesores | La Universidad del Pueblo</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body class="formulario">
        <%@ include file="html/header.html" %>

            <h1>Registro de Personal Docente</h1>
            <p>Bienvenido al sistema de registro de profesores. Por favor, complete el formulario para aplicar a las vacantes de los próximos cursos técnicos.</p>

        <section>
            <div class="form-content">
                <form action="procesar_profesor.jsp">
                    <label>Nombre Completo:</label><br>
                    <input type="text" name="nombre" required><br><br>

                    <label>Cédula:</label><br>
                    <input type="text" name="cedula" required><br><br>

                    <label>Materia que dicta:</label><br>
                    <input type="text" name="materia" required><br><br>

                    <label>Centro Regional donde labora:</label><br>
                    <select name="centro_regional">
                        <option value="Panamá">Panamá</option>
                        <option value="Coclé">Coclé</option>
                        <option value="Colón">Colón</option>
                        <option value="Veraguas">Veraguas</option>
                        <option value="Los Santos">Los Santos</option>
                        <option value="Bocas del Toro">Bocas del Toro</option>
                        <option value="Chiriquí">Chiriquí</option>
                    </select><br><br>

                    <label>¿Tiene experiencia en clases virtuales?</label><br>
                    <input type="radio" name="experiencia" value="SI" required> SI
                    <input type="radio" name="experiencia" value="NO" required> NO<br><br>

                    <input type="submit" value="Registrar Profesor">
                </form>
            </div>
        </section>
        
        <%@ include file="html/footer.html" %>
    </body>
</html>