
document.body.addEventListener('htmx:afterOnLoad', function(event) {

// Start Register Mono code block
const formMono = document.getElementById('monoForm');
if (formMono) {
    const profeRegisterUrl = document.getElementById('form-container').getAttribute('data-register-url');

    formMono.addEventListener('submit', async function(event) {
        event.preventDefault();  
        console.log("Form submitted");

        const monoData = new FormData(formMono);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        try {
            const response = await fetch(profeRegisterUrl, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: monoData,
            });

            const dataMono = await response.json();
            console.log("Response data:", dataMono);

            if (dataMono.status === 'success') {
                Swal.fire({
                    title: '¡Éxito!',
                    text: dataMono.message,
                    icon: 'success',
                    confirmButtonText: 'OK',
                });

                formMono.reset();
            } else {
                Swal.fire({
                    title: 'Error!',
                    text: dataMono.message || 'Hubo un problema. Por favor, intente nuevamente.',
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
    console.log('Form with ID "monoForm" not found!');
}

//   End Register Monos block
    });