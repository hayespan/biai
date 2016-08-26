$(document).ready(function() {
	$('#creativity-sketch').sketch();

	$('.form-verify-phone button').on('click', function(e) {
		e.preventDefault();
		var mobile_num = $('#mobile').val();
		$.ajax({
			url : '/captcha/mobile_trigger?f=json',
			type : 'POST',
			data : {
				mobile : mobile_num
			},
			success : function(result) {
				console.log(result);
			}
		});
	});

	$('form').on('submit', function(e) {
		e.preventDefault();
		// console.log($('#creativity-sketch').get(0).toDataURL());
		// console.log($("form input[type=file]")[0].files[0]);
		var valid_code = $('#valid-code').val();
		$.ajax({
			url : '/captcha/mobile_check?f=json',
			type : 'POST',
			data : {
				code : valid_code
			},
			success : function(result) {
				if (result.correct) {
					upload_work();
				} else {
					// console.log('verify failed!');
					upload_work();
				}
			}
		});
	});

	function upload_work() {
		var form_data = new FormData();
		if ($("form input[type=file]")[0].files[0]) {
			form_data.append("img", $("form input[type=file]")[0].files[0]);
			console.log($("form input[type=file]")[0].files[0]);
		} else {
			form_data.append("img", $('#creativity-sketch').get(0).toDataURL());
			console.log($('#creativity-sketch').get(0).toDataURL());
		}
		console.log(form_data.get('img'));
		$.ajax({
			url : '/creativity/post?f=json',
			type : 'POST',
			data: form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
			}
		});
	}
})
