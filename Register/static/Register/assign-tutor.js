document.body.addEventListener('htmx:afterOnLoad', function(event) {
// Start Asignar Tutor code block
const profesorIdField = document.getElementById("profesorIdField");
const tutorDropdown = document.getElementById("tutorDropdown");
const assignTutorButton = document.getElementById("assignTutorButton");

let addTutorUrl = "";

document.querySelectorAll(".assign-tutor-btn").forEach(button => {
button.addEventListener("click", () => {
    profesorIdField.value = button.closest("tr").querySelector("td:first-child").textContent;
    addTutorUrl = button.getAttribute("data-add-tutor-url");

});
});

assignTutorButton.addEventListener("click", async () => {
const profesorId = profesorIdField.value;
const monoId = tutorDropdown.value;
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

if (!monografiaId) {
    Swal.fire("Error", "Debe seleccionar una monografía.", "error");
    return;
}

try {
    const response = await fetch(addTutorUrl, {
    method: "POST",
    headers: {
        "X-CSRFToken": csrfToken,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ profesor_id: profesorId, monografia_id: monoId })
    });

    const data = await response.json();

    if (data.success) {
    Swal.fire("¡Éxito!", "Monografía asignada exitosamente", "success");
    $('#tutorModal').modal('hide');
    } else {
    Swal.fire("Error", data.error || "Hubo un problema. Por favor, intente nuevamente.", "error");
    }
} catch (error) {
    Swal.fire("Error", "Error de red. Por favor, intente nuevamente.", "error");
}
});
// End Asignar Tutor block
                });