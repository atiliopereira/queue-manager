
var llamados = [];
var pendientes = [];

$(document).ready(function () {

    $('.modal').modal({
            dismissible: true, // Modal can be dismissed by clicking outside of the modal
            opacity: .5, // Opacity of modal background
            inDuration: 300, // Transition in duration
            outDuration: 200, // Transition out duration
            startingTop: '4%', // Starting top style attribute
            endingTop: '10%' // Ending top style attribute
        }
    );


    $('#boton-prueba').click(function () {
        $('.modal').modal('open');
    });
    load(llamados, pendientes);
});

function load(llamados, pendientes){
    $.ajax({
        url: "/turno/turno/api/get_tickets",
        type: 'get',
        success: function (data) {
            cargar_pendientes(data, pendientes);
            cargar_llamados(data, llamados);
        },
        error: function (ex) {
            console.log('error '+ ex)
        }
    });
    setTimeout(function () {load(llamados, pendientes);}, 1000);
}

function cargar_pendientes(data, pendientes) {
    var tickets = data['tickets'];
    var tickets_id = [];
    $.each(tickets, function (i, obj) {
        // si no se encuentra en la lista se agrega
        tickets_id.push(obj.id);
        var id = 'espera_'+obj.id;
        var selector = '#'+id;
        if($(selector).length==0){
            pendientes.push(obj.id);
            $('#espera_table').append('' +
                '<tr id="'+id+'">' +
                '<td>'+obj.cliente+'</td>' +
                '<td>'+obj.sector+'</td>' +
                '<td>'+obj.box+'</td>');
        }

    });
    // si se encontraba en la lista y ahora no, se elimina
    $.each(pendientes, function (i, pend) {
        var tr_remove = '#espera_' + pend;
        if($.inArray(pend, tickets_id)<0){
            $(tr_remove).remove();
            pendientes.splice(pendientes.indexOf(pend), 1)
        }
    })
}
function cargar_llamados(data, llamados) {
    var tickets = data['llamados'];
    var tickets_id = [];
    $.each(tickets, function (i, obj) {
        // si no se encuentra en la lista se agrega
        tickets_id.push(obj.id);
        var id = 'llamado_'+obj.id;
        var selector = '#'+id;
        if($(selector).length==0){
            llamados.push(obj.id);
            cargar_modal(obj.sector, obj.cliente, obj.box);
            $(".modal").modal('open');
            setTimeout(function () {
                $('.modal').modal('close');
            }, 6000);
            $('#llamados_table').prepend('' +
                '<tr id="'+id+'">' +
                '<td>'+obj.cliente+'</td>' +
                '<td>'+obj.sector+'</td>' +
                '<td>'+obj.box+'</td>');
        }


    });
    // si se encontraba en la lista y ahora no, se elimina
    $.each(llamados, function (i, called) {
        var tr_remove = '#llamado_' + called;
        if($.inArray(called, tickets_id)<0){
            $(tr_remove).remove();
            llamados.splice(llamados.indexOf(called), 1)
        }
    })
}
function cargar_modal(sector, cliente, box){
    document.getElementById('audio').play();
    $('#modal_sector_id').html('<h2><strong>SECTOR: ' + sector+'</strong></h2>');
    $('#modal_paragraph_id').html('<h2> <strong>'+ cliente + '</strong> &nbsp;&nbsp;&nbsp;&nbsp; <strong>"' + box +'"</strong> </h2>');
}