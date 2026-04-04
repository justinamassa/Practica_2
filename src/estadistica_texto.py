def obtener_lineas(texto): 
    """Devuelve una lista con todas las lineas del texto."""
    return texto.strip().split('\n')
def contar_palabras(lineas):
    """Devuelve el total de palabras en todas las lineas."""
    total = 0
    for linea in lineas: 
        total += len (linea.split())
    return total 
def calcular_promedio(total_palabras, total_lineas):
    """Devuelve el promedio de palabras por linea."""
    return total_palabras / total_lineas 
def lineas_sobre_promedio(lineas, promedio):
    """Devuelve las lineas que tienen mas palabras que el promedio."""
    resultado = []
    for linea in lineas:
        cantidad_palabras = len(linea.split())
        if cantidad_palabras > promedio: 
            resultado.append((linea, cantidad_palabras))
    return resultado
