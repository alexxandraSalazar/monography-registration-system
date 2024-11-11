document.body.addEventListener('htmx:afterOnLoad', function(event) {
// Start delete Profesor block
const deleteProfForm = document.getElementById("deleteProfForm");
console.log(deleteProfForm);
if (deleteProfForm) {
    console.log('Form found');
    deleteProfForm.addEventListener("submit", async function(event) {
        event.preventDefault();
        console.log('Button clicked');

        const deleteProfUrl = deleteProfForm.getAttribute("data-register-url");
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const deleteProfData = new FormData(deleteProfForm);

        try {
            const response = await fetch(deleteProfUrl, {
                method: 'POST',
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: deleteProfData,
            });

            const dataProfDelete = await response.json();
            console.log("Response data:", dataProfDelete);

            if (dataProfDelete.status === 'success') {
                Swal.fire({
                    title: '¡Éxito!',
                    text: dataProfDelete.message,
                    icon: 'success',
                    confirmButtonText: 'OK',
                }).then(() => {
                    // to do: same as above
                    const addProfUrl = document.querySelector('.title').getAttribute('data-addProf-url');
                    console.log(addProfUrl)
                    if (addProfUrl) {
                        htmx.ajax('GET', addProfUrl, { target: '#content' });
                    } else {
                        console.error("addProfUrl not found on the body element.");
                    }
                });
            } else {
                Swal.fire({
                    title: 'Error!',
                    text: dataProfDelete.message || 'Hubo un problema. Por favor, intente nuevamente.',
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
    console.log('Form with ID "deleteProfForm" not found!');
}
// End delete profesor block
        });