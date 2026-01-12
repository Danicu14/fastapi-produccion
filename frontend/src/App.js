
import React, { useEffect, useState } from "react";

function App() {
  const [tareas, setTareas] = useState([]);
  const [titulo, setTitulo] = useState("");
  const [descripcion, setDescripcion] = useState("");
  const [mensaje, setMensaje] = useState("");

  // Obtener tareas
  const cargarTareas = () => {
    fetch("/api/tareas")
      .then((res) => res.json())
      .then(setTareas);
  };

  useEffect(() => {
    cargarTareas();
  }, []);

  // Agregar tarea
  const agregarTarea = (e) => {
    e.preventDefault();
    if (!titulo.trim()) return setMensaje("El título es obligatorio");
    fetch("/api/tareas", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id: 0, titulo, descripcion, completada: false }),
    })
      .then((res) => res.json())
      .then((data) => {
        setTitulo("");
        setDescripcion("");
        setMensaje("Tarea agregada");
        cargarTareas();
      });
  };

  // Eliminar tarea
  const eliminarTarea = (id) => {
    fetch(`/api/tareas/${id}`, { method: "DELETE" })
      .then((res) => res.json())
      .then(() => {
        setMensaje("Tarea eliminada");
        cargarTareas();
      });
  };

  // Marcar como completada
  const completarTarea = (id) => {
    fetch(`/api/tareas/${id}/completar`, { method: "PUT" })
      .then((res) => res.json())
      .then(() => {
        setMensaje("Tarea completada");
        cargarTareas();
      });
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 30, fontFamily: "Arial" }}>
      <h1 style={{ textAlign: "center" }}>Gestor de Tareas</h1>
      <form onSubmit={agregarTarea} style={{ marginBottom: 30, background: "#f7f7f7", padding: 20, borderRadius: 8 }}>
        <h2>Nueva tarea</h2>
        <input
          type="text"
          placeholder="Título"
          value={titulo}
          onChange={(e) => setTitulo(e.target.value)}
          style={{ width: "100%", padding: 8, marginBottom: 10 }}
        />
        <textarea
          placeholder="Descripción"
          value={descripcion}
          onChange={(e) => setDescripcion(e.target.value)}
          style={{ width: "100%", padding: 8, marginBottom: 10 }}
        />
        <button type="submit" style={{ padding: "8px 16px", background: "#1976d2", color: "#fff", border: "none", borderRadius: 4 }}>
          Agregar
        </button>
      </form>
      <h2>Lista de tareas</h2>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {tareas.length === 0 && <li>No hay tareas</li>}
        {tareas.map((tarea) => (
          <li key={tarea.id} style={{ background: "#e3e3e3", marginBottom: 10, padding: 15, borderRadius: 6, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <div>
              <strong style={{ textDecoration: tarea.completada ? "line-through" : "none" }}>{tarea.titulo}</strong>
              <p style={{ margin: "5px 0", color: "#555" }}>{tarea.descripcion}</p>
              {tarea.completada && <span style={{ color: "green", fontWeight: "bold" }}>Completada</span>}
            </div>
            <div>
              {!tarea.completada && (
                <button onClick={() => completarTarea(tarea.id)} style={{ marginRight: 10, background: "#43a047", color: "#fff", border: "none", borderRadius: 4, padding: "6px 12px" }}>
                  Completar
                </button>
              )}
              <button onClick={() => eliminarTarea(tarea.id)} style={{ background: "#d32f2f", color: "#fff", border: "none", borderRadius: 4, padding: "6px 12px" }}>
                Eliminar
              </button>
            </div>
          </li>
        ))}
      </ul>
      {mensaje && <p style={{ color: "#1976d2", fontWeight: "bold" }}>{mensaje}</p>}
    </div>
  );
}

export default App;
