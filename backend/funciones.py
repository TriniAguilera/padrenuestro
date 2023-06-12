import os

def procesar_archivo(archivo):
    lista_elementos = [["", "", "", "", "", "", "", "", "", "", ""]]
    nombre_archivo = archivo + ".txt"
    ruta = os.path.join("mapas", nombre_archivo)
    with open(ruta, "rt", encoding='utf-8') as a:
        filas_archivo = a.readlines()
    for fila in filas_archivo:
        linea = fila.strip()
        fila_buena = list(linea)
        fila_completa = [""]
        for elemento in fila_buena:
            fila_completa.append(elemento)
        fila_completa.append("")
        lista_elementos.append(fila_completa)
    lista_elementos.append(["", "", "", "", "", "", "", "", "", "", ""])
    return lista_elementos

def calcular_posicion_futura(letra_elemento, direccion, f, c):
    fila = f
    columna = c
    if letra_elemento == "L":
        if direccion == "R": ### derecha
            columna += 1
        elif direccion == "L": ### izquierda
            columna -= 1
        elif direccion == "U": ### arriba
            fila -= 1
        elif direccion == "D": ### abajo
            fila += 1
        if fila > 14:
            fila = 14
        elif fila < 1:
            fila = 1
        if columna > 9:
            columna = 9
        elif columna < 1:
            columna = 1
    elif letra_elemento == "H":
        if direccion == 1: ### derecha
            columna += 1
        elif direccion == -1: ### izquierda
            columna -= 1
        if columna > 9:
            columna = 9
        elif columna < 1:
            columna = 1
    elif letra_elemento == "V":
        if direccion == 1: ### arriba
            fila -= 1
        elif direccion == -1:
            fila += 1
        if fila > 14:
            fila = 14
        elif fila < 1:
            fila = 1
    elif letra_elemento == "R":
        if direccion == "R": ### derecha
            columna += 1
        elif direccion == "L": ### izquierda
            columna -= 1
        elif direccion == "U": ### arriba
            fila -= 1
        elif direccion == "D": ### abajo
            fila += 1
        if fila > 14:
            fila = 14
        elif fila < 1:
            fila = 1
        if columna > 9:
            columna = 9
        elif columna < 1:
            columna = 1
    return fila, columna