def calcular_costo(peso, zona):
    """Calcula el costo de envio segun el peso y la zona."""

    zonas_validas = ['local', 'regional', 'nacional']
    if zona not in zonas_validas:
        return None
    precios = {
        'local': [500, 1000, 2000],
        'regional': [1000, 2500, 5000],
        'nacional': [2000, 4500, 8000],
    }
    if peso <= 1:
        indice = 0
    elif peso <= 5:
        indice = 1
    else:
        indice = 2

    return precios[zona][indice]

