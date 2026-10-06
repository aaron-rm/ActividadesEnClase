import math

def taylor_exp(x, n):
    suma = 0
    for k in range(n + 1):
        termino = (x ** k) / math.factorial(k)
        suma += termino
    return suma

def exponencial():
    x = int(input("Punto a evaluar: x="))
    n = int(input("Cantidad de iteraciones: n="))
    for n in range(6):
        aprox = taylor_exp(x, n)
        real = math.exp(x)
        error_abs = abs(real - aprox)
        error_rel = error_abs / abs(real)

        print(f"n={n}")
        print(f"Aproximación = {aprox:.10f}")
        print(f"Valor real   = {real:.10f}")
        print(f"Error rel    = {error_rel:.10f}")
        print("-" * 40)
    pass

