# fastapi-produccion

Instrucciones rápidas para ejecutar la API localmente (Windows PowerShell):

1. Activar el virtualenv:

```powershell
.\venv\Scripts\Activate.ps1
```

2. Ejecutar la aplicación (con reload opcional):

```powershell
# con reload (ver cambios automáticamente)
python -m uvicorn main:app --reload

# sin reload
python -m uvicorn main:app
```

Alternativa: usar los scripts proporcionados desde la raíz del proyecto:

```powershell
# PowerShell
.\start.ps1 -Reload

# CMD
start.bat reload
```

Nota: Evita tener una copia de `main.py` dentro de `venv/`.
