document.body.addEventListener('htmx:afterOnLoad', function(event) {
//Start asignar Jurado code block
const juradoIdField = document.getElementById("juradoIdField");
const monografiaDropdown = document.getElementById("monografiaDropdown");
const assignJuradoButton = document.getElementById("assignJuradoButton");

let addJuradoUrl = "";

document.querySelectorAll(".assign-jurado-btn").forEach(button => {
button.addEventListener("click", () => {
    juradoIdField.value = button.closest("tr").querySelector("td:first-child").textContent;
    addJuradoUrl = button.getAttribute("data-add-jurado-url");
    
});
});

assignJuradoButton.addEventListener("click", async () => {
console.log('clicked'); 
const juradoId = juradoIdField.value;
const monografiaId = monografiaDropdown.value;
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

if (!juradoId || !monografiaId) {
    Swal.fire("Error", "Debe seleccionar un jurado y una monografía.", "error");
    return;
}

try {
    const response = await fetch(addJuradoUrl, {
    method: "POST",
    headers: {
        "X-CSRFToken": csrfToken,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ jurado_id: juradoId, monografia_id: monografiaId })
    });

    const data = await response.json();
    if (data.success) {
    Swal.fire("¡Éxito!", "Jurado asignado exitosamente", "success");
    $('#exampleModal').modal('hide');
    } else {
    Swal.fire("Error", data.error || "Hubo un problema. Por favor, intente nuevamente.", "error");
    }
} catch (error) {
    Swal.fire("Error", "Error de red. Por favor, intente nuevamente.", "error");
}
});

// End asignar jurado block
            });