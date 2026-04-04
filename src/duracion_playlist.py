def convertir_a_segundos(duracion):
    """Convierte una duración en formato m:ss a segundos."""
    partes = duracion.split(':')
    minutos = int(partes[0])
    segundos = int(partes[1])
    return minutos * 60 + segundos


def calcular_duracion_total(playlist):
    """Devuelve la duración total de la playlist en formato Xm Ys."""
    total_segundos = 0
    for cancion in playlist:
        total_segundos += convertir_a_segundos(cancion['duration'])
    minutos = total_segundos // 60
    segundos = total_segundos % 60
    return f"{minutos}m {segundos}s"


def cancion_mas_larga(playlist):
    """Devuelve la canción con mayor duración."""
    return max(playlist, key=lambda c: convertir_a_segundos(c['duration']))


def cancion_mas_corta(playlist):
    """Devuelve la canción con menor duración."""
    return min(playlist, key=lambda c: convertir_a_segundos(c['duration']))
