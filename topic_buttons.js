







$(document).ready(function () {
    $("button").on({
        click:function(){
            if ($(this).attr('on')==='0'){
                $(this).attr('on','1');
                let c = $(this).attr('topic');
                $(`button[topic='${c}']`).addClass('green');
                $(`button[topic='${c}']`).closest('tr').addClass('green');
            }
            else {
                let c = $(this).attr('topic');
                $(this).attr('on','0');
                $(`button[topic='${c}']`).removeClass('green');
                $(`button[topic='${c}']`).closest('tr').removeClass('green');
                $(`button[on='1']`).closest('tr').addClass('green');
            }
        }
    });
});