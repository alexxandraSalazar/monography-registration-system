document.body.addEventListener('htmx:afterOnLoad', function(event) {
// Start assign students code block
const assignButtons = document.querySelectorAll(".btn-success");
const studentIdField = document.getElementById("studentId");
const dropdown = document.getElementById("dropdown");
const assignButton = document.getElementById("assignButton");
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const addEstuUrl = document.getElementById('deleteEstuForm').getAttribute('add-estu-url');

assignButtons.forEach(button => {
button.addEventListener("click", function () {
const studentId = this.closest("tr").querySelector("td:first-child").textContent;
studentIdField.value = studentId;
});
});

assignButton.addEventListener("click", async function () {
const studentId = studentIdField.value;
const monoId = dropdown.value;

if (!monografiaId) {
    Swal.fire("Error", "Debe seleccionar una monografía.", "error");
    return;
}

try {
const response = await fetch(addEstuUrl, {
    method: "POST",
    headers: {
    "X-CSRFToken": csrfToken,
    "Content-Type": "application/json"
    },
    body: JSON.stringify({ student_id: studentId, mono_id: monoId })
});

const data = await response.json();

if (data.success) {
    Swal.fire({
    title: '¡Éxito!',
    text: 'Monografía asignada exitosamente',
    icon: 'success',
    confirmButtonText: 'OK'
    });

    $('#exampleModal').modal('hide');
} else {
    Swal.fire({
    title: 'Error',
    text: data.error || 'Hubo un problema. Por favor, intente nuevamente.',
    icon: 'error',
    confirmButtonText: 'OK'
    });
}
} catch (error) {
Swal.fire({
    title: 'Error',
    text: 'Error de red. Por favor, intente nuevamente.',
    icon: 'error',
    confirmButtonText: 'OK'
    });
}
});
// End assign students block
                    });