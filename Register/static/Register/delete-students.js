document.body.addEventListener('htmx:afterOnLoad', function(event) {
// Start delete student block
const deleteEstuForm = document.getElementById("deleteEstuForm");
console.log(deleteEstuForm);
if (deleteEstuForm) {
    console.log('Form found');
    deleteEstuForm.addEventListener("submit", async function(event) {
        event.preventDefault();
        console.log('Button clicked');

        const deleteEstuUrl = deleteEstuForm.getAttribute("data-register-url");
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const deleteEstuData = new FormData(deleteEstuForm);

        try {
            const response = await fetch(deleteEstuUrl, {
                method: 'POST',
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: deleteEstuData,
            });

            const dataEstuDelete = await response.json();
            console.log("Response data:", dataEstuDelete);

            if (dataEstuDelete.status === 'success') {
                Swal.fire({
                    title: '¡Éxito!',
                    text: dataEstuDelete.message,
                    icon: 'success',
                    confirmButtonText: 'OK',
                }).then(() => {
                    // To do: move the attribute to the partial correspondant html
                    const addEstuUrl = document.querySelector('.title').getAttribute('data-addEstu-url');
                    console.log(addEstuUrl)
                    if (addEstuUrl) {
                        htmx.ajax('GET', addEstuUrl, { target: '#content' });
                    } else {
                        console.error("addEstuUrl not found on the body element.");
                    }
                });
            } else {
                Swal.fire({
                    title: 'Error!',
                    text: dataEstuDelete.message || 'Hubo un problema. Por favor, intente nuevamente.',
                    icon: 'error',
                    confirmButtonText: 'OK',
                });
            }
        } catch (error) {
            console.log("Fetch error:", error);
            Swal.fire({
                title: 'Error!',
                text: 'Error de red. Por favor, intente nuevamente.',
                icon: 'error',
                confirmButtonText: 'OK',
            });
        }
    });
} else {
    console.log('Form with ID "deleteEstuForm" not found!');
}
// End delete Student block
    });