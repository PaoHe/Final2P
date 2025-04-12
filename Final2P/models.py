from pydantic import BaseModel, Field
from typing import Optional

class Pelicula(BaseModel):
    titulo: str = Field(..., min_length=2)
    genero: str = Field(..., min_length=4)
    año: int = Field(..., ge=1000, le=9999)
    clasificacion: str = Field(..., min_length=1, max_length=1, pattern='^[ABC]$')

class PeliculaUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=2)
    genero: Optional[str] = Field(None, min_length=4)
    año: Optional[int] = Field(None, ge=1000, le=9999)
    clasificacion: Optional[str] = Field(None, min_length=1, max_length=1, pattern='^[ABC]$')
