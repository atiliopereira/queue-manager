/**
 * Created by dissoi on 08/02/17.
 */
$(document).ready(function () {
    var aux = $('input[name=sitio]:checked').val() || '';
    $('#id_box').parent().css('display',(aux.indexOf('B') != -1)? 'block':'none');
    $('input[type=radio][name=sitio]').click(function () {
        $('#id_box').parent().css('display', ($(this).val().indexOf('B') != -1) ? 'block' : 'none');
    });


});