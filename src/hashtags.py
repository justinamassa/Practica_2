def obtener_hashtags(posts):
    """Extrae todos los hashtags de los posts y cuenta su frecuencia."""
    conteo = {}
    for post in posts:
        palabras = post.split()
        for palabra in palabras:
            if palabra.startswith('#'):
                hashtag = palabra.lower()
                if hashtag in conteo:
                    conteo[hashtag] += 1
                else:
                    conteo[hashtag] = 1
    return conteo


def hashtags_trending(conteo):
    """Devuelve los hashtags que aparecen más de una vez, ordenados por frecuencia."""
    trending = {h: c for h, c in conteo.items() if c > 1}
    return dict(sorted(trending.items(), key=lambda item: item[1], reverse=True))
