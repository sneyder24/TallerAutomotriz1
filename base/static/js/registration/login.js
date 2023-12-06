$(document).ready(function() {
        $('form').submit(function(event) {
            if (!$('.terms-checkbox').is(':checked')) {
                event.preventDefault(); // Evita que se envíe el formulario
                alert('Debes aceptar los términos y condiciones');
            }
        });
    });
