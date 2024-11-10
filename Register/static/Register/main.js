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


  
});





