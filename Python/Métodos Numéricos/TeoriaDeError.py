import teoriaError.exponencial as exp
import teoriaError.sin as sin
import teoriaError.cos as cos
import teoriaError.jacobi as jacobi
import teoriaError.gaussSeidel as gauss

while (True):
    print("Teoría de Erorr")
    print("-" * 40)
    print("Eliga una Opción")
    print(" 1: Euler")
    print(" 2: Sin")
    print(" 3: Cos")
    print(" 4: Jacobi")
    print(" 5: Gauss Seidel")
    print("-1: Salir")
    opcion=int(input("Eliga una opción: "))
    
    if opcion==-1:
        print("Saliendo...")
        break
    elif opcion ==1:
        exp.exponencial()
        continue
    elif opcion==2:
        sin.sin()
        continue
    elif opcion==3:
        cos.cos()
        continue
    elif opcion==4:
        jacobi.jacobi()
        continue
    elif opcion==5:
        gauss.gaussSeidel()
        continue