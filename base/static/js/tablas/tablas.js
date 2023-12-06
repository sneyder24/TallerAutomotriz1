new DataTable('#example', {
    language: {
        url: '//cdn.datatables.net/plug-ins/1.13.6/i18n/es-CO.json',
    },
    lengthmenu: [5,10,25,50],
    responsive: true,
    columnDefs: [
    { responsivePriority: 1, targets:1 },
    { responsivePriority: 2, targets: 9 },
    { responsivePriority: 3, targets: 10 }],
    dom: 'Bfrtip',
    buttons:{
        buttons:[
        {
        extend:'copy',
        text:'<i class="bi bi-clipboard-fill"></i>',
        titleAttr:'copiar',
        className:'my-2 btn fondtable'
        },
        {
        extend:'excel',
        text:'<i class="bi bi-filetype-exe"></i>',
        titleAttr:'exportar a excel',
        className:'btn fondtable my-2'
        },
        {
        extend:'pdf',
        text:'<i class="bi bi-filetype-pdf"></i>',
        titleAttr:'exportar a pdf',
        className:'btn fondtable my-2'
        },
        {
        extend:'print',
        text:'<i class="bi bi-printer-fill"></i>',
        titleAttr:'imprimir',
        className:'btn fondtable my-2'
        },
        {
        extend:'colvis',
        text:'<i class="bi bi-eye-fill"></i>',
        titleAttr:'imprimir',
        className:'btn fondtable my-2'
        },
        ]
    }
    });