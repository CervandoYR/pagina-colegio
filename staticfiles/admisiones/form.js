document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const alertSuccess = document.querySelector('.alert');

    form.addEventListener('submit', function(event) {
        // Mostrar la alerta al enviar el formulario
        alertSuccess.classList.add('show');
        
        // Ocultar la alerta después de 3 segundos
        setTimeout(() => {
            alertSuccess.classList.remove('show');
        }, 3000);

        // Limpiar todos los campos del formulario
        form.reset();
    });
});

