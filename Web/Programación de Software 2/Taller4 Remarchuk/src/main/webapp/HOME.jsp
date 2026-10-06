<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>La Universidad del Pueblo | Inicio</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <body>
        <%@ include file="html/header.html" %>

        <div class="main-container">
            <nav class="menu-nav">
                <h3>Menú de Navegación</h3>
                <ul>
                    <li><a href="HOME.jsp">Inicio</a></li>
                    <li><a href="ESTUDIANTES.jsp">Registro Estudiantes</a></li>
                    <li><a href="PROFESORES.jsp">Registro Profesores</a></li>
                    <li><a href="CALENDARIO.jsp">Calendario</a></li>
                    <li><a href="SOPORTE.jsp">Soporte</a></li>
                </ul>
            </nav>

            <section class="home-content">
                <h1>Bienvenido a la Universidad del Pueblo</h1>

                <div class="botones-nav">
				    <a href="PROFESORES.jsp">
				        <img src="img/profesores.png" alt="Profesores" width="200">
				        <p>Registro de Profesores</p>
				    </a>
				    <a href="CALENDARIO.jsp">
				        <img src="img/calendario.png" alt="Calendario" width="200">
				        <p>Calendario</p>
				    </a>
				    <a href="ESTUDIANTES.jsp">
				        <img src="img/estudiantes.png" alt="Estudiantes" width="200">
				        <p>Registro de Estudiantes</p>
				    </a>
				</div>

                <div class="noticias">
                    <h1>Últimas Noticias Universitarias</h1>
                    
                    <div class="noticia-item">
                        <h2 class="noticia-titulo">La UTP firma convenio con el IJA</h2>
                        <p class="noticia-desc">La Universidad Tecnológica de Panamá (UTP) formalizó un Convenio Marco de Cooperación con el Instituto 
                        Justo Arosemena (IJA), buscando impulsar actividades académicas, investigativas y facilitar la inserción de los estudiantes del 
                        instituto en las carreras tecnológicas de la universidad.</p>
                        <a href="https://utp.ac.pa/la-utp-firma-convenio-con-el-ija" class="noticia-link" target="_blank">Más información</a>
                    </div>

                    <div class="noticia-item">
                        <h2 class="noticia-titulo">¿Sabías qué es el Sistema Penal Acusatorio?</h2>
                        <p class="noticia-desc">Un artículo informativo publicado en la plataforma UPInforma, donde se explica de manera didáctica el funcionamiento, 
                        fundamentos y la importancia del Sistema Penal Acusatorio dentro del marco jurídico panameño.</p>
                        <a href="https://upinforma.com/nuevo/info.php?cat=noticias&s=" class="noticia-link" target="_blank">Más información</a>                    
                    </div>

                    <div class="noticia-item">
                        <h2 class="noticia-titulo">USMA y FECAP firman convenio de cooperación</h2>
                        <p class="noticia-desc">La Universidad Católica Santa María La Antigua (USMA) y la Federación de Educación Católica (FECAP) establecieron una 
                        alianza estratégica para colaborar en proyectos académicos, de investigación y capacitación profesional, fortaleciendo el intercambio entre ambas 
                        instituciones.</p>
                        <a href="https://usma.ac.pa/2022/08/31/usma-y-fecap-firman-convenio-de-cooperacion/" class="noticia-link" target="_blank">Más información</a>
                    </div>
                </div>
            </section>
        </div>

        <%@ include file="html/footer.html" %>
    </body>
</html>