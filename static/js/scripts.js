// Archivo JS para añadir interactividad
// En este ejemplo se previene el envío real del formulario de contacto
// mostrando un mensaje en consola.

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#contacto form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            console.log('Formulario enviado (demo)');
            alert('Gracias por tu mensaje!');
        });
    }
});
