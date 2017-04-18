function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    var clock = document.getElementById('id_current_time');
    if (clock){
        clock.innerHTML =h + ":" + m + ":" + s;
        var t = setTimeout(startTime, 500);
    }

}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

function today(){
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    if(dd<10) {
        dd='0'+dd
    }

    if(mm<10) {
        mm='0'+mm
    }

    var current_date = document.getElementById('id_current_date');
    if(current_date){
        current_date.innerHTML =     mm+'/'+dd+'/'+yyyy;
    }

}
$(document).ready(function () {
    startTime();
    today();
});

