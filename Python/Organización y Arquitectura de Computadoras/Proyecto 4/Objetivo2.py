# PARA DEPURAR UN ARCHIVO Y ELIMINAR ETIQUETAS

from pathlib import Path

DIRECTORIO = Path(__file__).resolve().parent

#ruta del archivo a depurar
RUTA = DIRECTORIO / 'P31.ASM'

RUTA_DEPURADA = DIRECTORIO / 'p41.asm'

etiquetas = []   # lista vacia de duplas [(etiqueta, adress) , (etiqueta, adress),....]
adress = 0       # direcion inicial de la primera instruccion de asembler

# abrir el archivo a depurar, recorrerlo linea por linea, eliminar etiquetas y escribir el resultado en un nuevo archivo
new_archivo = open(RUTA_DEPURADA, "w")                 # crear un archivo vacio
print("Archivo creado")
with open(RUTA) as archivo:                            #  abrir el archivo a depurar
    for linea in archivo:                              #  recorrer el archivo linea por linea
        lineaDepurada=''                               #  iniciar una cadena vacia  w=''
        
        # separa la cadena en una lista de elementos, usando el espacio como separador
        lista = linea.split()                          #  cada linea del archivo convertilo en lista
        print("Linea original: " + linea.strip())     #  imprimir la linea original sin espacios al inicio y al final
        for elemento in lista:                         #  recorrer la lista
            if len(lista)==0:                          # pregunta si lista esta vacia (no tiene elementos, linea vacia)
                print("Linea vacia")                       # si, imprimir "Linea vacia"
                break                                   # si, descatar esta lista
            elif elemento.startswith('/'):             # sino, pregunta si el primer caracter de la lista es == '/'
                print("Comentario encontrado")      # si, imprimir "Comentario encontrado"
                break                                # si, descartar la lista
            elif elemento.startswith(':'):             # sino, pregunta si el primer caracter es == ':'
                print("Etiqueta encontrada")         # si, imprimir "Etiqueta encontrada"
                etiquetas.append((elemento[1:].upper(),adress))      # ingresa datos a etiquetas [(lista,adress)]
            else:                                      # else 
                lineaDepurada += elemento.upper()+' '  # concatena en w el elemento en mayuscula
                print("Elemento procesado: " + lineaDepurada) 
        if len(lineaDepurada)>0:                       # w>0    
            adress += 1                                # incrementa el adress
            new_archivo.write(lineaDepurada+'\n')      # escribe w en el archivo con '\n'
            print("Linea depurada: " + lineaDepurada)
            print("\n")

new_archivo.close()
print("Archivo depurado")
print("Etiquetas encontradas:")
print(etiquetas)

# para el objetivo 3, devolver tupla de etiquetas [(etiqueta, adress), (etiqueta, adress),....]
# objetivo 3 abre el archivo generado en el objetivo 2
