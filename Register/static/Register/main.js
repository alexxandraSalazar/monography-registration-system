document.body.addEventListener('htmx:afterOnLoad', function(event) {
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
});
