import time, tracemalloc, threading
import tkinter as tk
from tkinter import ttk, messagebox

try:
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except Exception:
    PLOTLY_AVAILABLE = False

#Datos para ejemplo: ISBN, Título, Autor, Año, breve descripcion
LIBROS_DB = [
    {"isbn": "9780553381689", "titulo": "A Game of Thrones", "autor": "George R.R. Martin", "ano": 1996,
     "descripcion": "En Poniente, las familias nobles luchan por el control del Trono de Hierro mientras se avecina un invierno implacable."},
    {"isbn": "9780553108033", "titulo": "A Clash of Kings", "autor": "George R.R. Martin", "ano": 1998,
     "descripcion": "Múltiples reyes reclaman el trono, mientras la guerra fractura el reino y los peligros en el Norte se intensifican."},
    {"isbn": "9780553573427", "titulo": "A Storm of Swords", "autor": "George R.R. Martin", "ano": 2000,
     "descripcion": "Traiciones, batallas y alianzas inesperadas marcan la brutal lucha por el poder en los Siete Reinos."},
    {"isbn": "9780553801476", "titulo": "A Feast for Crows", "autor": "George R.R. Martin", "ano": 2005,
     "descripcion": "El reparto del poder tras la guerra revela nuevas intrigas, conspiraciones y luchas por el control político."},
    {"isbn": "9780553801506", "titulo": "A Dance with Dragons", "autor": "George R.R. Martin", "ano": 2011,
     "descripcion": "Jon Snow, Daenerys y Tyrion enfrentan decisiones clave en medio de guerras, dragones y amenazas antiguas."},
    {"isbn": "9780743273565", "titulo": "The Da Vinci Code", "autor": "Dan Brown", "ano": 2003,
     "descripcion": "Robert Langdon investiga un asesinato en el Louvre y descubre una conspiración milenaria ligada a la Iglesia."},
    {"isbn": "9780307474278", "titulo": "Angels & Demons", "autor": "Dan Brown", "ano": 2000,
     "descripcion": "Una sociedad secreta planea destruir el Vaticano mientras Langdon descifra símbolos antiguos para detenerla."},
    {"isbn": "9780385504201", "titulo": "The Lost Symbol", "autor": "Dan Brown", "ano": 2009,
     "descripcion": "Langdon sigue pistas masónicas en Washington D.C. para descubrir un antiguo secreto oculto en la capital."},
    {"isbn": "9780385537131", "titulo": "Inferno", "autor": "Dan Brown", "ano": 2013,
     "descripcion": "Una amenaza biológica inspirada en Dante pone en riesgo a la humanidad, y Langdon debe descifrar códigos para detenerla."},
    {"isbn": "9780385514231", "titulo": "Origin", "autor": "Dan Brown", "ano": 2017,
     "descripcion": "Un futurista revela una teoría sobre el origen y el destino de la humanidad, desafiando la fe y la ciencia."},
    {"isbn": "9780451524935", "titulo": "1984", "autor": "George Orwell", "ano": 1949,
     "descripcion": "Un futuro totalitario donde el Gran Hermano controla cada aspecto de la vida y manipula la verdad."},
    {"isbn": "9780451526342", "titulo": "Animal Farm", "autor": "George Orwell", "ano": 1945,
     "descripcion": "Una granja gobernada por animales se convierte en una sátira del autoritarismo y la corrupción del poder."},
    {"isbn": "9780156027328", "titulo": "Brave New World", "autor": "Aldous Huxley", "ano": 1932,
     "descripcion": "Una sociedad futurista donde la tecnología controla la felicidad, la genética y el comportamiento humano."},
    {"isbn": "9780060850524", "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ano": 1953,
     "descripcion": "Un bombero encargado de quemar libros comienza a cuestionar su papel en una sociedad sin pensamiento crítico."},
    {"isbn": "9780743273565", "titulo": "The Great Gatsby", "autor": "F. Scott Fitzgerald", "ano": 1925,
     "descripcion": "Jay Gatsby persigue el sueño americano en una historia de riqueza, amor y tragedia en los años 20."},
    {"isbn": "9780141439600", "titulo": "Wuthering Heights", "autor": "Emily Brontë", "ano": 1847,
     "descripcion": "Una historia pasional y oscura que explora amor, venganza y tormento entre Heathcliff y Catherine."},
    {"isbn": "9780142437209", "titulo": "Moby Dick", "autor": "Herman Melville", "ano": 1851,
     "descripcion": "El capitán Ahab obsesionado persigue a la ballena blanca en una travesía llena de simbolismo y tragedia."},
    {"isbn": "9780140449266", "titulo": "The Odyssey", "autor": "Homero", "ano": -800,
     "descripcion": "Odiseo enfrenta monstruos, dioses y desafíos épicos en su regreso a Ítaca."},
    {"isbn": "9780486264721", "titulo": "The Iliad", "autor": "Homero", "ano": -750,
     "descripcion": "La guerra de Troya narrada con héroes, dioses y conflictos entre gloria, honor y destino."},
    {"isbn": "9780141442464", "titulo": "Jane Eyre", "autor": "Charlotte Brontë", "ano": 1847,
     "descripcion": "Una joven enfrenta adversidades sociales y emocionales mientras busca amor e independencia."},
    {"isbn": "9780679783268", "titulo": "Crime and Punishment", "autor": "Fyodor Dostoevsky", "ano": 1866,
     "descripcion": "Un estudiante comete un crimen y enfrenta un conflicto psicológico entre culpa, moral y redención."},
    {"isbn": "9780140449136", "titulo": "The Brothers Karamazov", "autor": "Fyodor Dostoevsky", "ano": 1880,
     "descripcion": "Una compleja historia sobre fe, moral, crimen y filosofía en una familia rusa conflictiva."},
    {"isbn": "9780553803709", "titulo": "Foundation", "autor": "Isaac Asimov", "ano": 1951,
     "descripcion": "Hari Seldon predice la caída del Imperio Galáctico y crea una Fundación para preservar el conocimiento."},
    {"isbn": "9780553293357", "titulo": "Foundation and Empire", "autor": "Isaac Asimov", "ano": 1952,
     "descripcion": "La Fundación enfrenta amenazas internas y externas que ponen a prueba su estabilidad."},
    {"isbn": "9780553293364", "titulo": "Second Foundation", "autor": "Isaac Asimov", "ano": 1953,
     "descripcion": "La misteriosa Segunda Fundación trabaja desde las sombras para preservar el futuro de la humanidad."},
    {"isbn": "9780345339683", "titulo": "The Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937,
     "descripcion": "Bilbo Bolsón es arrastrado a una aventura con enanos, dragones y tesoros legendarios."},
    {"isbn": "9780618640157", "titulo": "The Fellowship of the Ring", "autor": "J.R.R. Tolkien", "ano": 1954,
     "descripcion": "Un grupo diverso se une para destruir un anillo que podría esclavizar a la Tierra Media."},
    {"isbn": "9780618640188", "titulo": "The Two Towers", "autor": "J.R.R. Tolkien", "ano": 1954,
     "descripcion": "La Comunidad se divide mientras la guerra contra Sauron y Saruman amenaza toda la Tierra Media."},
    {"isbn": "9780618640195", "titulo": "The Return of the King", "autor": "J.R.R. Tolkien", "ano": 1955,
     "descripcion": "Aragorn reclama su destino mientras el Anillo Único se enfrenta a su destrucción final."},
    {"isbn": "9780547928227", "titulo": "The Silmarillion", "autor": "J.R.R. Tolkien", "ano": 1977,
     "descripcion": "El origen de la Tierra Media, los elfos, los anillos de poder y la historia de Morgoth y Sauron."},
    {"isbn": "9780141439846", "titulo": "Frankenstein", "autor": "Mary Shelley", "ano": 1818,
     "descripcion": "Victor Frankenstein crea una criatura consciente que lo confronta con las consecuencias de su ambición."},
    {"isbn": "9780679723165", "titulo": "Lolita", "autor": "Vladimir Nabokov", "ano": 1955,
     "descripcion": "El profesor Humbert Humbert relata su obsesión amorosa y perturbadora con una niña llamada Lolita."},
    {"isbn": "9780747532743", "titulo": "Harry Potter and the Philosopher's Stone", "autor": "J.K. Rowling", "ano": 1997,
     "descripcion": "Un niño descubre que es mago y entra a un mundo de magia, amistad y peligros oscuros."},
    {"isbn": "9780439064873", "titulo": "Harry Potter and the Chamber of Secrets", "autor": "J.K. Rowling", "ano": 1998,
     "descripcion": "Una misteriosa cámara es abierta y criaturas peligrosas acechan a los estudiantes de Hogwarts."},
    {"isbn": "9780439136365", "titulo": "Harry Potter and the Prisoner of Azkaban", "autor": "J.K. Rowling", "ano": 1999,
     "descripcion": "Un peligroso prisionero escapa de Azkaban y parece estar tras Harry."},
    {"isbn": "9780439139601", "titulo": "Harry Potter and the Goblet of Fire", "autor": "J.K. Rowling", "ano": 2000,
     "descripcion": "Un torneo mágico pone a prueba habilidades, valentía y revela el regreso de un poder oscuro."},
    {"isbn": "9780439358071", "titulo": "Harry Potter and the Order of the Phoenix", "autor": "J.K. Rowling", "ano": 2003,
     "descripcion": "Harry enfrenta la incredulidad del Ministerio mientras se prepara para enfrentar a Voldemort."},
    {"isbn": "9780439785969", "titulo": "Harry Potter and the Half-Blood Prince", "autor": "J.K. Rowling", "ano": 2005,
     "descripcion": "Las reliquias del pasado revelan secretos sobre Voldemort y cómo vencerlo."},
    {"isbn": "9780545010221", "titulo": "Harry Potter and the Deathly Hallows", "autor": "J.K. Rowling", "ano": 2007,
     "descripcion": "Harry enfrenta su destino final mientras la guerra mágica llega a su clímax."},
    {"isbn": "9780441172719", "titulo": "Dune", "autor": "Frank Herbert", "ano": 1965,
     "descripcion": "En Arrakis, Paul Atreides descubre su destino en medio de profecías, poder y supervivencia."},
    {"isbn": "9780441013593", "titulo": "Dune Messiah", "autor": "Frank Herbert", "ano": 1969,
     "descripcion": "Paul, ahora emperador, enfrenta las consecuencias de su ascenso y las profecías que lo persiguen."},
    {"isbn": "9780441104024", "titulo": "Children of Dune", "autor": "Frank Herbert", "ano": 1976,
     "descripcion": "La familia Atreides lucha por el control de Arrakis mientras el destino de la humanidad pende de un hilo."},
    {"isbn": "9780061122415", "titulo": "To Kill a Mockingbird", "autor": "Harper Lee", "ano": 1960,
     "descripcion": "Una niña presencia las injusticias raciales en el sur de Estados Unidos a través del juicio de un hombre inocente."},
    {"isbn": "9781501128035", "titulo": "It", "autor": "Stephen King", "ano": 1986,
     "descripcion": "Un grupo de amigos enfrenta a una entidad maléfica que se alimenta del miedo en un pueblo de Maine."},
    {"isbn": "9780307743657", "titulo": "The Shining", "autor": "Stephen King", "ano": 1977,
     "descripcion": "Una familia pasa el invierno en un hotel aislado, donde fuerzas sobrenaturales toman el control."},
    {"isbn": "9781476787817", "titulo": "Pet Sematary", "autor": "Stephen King", "ano": 1983,
     "descripcion": "Un cementerio antiguo tiene el poder de traer a los muertos, pero con consecuencias horribles."},
    {"isbn": "9780140283334", "titulo": "Lord of the Flies", "autor": "William Golding", "ano": 1954,
     "descripcion": "Un grupo de niños varados en una isla se organiza, pero pronto cae en el caos y la barbarie."},
    {"isbn": "9780743482837", "titulo": "Hamlet", "autor": "William Shakespeare", "ano": 1603,
     "descripcion": "El príncipe Hamlet busca vengar la muerte de su padre, enfrentando dilemas morales y políticos."},
    {"isbn": "9780060850524", "titulo": "The Alchemist", "autor": "Paulo Coelho", "ano": 1988,
     "descripcion": "Un pastor andaluz sigue su Leyenda Personal en una travesía espiritual hacia Egipto."},
    {"isbn": "9780307588371", "titulo": "The Girl with the Dragon Tattoo", "autor": "Stieg Larsson", "ano": 2005,
     "descripcion": "Un periodista y una hacker investigan un misterio familiar oculto desde hace décadas."},
    {"isbn": "9780062316110", "titulo": "The Fault in Our Stars", "autor": "John Green", "ano": 2012,
     "descripcion": "Dos jóvenes con cáncer se enamoran mientras enfrentan su propia mortalidad con humor y dolor."},
    {"isbn": "9780439354447", "titulo": "Eragon", "autor": "Christopher Paolini", "ano": 2002,
     "descripcion": "Un joven granjero encuentra un huevo de dragón que lo lleva a convertirse en Jinete de Dragón."},
    {"isbn": "9780439554892", "titulo": "The Hunger Games", "autor": "Suzanne Collins", "ano": 2008,
     "descripcion": "En un futuro distópico, jóvenes luchan a muerte en un espectáculo televisado."},
    {"isbn": "9780439023518", "titulo": "Catching Fire", "autor": "Suzanne Collins", "ano": 2009,
     "descripcion": "Katniss se convierte en símbolo de rebelión mientras enfrenta un nuevo torneo mortal."},
    {"isbn": "9780545310582", "titulo": "Mockingjay", "autor": "Suzanne Collins", "ano": 2010,
     "descripcion": "La rebelión contra el Capitolio llega a su punto más peligroso y decisivo."},
    {"isbn": "9780060935467", "titulo": "The Kite Runner", "autor": "Khaled Hosseini", "ano": 2003,
     "descripcion": "Una historia de amistad, traición y redención ambientada en Afganistán."},
    {"isbn": "9781439107959", "titulo": "The Book Thief", "autor": "Markus Zusak", "ano": 2005,
     "descripcion": "Narrada por la Muerte, sigue la historia de una niña que roba libros durante la Segunda Guerra Mundial."},
    {"isbn": "9780307269997", "titulo": "The Help", "autor": "Kathryn Stockett", "ano": 2009,
     "descripcion": "Criadas afroamericanas cuentan sus historias de discriminación en los años 60."},
    {"isbn": "9780141036136", "titulo": "The Road", "autor": "Cormac McCarthy", "ano": 2006,
     "descripcion": "Un padre y su hijo luchan por sobrevivir en un mundo postapocalíptico devastado."},
    {"isbn": "9780140280197", "titulo": "A Thousand Splendid Suns", "autor": "Khaled Hosseini", "ano": 2007,
     "descripcion": "Dos mujeres afganas unen fuerzas para sobrevivir a la opresión y la guerra."},
    {"isbn": "9780307346605", "titulo": "Gone Girl", "autor": "Gillian Flynn", "ano": 2012,
     "descripcion": "Una esposa desaparece misteriosamente, y su esposo se convierte en sospechoso principal."},
    {"isbn": "9780553386790", "titulo": "The Martian", "autor": "Andy Weir", "ano": 2011,
     "descripcion": "Un astronauta queda atrapado en Marte y usa su ingenio para sobrevivir solo."}
]

