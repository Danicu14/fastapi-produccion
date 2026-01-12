from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Bicicleta(BaseModel):
    id: int
    nombre: str
    disponible: bool

bicicletas = [
    Bicicleta(id=1, nombre="Bicicleta Urbana", disponible=True),
    Bicicleta(id=2, nombre="Bicicleta Montaña", disponible=True),
    Bicicleta(id=3, nombre="Bicicleta Eléctrica", disponible=True),
]

@app.get("/api/bicicletas")
def listar_bicicletas():
    return bicicletas

@app.post("/api/reservar/{id}")
def reservar_bicicleta(id: int):
    for bici in bicicletas:
        if bici.id == id:
            if not bici.disponible:
                raise HTTPException(status_code=400, detail="La bicicleta ya está reservada.")
            bici.disponible = False
            return {"mensaje": f"Has reservado la {bici.nombre}"}
    raise HTTPException(status_code=404, detail="Bicicleta no encontrada.")
