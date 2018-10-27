
function motor_go(LR){
    $.ajax({
        url: '/motor_forward',
        type:'POST',
        dataType: 'json',
        data:{'speed': $('#motor_speed').val(), 'LR':LR},
        timeout:1000,
    }).done(function(data){
        this.backgroundColor = "red";
    }).fail(function(XMLHttpRequest,textStatus, errorThrown){
        //
    });
}

function motor_back(LR){
    $.ajax({
        url: '/motor_back',
        type:'POST',
        dataType: 'json',
        data:{'speed': $('#motor_speed').val(), 'LR':LR},
        timeout:1000,
    }).done(function(data){
        this.background.color = "yellow";
        //
    }).fail(function(XMLHttpRequest,textStatus, errorThrown){
        //
    });
}

function motor_stop(LR){
    $.ajax({
        url: '/motor_stop',
        dataType: 'json',
        data:{'LR': LR},
        type:'POST',
        timeout:1000,
    }).done(function(data){
        //
    }).fail(function(XMLHttpRequest,textStatus, errorThrown){
        //
    });
}



