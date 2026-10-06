# Proyecto 4: ensamblador educativo

Traducción de un programa con instrucciones de las máquinas educativas PC1 y PC2 a palabras hexadecimales. Los scripts Python conservan junto a ellos el programa fuente y los resultados de la entrega.

| Archivo | Función |
| --- | --- |
| [P31.ASM](P31.ASM) | Programa fuente con instrucciones, comentarios y etiquetas. |
| [Objetivo2.py](Objetivo2.py) | Elimina comentarios y etiquetas, normaliza instrucciones y registra direcciones. |
| [p41.asm](p41.asm) | Archivo intermedio de instrucciones depuradas. |
| [Objetivo3.py](Objetivo3.py) | Codifica instrucciones y resuelve referencias a etiquetas. |
| [CODE.ROM](CODE.ROM) | Salida hexadecimal con cabecera `v2.0 raw`. |

## Ejecución

Con Python 3, sin paquetes externos:

```powershell
python Objetivo3.py
```

`Objetivo3.py` importa `Objetivo2.py`, que ejecuta primero la depuración y construye la tabla de etiquetas. Por ello, una ejecución vuelve a generar **p41.asm y CODE.ROM**. También puedes ejecutar `Objetivo2.py` para realizar solo la primera etapa.

Las rutas se calculan a partir de la carpeta del script, por lo que ya no dependen de una ruta de OneDrive ni del directorio desde el que se invoque Python. Las instrucciones corresponden al formato educativo de esta entrega.

[← Volver al portafolio](../../../readme.md)
