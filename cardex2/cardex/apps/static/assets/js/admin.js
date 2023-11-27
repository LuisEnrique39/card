/* Javascript para esconder el boton de agregar puesto nuevo */

document.getElementById('mostrar-formulario').addEventListener('click', function () {
    var formulario = document.getElementById('formulario');
    var mostrarBoton = document.getElementById('mostrar-formulario');
    var ocultarBoton = document.getElementById('ocultar-formulario');

    if (formulario.style.display === 'none') {
        formulario.style.display = 'block';
        mostrarBoton.style.display = 'none';
        ocultarBoton.style.display = 'block';
    }
});

document.getElementById('ocultar-formulario').addEventListener('click', function () {
    var formulario = document.getElementById('formulario');
    var mostrarBoton = document.getElementById('mostrar-formulario');
    var ocultarBoton = document.getElementById('ocultar-formulario');

    if (formulario.style.display === 'block') {
        formulario.style.display = 'none';
        mostrarBoton.style.display = 'block';
        ocultarBoton.style.display = 'none';
    }
});


/* modal de detalle puesto */
$(document).ready(function() {
    // Asigna un evento 'click' a todos los elementos con la clase 'ver-detalle'
    $('.ver-detalle').click(function() {
        // Encuentra el modal que corresponde al elemento clickeado
        var modalId = $(this).data('target');
        var modal = $(modalId);

        // Muestra el modal
        modal.modal('show');
    });
});


