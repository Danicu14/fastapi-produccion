param([switch]$Reload)
$python = Join-Path $PSScriptRoot 'venv\Scripts\python.exe'
if ($Reload) {
    & $python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
} else {
    & $python -m uvicorn main:app --host 127.0.0.1 --port 8000
}
