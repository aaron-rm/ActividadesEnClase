# SE DESARROLLAN TODAS LAS RUTINAS AGRUPADAS EN 4 GRUPOS
# 1- 3 REGISTROS, 2- 2 REGISTROS 3- CONSTANTE O ETIQUETA 4- 1 REGISTRO

import re
from Objetivo2 import DIRECTORIO, etiquetas # importar etiquetas del objetivo 2

RUTA_DEPURADA = DIRECTORIO / 'p41.asm'
RUTA_FINAL = DIRECTORIO / 'CODE.ROM'

new_archivo = open(RUTA_FINAL, "w")                 # crear un archivo vacio
print("\nArchivo creado")

def add(linea): # Para instrucciones que tienen RD RF1 RF2 (ADD,MUL,SUB,DIV,AND,REM,OR,XOR)
   numeros = re.findall(r'\d+', linea)
   numeros_enteros = [int(num) for num in numeros]
   hexadecimal = hex(subr%16)[2:]+''.join(hex(num)[2:] for num in numeros_enteros)

   hexadecimal = hexadecimal.upper()
   print("Hexadecimal: " + hexadecimal)
   new_archivo.write(hexadecimal+'\n')      # escribe w en el archivo con '\n'
   

def shr(linea): # Para Instrucciones que tienen RD RF1 xx y xx RF1 RF2 (SHR,RR,SHL,RL y SLT,SGT,EQ,NEQ)
   numeros = re.findall(r'\d+', linea)
   numeros_enteros = [int(num) for num in numeros]
   hexadecimal = hex(subr%16)[2:]
   if subr%16 > 5 and subr%16 < 9: 
      hexadecimal += hex(subr>15)[2:]+''.join(hex(num)[2:] for num in numeros_enteros)+' '
   else:
      hexadecimal = hexadecimal+''.join(hex(num)[2:] for num in numeros_enteros)+"0 "

   hexadecimal = hexadecimal.upper()
   print("Hexadecimal: " + hexadecimal)
   new_archivo.write(hexadecimal+'\n')

def li(linea): # Para instrucciones que tienen inmediato o constantes y Etiquetas (LI,LUI y JMP,BRA)
   numeros = re.findall(r'\d+', linea)
   numeros_enteros = [int(num) for num in numeros]
   hexadecimal = hex(subr)[2:]
   if subr > 11:
      etiqueta = pos[1]
      for etiq, valor in etiquetas:
         if etiq == etiqueta:
            hexadecimal += hex(valor)[2:].zfill(3)+' '
            break
   else:
      hexadecimal += hex(numeros_enteros[0])[2:]+pos[2]+pos[3]+' '

   hexadecimal = hexadecimal.upper()
   print("Hexadecimal: " + hexadecimal)
   new_archivo.write(hexadecimal+'\n')

def jr(linea): # Para instrucciones JR,SPC y BBR,CLS,RST
   numeros = re.findall(r'\d+', linea)
   numeros_enteros = [int(num) for num in numeros]
   hexadecimal = hex(subr%16)[2:]
   if subr == 29:
      hexadecimal = "e100 "
   if subr%16 == 14 :
      hexadecimal += hex(3 if subr>15 else 0)[2:]+hex(numeros_enteros[0])[2:]+"0 "
   elif subr%16 == 15:
      hexadecimal += "100 "

   hexadecimal = hexadecimal.upper()
   print("Hexadecimal: " + hexadecimal)
   new_archivo.write(hexadecimal+'\n')

nemonicos = [  "ADD","SUB","AND","OR","SR","SL","SLT","EQ","SB", "LB","LI","LUI","JMP","BRA","JR","SPC",
               "MUL","DIV","REM","XOR","RR","RL","SGT","NEQ","MOV","SWP",'','','',     "RST","BBR","CLS"]
subrutinas = [ add,  add,   add,  add,  shr, shr, shr,  shr,  shr,  shr, li, li,   li,   li,   jr,  jr,
               add,  add,  add,  add,   shr, shr, shr,  shr,  shr,  shr,  0,  0,    0,   jr,   jr,  jr]

# agregar lineas para crear nuevo archivo

with open(RUTA_DEPURADA) as archivo:
   new_archivo.write("v2.0 raw\n")      # escribir w en el archivo con '\n'
   for linea in archivo:                  # se hace un ciclo recorriendo el arreglo : linea = lineas[0], linea = lineas[1] ....
      print("\nLinea original: " + linea.strip())     #  imprimir la linea original sin espacios al inicio y al final
      pos = linea.split()               # se hace una lista a partir de la cadena ADD  R2  R3  R10 : LISTA =[ADD R2 R3 R10]
      nemonico = pos[0]                # palabra = al nemonico (ADD)
      OK = 0
      for subr in range(32):         # recorrido de los 32 nemonicos
         if nemonico == nemonicos[subr]: # pregunta si palabra es igual algun nemonico de la lista llamada nemonicos
            subrutinas[subr](linea) # si es igual va a la subrutina pertinente
            OK=1
            break
         
      if OK == 0:
         print("No se ha encontrado este nemonico -->",linea.strip())

   print("\nArchivo final creado")
   new_archivo.close()
