# Métodos Numéricos 🧮

Aplicación de consola sobre teoría de error, aproximaciones de funciones y resolución iterativa de sistemas de ecuaciones. Procede de la carpeta `METNUM` de TrabajosEnClase.

| Archivo | Contenido |
| --- | --- |
| [TeoriaDeError.py](TeoriaDeError.py) | Menú que conecta los cinco ejercicios. |
| [exponencial.py](teoriaError/exponencial.py) | Aproximación de `e^x` mediante Taylor y cálculo de error relativo. |
| [sin.py](teoriaError/sin.py) | Serie de Taylor del seno; entrada en radianes. |
| [cos.py](teoriaError/cos.py) | Serie de Taylor del coseno; entrada en radianes. |
| [jacobi.py](teoriaError/jacobi.py) | Método de Jacobi con truncamiento y control de tolerancia. |
| [gaussSeidel.py](teoriaError/gaussSeidel.py) | Gauss-Seidel con valores actualizados durante cada iteración. |

## Ejecución

Desde esta carpeta:

```powershell
python -m pip install numpy
python TeoriaDeError.py
```

El menú ofrece exponencial, seno, coseno, Jacobi y Gauss-Seidel; `-1` termina la ejecución. En los métodos iterativos se introducen la matriz, el vector independiente, la tolerancia porcentual, el máximo de iteraciones y los decimales de truncamiento.

## Particularidades del código

En `exponencial.py` se solicita una cantidad de iteraciones, pero el ciclo actual evalúa siempre seis aproximaciones (`n = 0` a `5`). Los sistemas lineales requieren coeficientes diagonales distintos de cero; la convergencia depende de la matriz ingresada y de los parámetros elegidos.

[← Volver al portafolio](../../readme.md)