# LOGICA
class Logica:
    def __init__(self):
        # Datos internos para la App
        self.libros = list(LIBROS_DB)
        # Copia ordenada para la búsqueda binaria interna de la App
        self.libros_ordenados_isbn = self.ordenar_por_atributo(self.libros, 'isbn')

    # Algoritmos
    @staticmethod
    def algoritmo_busqueda_binaria(lista_ordenada, isbn_buscado):
        bajo, alto = 0, len(lista_ordenada) - 1
        while bajo <= alto:
            medio = (bajo + alto) // 2
            isbn_medio = lista_ordenada[medio]['isbn']
            if isbn_medio == isbn_buscado:
                return lista_ordenada[medio]
            elif isbn_medio < isbn_buscado:
                bajo = medio + 1
            else:
                alto = medio - 1
        return None

    @staticmethod
    def algoritmo_busqueda_lineal(lista, termino_busqueda):
        termino = termino_busqueda.lower()
        # List comprehension es la forma pythonica de búsqueda lineal
        return [libro for libro in lista if termino in libro["titulo"].lower()]

    @staticmethod
    def ordenar_por_atributo(lista, atributo, reverso=False):
        return sorted(lista, key=lambda x: x[atributo], reverse=reverso)

    @staticmethod
    def intercambio_directo(lista):
        arr = lista.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j]["titulo"] > arr[j+1]["titulo"]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def seleccion_directa(lista):
        arr = lista.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j]["titulo"] < arr[min_idx]["titulo"]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    @staticmethod
    def insercion_directa(lista):
        arr = lista.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j]["titulo"] > key["titulo"]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    # Lógica de negocio
    def obtener_libros_filtrados(self, termino, criterio, autor_filtro, orden):
        termino = termino.strip().lower()
        autor_filtro = autor_filtro.strip().lower()
        resultados = []

        # 1. BÚSQUEDA
        if termino:
            if criterio == "ISBN":
                libro_encontrado = self.algoritmo_busqueda_binaria(self.libros_ordenados_isbn, termino)
                resultados = [libro_encontrado] if libro_encontrado else []
            else:
                resultados = self.algoritmo_busqueda_lineal(self.libros, termino)
        else:
            resultados = list(self.libros)

        # 2. FILTRO AUTOR (Lineal simple)
        if autor_filtro:
            resultados = [l for l in resultados if autor_filtro in l["autor"].lower()]

        # 3. ORDENAMIENTO
        if orden == "Título (A-Z)":
            resultados = self.ordenar_por_atributo(resultados, 'titulo')
        elif orden == "Título (Z-A)":
            resultados = self.ordenar_por_atributo(resultados, 'titulo', reverso=True)
        elif orden == "Año (Más reciente primero)":
            resultados = self.ordenar_por_atributo(resultados, 'ano', reverso=True)
        elif orden == "Año (Más antiguo primero)":
            resultados = self.ordenar_por_atributo(resultados, 'ano')

        return resultados

