function fetchMonoInfo(monoId) {
    fetch("{% url 'index' %}", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken')  // Ensure CSRF token is passed
        },
        body: JSON.stringify({
            'mono_id': monoId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Construct the modal content with the student and professors info
            const modalBody = document.getElementById('modalBodyContent');
            modalBody.innerHTML = `
                <p><strong>Estudiante:</strong> ${data.estudiante.nombres} ${data.estudiante.apellidos}</p>
                <p><strong>Profesores asignados:</strong></p>
                <ul>
                    ${data.profesores.map(prof => `
                        <li>${prof.nombre} - ${prof.rol}</li>
                    `).join('')}
                </ul>
            `;
        } else {
            alert("Error: " + data.message);
        }
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}

// Utility function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}