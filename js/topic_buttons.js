







$(document).ready(function () {
    $("table").tablesorter({
        sortList: [[0,1]]   // row number desc (most recently added first)
        //sortList: [[4,1], [2,0]] // year desc, title asc
    });
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
