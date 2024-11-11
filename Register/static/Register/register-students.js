
document.body.addEventListener('htmx:afterOnLoad', function(event) {
// Start register Student code block
const form = document.getElementById('estuForm');
if (form) {
    const registerUrl = document.getElementById('form-container').getAttribute('data-register-url');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();  
        console.log("Form submitted");

        const estuData = new FormData(form);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        try {
            const response = await fetch(registerUrl, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                },
                body: estuData,
            });

            const data = await response.json();
            console.log("Response data:", data);

            if (data.status === 'success') {
                Swal.fire({
                    title: '¡Éxito!',
                    text: data.message,
                    icon: 'success',
                    confirmButtonText: 'OK',
                });

                form.reset();
            } else {
                Swal.fire({
                    title: 'Error!',
                    text: data.message || 'Hubo un problema. Por favor, intente nuevamente.',
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
    console.log('Form with ID "estuForm" not found!');
}
//   End register student block
});