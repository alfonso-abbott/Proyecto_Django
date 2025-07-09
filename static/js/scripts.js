// Archivo JS para añadir interactividad
// En este ejemplo se previene el envío real del formulario de contacto
// mostrando un mensaje en consola.

/*
Archivo JavaScript principal para la página.

Se encarga de dos tareas:
1. Mostrar un mensaje cuando el usuario envía el formulario de contacto.
2. Activar o desactivar el modo oscuro al presionar un botón.
*/

document.addEventListener('DOMContentLoaded', () => {
    // --- Manejo del formulario de contacto ---
    const form = document.querySelector('#contacto form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            console.log('Formulario enviado (demo)');
            alert('Gracias por tu mensaje!');
        });
    }

    // --- Funcionalidad de modo oscuro ---
    const toggle = document.getElementById('btn-dark-mode');
    if (toggle) {
        toggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
        });
    }
});
