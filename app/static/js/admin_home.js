$(document).ready(function () {
    var ajaxData = {
        url: '/admin/home/',
        type: 'POST',
        dataType: 'json',
        data: '',
        processData: false,
        contentType: 'application/json;charset=UTF-8'
    };
    $('#poster button.change_poster').each(function (index) {
        $(this).click(function () {
            var id = $('#poster tr').eq(index + 1).children('td').length;
            console.log(id);
        });
    });
    $('#poster button.delete_poster').each(function (index) {
        $(this).click(function () {
            var id = $('#poster tr').eq(index + 1).children('td').eq(0).text();
            ajaxData.url = '/admin/home/' + 'del_poster';
            ajaxData.data = JSON.stringify({
                'id': parseInt(id)
            });
            $.ajax(ajaxData);
        });
    });
    $('#video button.delete_video').each(function (index) {
        $(this).click(function () {
            var id = $('#video tr').eq(index + 1).children('td').eq(0).text();
            ajaxData.url = '/admin/home/' + 'del_video';
            ajaxData.data = JSON.stringify({
                'id': parseInt(id)
            });
            $.ajax(ajaxData);
        });
    });

    $('#news button.hide_show').each(function (index) {
        $(this).click(function () {
            if($(this).text() == '显示') {
                ajaxData.url = '/admin/home/' + 'show_new';
                $(this).text('不显示');
            } else {
                ajaxData.url = '/admin/home/' + 'hide_new';
                $(this).text('显示');
            }
            var id = $('#news tr').eq(index + 1).children('td').eq(0).text();
            console.log(id);
            ajaxData.data = JSON.stringify({
                'id': parseInt(id)
            });
            $.ajax(ajaxData);
        });
    });

    $('#news button.choose_new').each(function (index) {
        $(this).click(function () {
            $('#new_input').show();
            var id = $('#news tr').eq(index + 1).children('td').eq(0).text();
            $('#new_input button').click(function () {
                var name = $('#new_input input').val();
                ajaxData.url = '/admin/home/' + 'change_new';
                ajaxData.data = JSON.stringify({
                    'id': parseInt(id),
                    'name': name
                });
                $.ajax(ajaxData);
            });
        });
    });

    $('#classify button.classify').each(function (index) {
        $(this).click(function () {
            var id = $('#classify tr').eq(index + 1).children('td').eq(0).text();
            var val = $('#classify tr').eq(index + 1).children('td').eq(1).text();
            $('#classify_form').show();
            $('#classify_form input').eq(0).val(id);
            $('#classify_form input').eq(1).val(val);
        });
    });
});