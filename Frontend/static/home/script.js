
button_data = document.getElementById("button_data");

id_personas = 0;

function button_send_data() {
    data_catch = document.getElementById("form_data").value;

    console.log("boton apretadiño");
    id_personas += 1;

    fetch("http://localhost:8000", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: id_personas, nombre: data_catch })
    })
    .then(res => res.json())
    .then(data => console.log("Respuesta del servidor:", data))
}

