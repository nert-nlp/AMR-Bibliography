







$(document).ready(function () {
    $("button").on({
        click:function(){
            if ($(this).attr('on')==='0'){
                let c = $(this).attr('topic');
                $(`button[topic='${c}']`).attr('on','1');
                $(`button[topic='${c}']`).addClass('green');
                $(`button[topic='${c}']`).closest('tr').addClass('green');
            }
            else {
                let c = $(this).attr('topic');
                $(`button[topic='${c}']`).attr('on','0');
                $(`button[topic='${c}']`).removeClass('green');
                $(`button[topic='${c}']`).closest('tr').removeClass('green');
                $(`button[on='1']`).closest('tr').addClass('green');
            }
        }
    });
});