# APP
class BibliotecaGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- CONTROLADOR Y LÓGICA ---
        self.Logica = Logica()
        self.analizador = AnalizadorEmpirico(self.Logica)

        # --- CONFIGURACIÓN DE LA VENTANA ---
        self.title("Biblioteca Virtual")
        self.geometry("1000x650")
        self.configure(bg="#f0f2f5")

        # --- ESTILOS ---
        s = ttk.Style()
        s.configure('White.TFrame', background='white')

        # --- VARIABLES DE LA UI ---
        self.criterio_busqueda = tk.StringVar(value="Título")
        self.termino_busqueda = tk.StringVar()
        self.autor_filtro = tk.StringVar()
        self.criterio_orden = tk.StringVar(value="Título (A-Z)")

        self.mapa_datos = {}

        # Crear widgets
        self.crear_widgets()

        # Llenar tabla al iniciar
        self.actualizar_tabla()

    # ------------------------------------------------------------
    #                       UI
    # ------------------------------------------------------------
    def crear_widgets(self):
        lbl_titulo = ttk.Label(self, text="Biblioteca Virtual", font=("Arial", 24, "bold"), background="#f0f2f5")
        lbl_titulo.pack(pady=(10, 20))

        panel = ttk.Frame(self, padding="15", style="White.TFrame")
        panel.pack(fill="x", padx=30, pady=10)

        # Criterio
        cb_criterio = ttk.Combobox(panel, textvariable=self.criterio_busqueda,
                                   values=["Título", "ISBN"], state="readonly", width=10)
        cb_criterio.grid(row=0, column=0, padx=5, pady=10)

        # Entrada búsqueda
        entry_search = ttk.Entry(panel, textvariable=self.termino_busqueda, width=50)
        entry_search.grid(row=0, column=1, padx=5, pady=10)
        entry_search.bind("<Return>", lambda event: self.actualizar_tabla())

        # Botón buscar
        ttk.Button(panel, text="🔍 Buscar", command=self.actualizar_tabla)\
            .grid(row=0, column=2, padx=5, pady=10)

        # Botón análisis
        ttk.Button(panel, text="📊 Ejecutar Análisis Empírico",
                   command=self.solicitar_ejecucion_analisis)\
            .grid(row=0, column=3, padx=5, pady=10)

        # Ordenar
        ttk.Label(panel, text="Ordenar por:", background="white")\
            .grid(row=1, column=0, padx=5, pady=10, sticky="w")

        cb_orden = ttk.Combobox(panel, textvariable=self.criterio_orden,
                                values=["Título (A-Z)", "Título (Z-A)",
                                        "Año (Más reciente primero)", "Año (Más antiguo primero)"],
                                state="readonly")
        cb_orden.grid(row=1, column=1, padx=5, pady=10)
        cb_orden.bind("<<ComboboxSelected>>", lambda event: self.actualizar_tabla())

        # Autor
        ttk.Label(panel, text="Filtrar autor:", background="white")\
            .grid(row=1, column=2, padx=5, pady=10)

        entry_autor = ttk.Entry(panel, textvariable=self.autor_filtro, width=30)
        entry_autor.grid(row=1, column=3, padx=5, pady=10)
        entry_autor.bind("<Return>", lambda event: self.actualizar_tabla())

        # TABLA
        tabla_frame = ttk.Frame(self, padding="15", style="White.TFrame")
        tabla_frame.pack(fill="both", expand=True, padx=30, pady=10)

        columns = ("ISBN", "Título", "Autor", "Año")
        self.tree = ttk.Treeview(tabla_frame, columns=columns, show="headings")
        self.tree.pack(side="left", fill="both", expand=True)

        for col in columns:
            self.tree.heading(col, text=col.upper())

        self.tree.column("ISBN", width=150, anchor="center")
        self.tree.column("Título", width=300, anchor="w")
        self.tree.column("Autor", width=200, anchor="w")
        self.tree.column("Año", width=80, anchor="center")

        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_fila)

    # ------------------------------------------------------------
    #         MÉTODOS DEL CONTROLADOR (ANTES EN BibliotecaApp)
    # ------------------------------------------------------------
    def actualizar_tabla(self):
        termino = self.termino_busqueda.get()
        criterio = self.criterio_busqueda.get()
        autor = self.autor_filtro.get()
        orden = self.criterio_orden.get()

        resultados = self.Logica.obtener_libros_filtrados(termino, criterio, autor, orden)
        self.mostrar_resultados(resultados)

    def mostrar_resultados(self, lista):
        self.tree.delete(*self.tree.get_children())
        self.mapa_datos = {}

        for libro in lista:
            item_id = self.tree.insert("", "end",
                                       values=(libro["isbn"], libro["titulo"], libro["autor"], libro["ano"]))
            self.mapa_datos[item_id] = libro

    def seleccionar_fila(self, event):
        item_id = self.tree.focus()
        if not item_id:
            return
        libro = self.mapa_datos[item_id]
        self.abrir_modal_detalle(libro)

    def abrir_modal_detalle(self, libro):
        modal = tk.Toplevel(self)
        modal.title(libro["titulo"])
        modal.geometry("500x350")
        modal.transient(self)
        modal.grab_set()

        frame = ttk.Frame(modal, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text=libro["titulo"], font=("Arial", 16, "bold")).pack()
        ttk.Label(frame, text=f"Autor: {libro['autor']}").pack(anchor="w")
        ttk.Label(frame, text=f"Año: {libro['ano']}").pack(anchor="w")
        ttk.Label(frame, text=f"ISBN: {libro['isbn']}").pack(anchor="w")

        ttk.Separator(frame).pack(fill="x", pady=10)

        ttk.Label(frame, text=libro["descripcion"], wraplength=460, justify="left").pack(anchor="w")

        ttk.Button(frame, text="Cerrar", command=modal.destroy)\
            .pack(pady=10)

    # ------------------ ANÁLISIS EMPÍRICO ------------------------
    def solicitar_ejecucion_analisis(self):
        if not PLOTLY_AVAILABLE:
            messagebox.showerror("Error", "Plotly no está instalado.")
            return

        if not messagebox.askyesno("Confirmar", "¿Deseas ejecutar el análisis empírico?"):
            return

        threading.Thread(target=self._ejecutar_analisis, daemon=True).start()

    def _ejecutar_analisis(self):
        try:
            self.after(0, lambda: messagebox.showinfo("Análisis", "El análisis ha iniciado."))

            self.analizador.analisis_empirico()

            self.after(0, lambda: messagebox.showinfo("Análisis", "Análisis finalizado."))
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Error", str(e)))

