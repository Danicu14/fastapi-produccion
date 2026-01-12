@echo off
setlocal enabledelayedexpansion
set PYTHON=%~dp0venv\Scripts\python.exe
if "%1"=="reload" (
  "%PYTHON%" -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
) else (
  "%PYTHON%" -m uvicorn main:app --host 127.0.0.1 --port 8000
)
