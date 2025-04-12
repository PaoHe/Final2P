from fastapi import FastAPI, HTTPException, Depends, Header
from models import Pelicula, PeliculaUpdate
import database
import auth

app = FastAPI()

#Crear peli
@app.post("/peliculas")
def crear_pelicula(pelicula: Pelicula):
    id = database.agregar_pelicula(pelicula.dict())
    return {"id": id, "mensaje": "Pelicula guardada correctamente"}

#Editar peli
@app.put("/peliculas/{id}")
def editar(id: int, datos: PeliculaUpdate):
    if database.editar_pelicula(id, datos.dict(exclude_unset=True)):
        return {"mensaje": "Película actualizada"}
    raise HTTPException(status_code=404, detail="Película no encontrada")

#Eliminar peli
@app.delete("/peliculas/{id}")
def eliminar(id: int, token: str = Header(...)):
    if not auth.verificar_token(token):
        raise HTTPException(status_code=401, detail="Token inválido")
    if database.eliminar_pelicula(id):
        return {"mensaje": "Película eliminada"}
    raise HTTPException(status_code=404, detail="Película no encontrada")

#Obtener peli
@app.get("/peliculas")
def obtener_todas():
    return database.obtener_todas()

#Obtener peli por id
@app.get("/peliculas/{id}")
def obtener_una(id: int):
    pelicula = database.obtener_pelicula(id)
    if pelicula:
        return pelicula
    raise HTTPException(status_code=404, detail="Película no encontrada")

#Obtener token peli
@app.get("/token")
def obtener_token():
    return {"token": auth.crear_token({"usuario": "admin"})}
