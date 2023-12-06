
document.addEventListener("DOMContentLoaded", function () {
    var tipoUsuario = document.getElementById("id_tipo_usuario");
    var campos = document.querySelectorAll(".tipo-campo");

    tipoUsuario.addEventListener("change", function () {
        campos.forEach(function(campo) {
            campo.style.display = "none";
        });

        var tipoSeleccionado = tipoUsuario.value;
        if (tipoSeleccionado) {
            var campoMostrar = document.getElementById("campos_" + tipoSeleccionado.toLowerCase());
            campoMostrar.style.display = "block";
        }
    });

    tipoUsuario.dispatchEvent(new Event("change"));
});