# ANALISIS EMPIRICO
class AnalizadorEmpirico:
    def __init__(self, logica):
        self.log = logica

    @staticmethod
    def generar_libros(n):
        # Genera libros mínimos con campo 'titulo' para los algoritmos de ordenamiento
        return [{"titulo": f"Libro_{i}"} for i in range(n)]

    @staticmethod
    def medir_tiempo_memoria(func, datos):
        inicio = time.perf_counter()
        tracemalloc.start()
        func(datos)
        memoria = tracemalloc.get_traced_memory()[1] / 1024  # KB
        tracemalloc.stop()
        fin = time.perf_counter()
        tiempo_ms = (fin - inicio) * 1000
        tiempo_s = fin - inicio
        return round(tiempo_ms, 4), round(tiempo_s, 6), round(memoria, 4)

    def analisis_empirico(self, tamanios=None):
        if not PLOTLY_AVAILABLE:
            raise RuntimeError("plotly no está disponible en este entorno. Instala plotly para generar gráficas.")

        if tamanios is None:
            tamanios = [100, 500, 1000, 2000, 5000, 7000, 10000, 15000]

        tabla_inter = []
        tabla_selec = []
        tabla_insert = []

        for n in tamanios:
            print(f"\n>>> Analizando con n = {n} ...")
            libros = self.generar_libros(n)

            t1, s1, m1 = self.medir_tiempo_memoria(self.log.intercambio_directo, libros)
            t2, s2, m2 = self.medir_tiempo_memoria(self.log.seleccion_directa, libros)
            t3, s3, m3 = self.medir_tiempo_memoria(self.log.insercion_directa,  libros)

            tabla_inter.append([n, t1, s1, m1])
            tabla_selec.append([n, t2, s2, m2])
            tabla_insert.append([n, t3, s3, m3])

        self.imprimir_tabla("INTERCAMBIO DIRECTO", tabla_inter)
        self.imprimir_tabla("SELECCIÓN DIRECTA", tabla_selec)
        self.imprimir_tabla("INSERCIÓN DIRECTA", tabla_insert)
        self.graficas_estilo_profesor(tabla_inter, tabla_selec, tabla_insert)

    @staticmethod
    def imprimir_tabla(nombre, datos):
        print(f"\n=== {nombre} ===\n")
        print("{:<8} {:<15} {:<15} {:<15}".format("n", "Tiempo (ms)", "Tiempo (s)", "Memoria (KB)"))
        print("-"*58)
        for fila in datos:
            print("{:<8} {:<15} {:<15} {:<15}".format(*fila))
        print()

    @staticmethod
    def graficas_estilo_profesor(inter, selec, inser):
        def crear_fig(datos, titulo):
            n = [x[0] for x in datos]
            tiempo = [x[1] for x in datos]
            memoria = [x[3] for x in datos]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=n, y=tiempo, mode="lines+markers", name="Tiempo (ms)"))
            fig.add_trace(go.Scatter(x=n, y=memoria, mode="lines+markers", name="Memoria (KB)"))

            fig.update_layout(
                title={"text": titulo, "x":0.5, "y":0.92},
                xaxis_title="Tamaño n",
                yaxis_title="Valor",
                template="simple_white",
                width=900,
                height=450
            )
            fig.show()

        crear_fig(inter, "Intercambio Directo — Tiempo y Memoria")
        crear_fig(selec, "Selección Directa — Tiempo y Memoria")
        crear_fig(inser, "Inserción Directa — Tiempo y Memoria")

if __name__ == "__main__":
    app = BibliotecaGUI()
    app.mainloop()