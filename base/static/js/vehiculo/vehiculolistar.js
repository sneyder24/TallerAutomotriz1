$(document).ready(function() {
    var table = $('#vehiculos-table').DataTable({
    dom: 'Bfrtip',
    buttons: [
        {
            extend: 'copy',
            className: 'btn btn-secondary btn-lg me-1',
            text: '<i class="bi bi-files"></i> Copiar'
        },
        {
            extend: 'excel',
            className: 'btn btn-secondary btn-lg me-1',
            text: '<i class="bi bi-file-earmark-excel"></i> Excel'
        },
        {
            extend: 'pdf',
            className: 'btn btn-secondary btn-lg me-1',
            text: '<i class="bi bi-file-earmark-pdf"></i> PDF'
        },
        {
            extend: 'print',
            className: 'btn btn-secondary btn-lg me-1',
            text: '<i class="bi bi-printer"></i> Imprimir'
        }
    ],
    language: {
        emptyTable: 'No hay datos disponibles en la tabla',
        zeroRecords: 'No se encontraron registros coincidentes',
        info: 'Mostrando _START_ a _END_ de _TOTAL_ registros',
        infoEmpty: 'Mostrando 0 a 0 de 0 registros',
        lengthMenu: 'Mostrar _MENU_ registros por página',
        search: 'Buscar:',
        paginate: {
            first: 'Primero',
            last: 'Último',
            next: 'Siguiente',
            previous: 'Anterior'
        }
    }
});
table.buttons().nodes().addClass('btn-sm');
});