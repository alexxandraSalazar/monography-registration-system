
document.body.addEventListener('htmx:afterOnLoad', function(event) {
// Start Register profesors code block
const formProfe = document.getElementById('profeForm');
if (formProfe) {
    const profeRegisterUrl = document.getElementById('form-container').getAttribute('data-register-url');

    formProfe.addEventListener('submit', async function(event) {
        event.preventDefault();  
        console.log("Form submitted");

        const profeData = new FormData(formProfe);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        try {
            const response = await fetch(profeRegisterUrl, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: profeData,
            });

            const dataProfe = await response.json();
            console.log("Response data:", dataProfe);

            if (dataProfe.status === 'success') {
                Swal.fire({
                    title: '¡Éxito!',
                    text: dataProfe.message,
                    icon: 'success',
                    confirmButtonText: 'OK',
                });

                formProfe.reset();
            } else {
                Swal.fire({
                    title: 'Error!',
                    text: dataProfe.message || 'Hubo un problema. Por favor, intente nuevamente.',
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
    console.log('Form with ID "profeForm" not found!');
}

// End Register profesors block
    });