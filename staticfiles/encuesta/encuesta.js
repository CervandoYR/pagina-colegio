document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const alertSuccess = document.querySelector('.alert');

    form.addEventListener('submit', function(event) {
        alertSuccess.classList.add('show');
        
        setTimeout(() => {
            alertSuccess.classList.remove('show');
        }, 3000);

        form.reset();
    });
});
