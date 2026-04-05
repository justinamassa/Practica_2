def calcular_puntaje_ronda(scores):
    """Calcula el puntaje total  de cada participante en una ronda."""
    return {participante: sum(jueces.values())
            for participante, jueces in scores.items()}

def obtener_ganador_ronda(puntajes_ronda):
    """Devuelve el ganador de la ronda y su puntaje."""
    ganador = max(puntajes_ronda, key=lambda p: puntajes_ronda[p])
    return ganador, puntajes_ronda[ganador]

def actualizar_totales(totales, puntajes_ronda, ganador):
    """Actualiza los totales acumulados de cada participante."""
    for participante, puntaje in puntajes_ronda.items():
        totales[participante]['total'] += puntaje
        totales[participante]['rondas_ganadas'] += (1 if participante == ganador else 0)
        if puntaje > totales[participante]['mejor_ronda']:
            totales[participante]['mejor_ronda'] = puntaje
    return totales

def mostrar_tabla(totales, num_rondas):
    """Muestra la tabla de posiciones ordenada por puntaje total."""
    print(f"{'Cocinero':<12} {'Puntaje':>8} {'Rondas ganadas':>15} {'Mejor ronda':>12} {'Promedio':>10}")
    print("-" * 60)
    ranking = sorted(totales.items(), key=lambda x: x[1]['total'], reverse=True)
    for participante, datos in ranking:
        promedio = datos['total'] / num_rondas
        print(f"{participante:<12} {datos['total']:>8} {datos['rondas_ganadas']:>15} {datos['mejor_ronda']:>12} {promedio:>10.1f}")
    print("-" * 60)

def inicializar_totales(participantes):
    """Inicializa el diccionario de totales para cada participante."""
    return {participante: {'total': 0, 'rondas_ganadas': 0, 'mejor_ronda': 0}
            for participante in participantes}
