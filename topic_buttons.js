







$(document).ready(function () {
    $("button").on({
        click:function(){
            if ($(this).attr('on')==='0'){
                let c = $(this).attr('topic');
                $(`button[topic='${c}']`).addClass('green');
                $(`button[topic='${c}']`).closest('tr').addClass('green');
                $(this).attr('on','1');
            }
            else {
                let c = $(this).attr('topic');
                $(`button[topic='${c}']`).removeClass('green');
                $(`button[topic='${c}']`).closest('tr').removeClass('green');
                $(this).attr('on','0');
            }
        }
    });
});