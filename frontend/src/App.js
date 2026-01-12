import React, { useEffect, useState } from "react";

function App() {
  const [bicicletas, setBicicletas] = useState([]);
  const [reserva, setReserva] = useState("");
  const [mensaje, setMensaje] = useState("");

  useEffect(() => {
    fetch("/api/bicicletas")
      .then((res) => res.json())
      .then(setBicicletas);
  }, [mensaje]);

  const reservar = (id) => {
    fetch(`/api/reservar/${id}`, { method: "POST" })
      .then((res) => res.json())
      .then((data) => {
        setMensaje(data.mensaje);
        setReserva(id);
      });
  };

  return (
    <div style={{ maxWidth: 500, margin: "auto", padding: 20 }}>
      <h1>Reserva de Bicicletas</h1>
      <ul>
        {bicicletas.map((bici) => (
          <li key={bici.id}>
            {bici.nombre} - {bici.disponible ? "Disponible" : "Reservada"}
            {bici.disponible && (
              <button style={{ marginLeft: 10 }} onClick={() => reservar(bici.id)}>
                Reservar
              </button>
            )}
          </li>
        ))}
      </ul>
      {mensaje && <p>{mensaje}</p>}
    </div>
  );
}

export default App;
