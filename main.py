
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

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str
    completada: bool = False

tareas = []
contador_id = 1

@app.get("/api/tareas")
def listar_tareas():
    return tareas

@app.post("/api/tareas")
def agregar_tarea(tarea: Tarea):
    global contador_id
    tarea.id = contador_id
    contador_id += 1
    tareas.append(tarea)
    return tarea

@app.delete("/api/tareas/{id}")
def eliminar_tarea(id: int):
    for tarea in tareas:
        if tarea.id == id:
            tareas.remove(tarea)
            return {"mensaje": "Tarea eliminada"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.put("/api/tareas/{id}/completar")
def completar_tarea(id: int):
    for tarea in tareas:
        if tarea.id == id:
            tarea.completada = True
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
