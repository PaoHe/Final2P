peliculas_db = {}
contador = 1

def agregar_pelicula(pelicula):
    global contador
    peliculas_db[contador] = pelicula
    contador += 1
    return contador - 1

def editar_pelicula(pelicula_id, datos):
    if pelicula_id in peliculas_db:
        peliculas_db[pelicula_id].update(datos)
        return True
    return False

def eliminar_pelicula(pelicula_id):
    return peliculas_db.pop(pelicula_id, None)

def obtener_pelicula(pelicula_id):
    return peliculas_db.get(pelicula_id)

def obtener_todas():
    return peliculas_db
