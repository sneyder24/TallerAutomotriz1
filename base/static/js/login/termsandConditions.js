$(document).ready(function() {
    $('form').submit(function(event) {
        if (!$('.terms-checkbox').is(':checked')) {
            event.preventDefault(); 
            alert('Debes aceptar los términos y condiciones');
        }
    });
});