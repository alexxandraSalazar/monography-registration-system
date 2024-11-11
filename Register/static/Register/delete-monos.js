document.body.addEventListener('htmx:afterOnLoad', function(event) {
// Start delete mono code block
const deleteMonoForm = document.getElementById("deleteMonoForm");
console.log(deleteMonoForm)
if (deleteMonoForm) {
console.log('here')
    deleteMonoForm.addEventListener("submit", async function(event) {
    console.log('no')
    event.preventDefault()
    console.log('btn clicked')
        const deleteMonoUrl = deleteMonoForm.getAttribute("data-register-url");
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const deleteMonoData = new FormData(deleteMonoForm);

        try {
            const response = await fetch(deleteMonoUrl, {
                method: 'POST',
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: deleteMonoData,
            });

            const dataMonoDelete = await response.json();
            console.log("Response data:", dataMonoDelete);

            if (dataMonoDelete.status === 'success') {
                Swal.fire({
                    title: '¡Éxito!',
                    text: dataMonoDelete.message,
                    icon: 'success',
                    confirmButtonText: 'OK',
                }).then(() => {
                    const indexUrl = document.body.getAttribute('data-index-url');
                    htmx.ajax('GET', indexUrl, { target: '#content' });
                });
            } else {
                Swal.fire({
                    title: 'Error!',
                    text: dataMonoDelete.message || 'Hubo un problema. Por favor, intente nuevamente.',
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
    console.log('Form with ID "deleteMonoForm" not found!');
}
//   End delete mono block
});