# Frontend para Reserva de Bicicletas

Este frontend React permite ver bicicletas disponibles y reservarlas, conectándose al backend FastAPI.

## Scripts
- `npm start`: Ejecuta la app en modo desarrollo.
- `npm run build`: Genera la versión de producción.

## Despliegue en Render
1. Instala dependencias: `npm install`
2. Configura el backend FastAPI para aceptar peticiones desde el frontend.
3. Despliega ambos servicios en Render.

## Estructura
- src/App.js: Componente principal
- src/index.js: Entrada de la app
- public/index.html: HTML base

## API
- GET `/api/bicicletas`: Lista de bicicletas
- POST `/api/reservar/{id}`: Reservar bicicleta

Asegúrate de que el backend esté corriendo y accesible desde el frontend.
