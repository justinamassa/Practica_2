def filtrar_spoilers(texto, palabras_spoiler):
    """Reemplaza las palabras spoiler en el texto por asteriscos."""
    resultado = texto 
    for palabra in palabras_spoiler: 
        asteriscos = '*' * len(palabra)
        resultado = resultado.replace(palabra, asteriscos)
        resultado = resultado.replace(palabra.lower(), asteriscos)
        resultado = resultado.replace(palabra.upper(), asteriscos)
        resultado = resultado.replace(palabra.capitalize(), asteriscos)
    return resultado

