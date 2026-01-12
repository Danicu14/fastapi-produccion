import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Servir archivos estáticos del build de React
frontend_build_path = os.path.join(os.path.dirname(__file__), "frontend", "build")
if os.path.exists(frontend_build_path):
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.mount("/static", StaticFiles(directory=os.path.join(frontend_build_path, "static")), name="static")

    @app.get("/", include_in_schema=False)
    def serve_react_root():
        index_file = os.path.join(frontend_build_path, "index.html")
        return FileResponse(index_file)

    @app.get("/{full_path:path}", include_in_schema=False)
    def serve_react_app(full_path: str):
        index_file = os.path.join(frontend_build_path, "index.html")
        return FileResponse(index_file)
else:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    @app.get("/")
    def root():
        return {"mensaje": "El frontend no está compilado. Ejecuta 'npm run build' en la carpeta frontend."}

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
