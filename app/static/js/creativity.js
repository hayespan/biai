$(document).ready(function() {
	$('#creativity-sketch').sketch();

	$('#choose-color').on('click', function(e) {
		e.preventDefault();
		$('.color-dropdown').removeClass('hidden');
	});

	$('.color-dropdown a').on('click', function(e) {
		var color = this.dataset.color;
		$('#choose-color').css("background-color", color);
		$('.color-dropdown').addClass('hidden');
	});

	$('#choose-size').on('click', function(e) {
		e.preventDefault();
		$('.size-dropdown').removeClass('hidden');
	});

	$('.size-dropdown a').on('click', function(e) {
		var size = this.dataset.size;
		$('#choose-size').text(size);
		$('.size-dropdown').addClass('hidden');
	});

	$('.form-verify-phone button').on('click', function(e) {
		e.preventDefault();
		var that = $(this);
		var mobile_num = $('#mobile').val();
		if (!mobile_num) {
			$(this).siblings('.alert-hint').text('还没填手机号码呢亲');
			$(this).siblings('.alert-hint').removeClass('hidden');
			return false;
		}
		$.ajax({
			url : '/captcha/mobile_trigger?f=json',
			type : 'POST',
			data : {
				mobile : mobile_num
			},
			success : function(result) {
				if (result.data.msg == 'invalid mobile') {
					that.siblings('.alert-hint').text('手机号码格式有误');
					that.siblings('.alert-hint').removeClass('hidden');
				} else if (result.data.msg == 'send fail') {
					that.siblings('.alert-hint').text('发送失败请重试');
					that.siblings('.alert-hint').removeClass('hidden');
				} else {
					that.siblings('.alert-hint').addClass('hidden');
					that.attr('disabled', 'disabled');
					that.addClass('disabled');
					that.text('已发送(60)');
					var count = 59;
					var clock = setInterval(function() {
						that.text('已发送('+count+')');
						if (count == 0) {
							clearInterval(clock);
							that.removeClass('disabled');
							that.removeAttr('disabled');
							that.text('发送验证码');
						}
						count--;
					}, 1000);
				}
			}
		});
	});

	$('.creativity-form').on('submit', function(e) {
		e.preventDefault();
		var valid_code = $('#verify-code').val();
		$.ajax({
			url : '/captcha/mobile_check?f=json',
			type : 'POST',
			data : {
				code : valid_code
			},
			success : function(result) {
				if (result.data.correct) {
					upload_work();
				} else {
					// upload_work();
					$('#verify-code').siblings('.alert-hint').text('验证码有误请重试');
					$('#verify-code').siblings('.alert-hint').removeClass('hidden');
				}
			}
		});
	});

	$('.form-item input').on('click', function() {
		$(this).siblings('.alert-hint').addClass('hidden');
	})

	function upload_work() {
		var form_data = new FormData();
		form_data.append("code", $('#verify-code').val());
		form_data.append("mobile", $('#mobile').val());
		console.log(form_data.get('code'));
		console.log(form_data.get('mobile'));
		if ($("form input[type=file]")[0].files[0]) {
			form_data.append("img", $("form input[type=file]")[0].files[0]);
		} 
		if ($('#creativity-sketch').get(0).toDataURL() != 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA9QAAAG4CAYAAACkfa+MAAAgAElEQVR4Xu3XoREAAAjEMNh/aWagOvg3OUx3HAECBAgQIECAAAECBAgQIPAW2PfCgAABAgQIECBAgAABAgQIEBhB7QkIECBAgAABAgQIECBAgEAQENQBzYQAAQIECBAgQIAAAQIECAhqP0CAAAECBAgQIECAAAECBIKAoA5oJgQIECBAgAABAgQIECBAQFD7AQIECBAgQIAAAQIECBAgEAQEdUAzIUCAAAECBAgQIECAAAECgtoPECBAgAABAgQIECBAgACBICCoA5oJAQIECBAgQIAAAQIECBAQ1H6AAAECBAgQIECAAAECBAgEAUEd0EwIECBAgAABAgQIECBAgICg9gMECBAgQIAAAQIECBAgQCAICOqAZkKAAAECBAgQIECAAAECBAS1HyBAgAABAgQIECBAgAABAkFAUAc0EwIECBAgQIAAAQIECBAgIKj9AAECBAgQIECAAAECBAgQCAKCOqCZECBAgAABAgQIECBAgAABQe0HCBAgQIAAAQIECBAgQIBAEBDUAc2EAAECBAgQIECAAAECBAgIaj9AgAABAgQIECBAgAABAgSCgKAOaCYECBAgQIAAAQIECBAgQEBQ+wECBAgQIECAAAECBAgQIBAEBHVAMyFAgAABAgQIECBAgAABAoLaDxAgQIAAAQIECBAgQIAAgSAgqAOaCQECBAgQIECAAAECBAgQENR+gAABAgQIECBAgAABAgQIBAFBHdBMCBAgQIAAAQIECBAgQICAoPYDBAgQIECAAAECBAgQIEAgCAjqgGZCgAABAgQIECBAgAABAgQEtR8gQIAAAQIECBAgQIAAAQJBQFAHNBMCBAgQIECAAAECBAgQICCo/QABAgQIECBAgAABAgQIEAgCgjqgmRAgQIAAAQIECBAgQIAAAUHtBwgQIECAAAECBAgQIECAQBAQ1AHNhAABAgQIECBAgAABAgQICGo/QIAAAQIECBAgQIAAAQIEgoCgDmgmBAgQIECAAAECBAgQIEBAUPsBAgQIECBAgAABAgQIECAQBAR1QDMhQIAAAQIECBAgQIAAAQKC2g8QIECAAAECBAgQIECAAIEgIKgDmgkBAgQIECBAgAABAgQIEBDUfoAAAQIECBAgQIAAAQIECAQBQR3QTAgQIECAAAECBAgQIECAgKD2AwQIECBAgAABAgQIECBAIAgI6oBmQoAAAQIECBAgQIAAAQIEBLUfIECAAAECBAgQIECAAAECQUBQBzQTAgQIECBAgAABAgQIECAgqP0AAQIECBAgQIAAAQIECBAIAoI6oJkQIECAAAECBAgQIECAAAFB7QcIECBAgAABAgQIECBAgEAQENQBzYQAAQIECBAgQIAAAQIECAhqP0CAAAECBAgQIECAAAECBIKAoA5oJgQIECBAgAABAgQIECBAQFD7AQIECBAgQIAAAQIECBAgEAQEdUAzIUCAAAECBAgQIECAAAECgtoPECBAgAABAgQIECBAgACBICCoA5oJAQIECBAgQIAAAQIECBAQ1H6AAAECBAgQIECAAAECBAgEAUEd0EwIECBAgAABAgQIECBAgICg9gMECBAgQIAAAQIECBAgQCAICOqAZkKAAAECBAgQIECAAAECBAS1HyBAgAABAgQIECBAgAABAkFAUAc0EwIECBAgQIAAAQIECBAgIKj9AAECBAgQIECAAAECBAgQCAKCOqCZECBAgAABAgQIECBAgAABQe0HCBAgQIAAAQIECBAgQIBAEBDUAc2EAAECBAgQIECAAAECBAgIaj9AgAABAgQIECBAgAABAgSCgKAOaCYECBAgQIAAAQIECBAgQEBQ+wECBAgQIECAAAECBAgQIBAEBHVAMyFAgAABAgQIECBAgAABAoLaDxAgQIAAAQIECBAgQIAAgSAgqAOaCQECBAgQIECAAAECBAgQENR+gAABAgQIECBAgAABAgQIBAFBHdBMCBAgQIAAAQIECBAgQICAoPYDBAgQIECAAAECBAgQIEAgCAjqgGZCgAABAgQIECBAgAABAgQEtR8gQIAAAQIECBAgQIAAAQJBQFAHNBMCBAgQIECAAAECBAgQICCo/QABAgQIECBAgAABAgQIEAgCgjqgmRAgQIAAAQIECBAgQIAAAUHtBwgQIECAAAECBAgQIECAQBAQ1AHNhAABAgQIECBAgAABAgQICGo/QIAAAQIECBAgQIAAAQIEgoCgDmgmBAgQIECAAAECBAgQIEBAUPsBAgQIECBAgAABAgQIECAQBAR1QDMhQIAAAQIECBAgQIAAAQKC2g8QIECAAAECBAgQIECAAIEgIKgDmgkBAgQIECBAgAABAgQIEBDUfoAAAQIECBAgQIAAAQIECAQBQR3QTAgQIECAAAECBAgQIECAgKD2AwQIECBAgAABAgQIECBAIAgI6oBmQoAAAQIECBAgQIAAAQIEBLUfIECAAAECBAgQIECAAAECQUBQBzQTAgQIECBAgAABAgQIECAgqP0AAQIECBAgQIAAAQIECBAIAoI6oJkQIECAAAECBAgQIECAAAFB7QcIECBAgAABAgQIECBAgEAQENQBzYQAAQIECBAgQIAAAQIECAhqP0CAAAECBAgQIECAAAECBIKAoA5oJgQIECBAgAABAgQIECBAQFD7AQIECBAgQIAAAQIECBAgEAQEdUAzIUCAAAECBAgQIECAAAECgtoPECBAgAABAgQIECBAgACBICCoA5oJAQIECBAgQIAAAQIECBAQ1H6AAAECBAgQIECAAAECBAgEAUEd0EwIECBAgAABAgQIECBAgICg9gMECBAgQIAAAQIECBAgQCAICOqAZkKAAAECBAgQIECAAAECBAS1HyBAgAABAgQIECBAgAABAkFAUAc0EwIECBAgQIAAAQIECBAgIKj9AAECBAgQIECAAAECBAgQCAKCOqCZECBAgAABAgQIECBAgAABQe0HCBAgQIAAAQIECBAgQIBAEBDUAc2EAAECBAgQIECAAAECBAgIaj9AgAABAgQIECBAgAABAgSCgKAOaCYECBAgQIAAAQIECBAgQEBQ+wECBAgQIECAAAECBAgQIBAEBHVAMyFAgAABAgQIECBAgAABAoLaDxAgQIAAAQIECBAgQIAAgSAgqAOaCQECBAgQIECAAAECBAgQENR+gAABAgQIECBAgAABAgQIBAFBHdBMCBAgQIAAAQIECBAgQICAoPYDBAgQIECAAAECBAgQIEAgCAjqgGZCgAABAgQIECBAgAABAgQEtR8gQIAAAQIECBAgQIAAAQJBQFAHNBMCBAgQIECAAAECBAgQICCo/QABAgQIECBAgAABAgQIEAgCgjqgmRAgQIAAAQIECBAgQIAAAUHtBwgQIECAAAECBAgQIECAQBAQ1AHNhAABAgQIECBAgAABAgQICGo/QIAAAQIECBAgQIAAAQIEgoCgDmgmBAgQIECAAAECBAgQIEBAUPsBAgQIECBAgAABAgQIECAQBAR1QDMhQIAAAQIECBAgQIAAAQKC2g8QIECAAAECBAgQIECAAIEgIKgDmgkBAgQIECBAgAABAgQIEBDUfoAAAQIECBAgQIAAAQIECAQBQR3QTAgQIECAAAECBAgQIECAgKD2AwQIECBAgAABAgQIECBAIAgI6oBmQoAAAQIECBAgQIAAAQIEBLUfIECAAAECBAgQIECAAAECQUBQBzQTAgQIECBAgAABAgQIECAgqP0AAQIECBAgQIAAAQIECBAIAoI6oJkQIECAAAECBAgQIECAAAFB7QcIECBAgAABAgQIECBAgEAQENQBzYQAAQIECBAgQIAAAQIECAhqP0CAAAECBAgQIECAAAECBIKAoA5oJgQIECBAgAABAgQIECBAQFD7AQIECBAgQIAAAQIECBAgEAQEdUAzIUCAAAECBAgQIECAAAECgtoPECBAgAABAgQIECBAgACBICCoA5oJAQIECBAgQIAAAQIECBAQ1H6AAAECBAgQIECAAAECBAgEAUEd0EwIECBAgAABAgQIECBAgICg9gMECBAgQIAAAQIECBAgQCAICOqAZkKAAAECBAgQIECAAAECBAS1HyBAgAABAgQIECBAgAABAkFAUAc0EwIECBAgQIAAAQIECBAgIKj9AAECBAgQIECAAAECBAgQCAKCOqCZECBAgAABAgQIECBAgAABQe0HCBAgQIAAAQIECBAgQIBAEBDUAc2EAAECBAgQIECAAAECBAgIaj9AgAABAgQIECBAgAABAgSCgKAOaCYECBAgQIAAAQIECBAgQEBQ+wECBAgQIECAAAECBAgQIBAEBHVAMyFAgAABAgQIECBAgAABAoLaDxAgQIAAAQIECBAgQIAAgSAgqAOaCQECBAgQIECAAAECBAgQENR+gAABAgQIECBAgAABAgQIBAFBHdBMCBAgQIAAAQIECBAgQICAoPYDBAgQIECAAAECBAgQIEAgCAjqgGZCgAABAgQIECBAgAABAgQEtR8gQIAAAQIECBAgQIAAAQJBQFAHNBMCBAgQIECAAAECBAgQICCo/QABAgQIECBAgAABAgQIEAgCgjqgmRAgQIAAAQIECBAgQIAAAUHtBwgQIECAAAECBAgQIECAQBAQ1AHNhAABAgQIECBAgAABAgQICGo/QIAAAQIECBAgQIAAAQIEgoCgDmgmBAgQIECAAAECBAgQIEBAUPsBAgQIECBAgAABAgQIECAQBAR1QDMhQIAAAQIECBAgQIAAAQKC2g8QIECAAAECBAgQIECAAIEgIKgDmgkBAgQIECBAgAABAgQIEBDUfoAAAQIECBAgQIAAAQIECAQBQR3QTAgQIECAAAECBAgQIECAgKD2AwQIECBAgAABAgQIECBAIAgI6oBmQoAAAQIECBAgQIAAAQIEBLUfIECAAAECBAgQIECAAAECQUBQBzQTAgQIECBAgAABAgQIECAgqP0AAQIECBAgQIAAAQIECBAIAoI6oJkQIECAAAECBAgQIECAAAFB7QcIECBAgAABAgQIECBAgEAQENQBzYQAAQIECBAgQIAAAQIECAhqP0CAAAECBAgQIECAAAECBIKAoA5oJgQIECBAgAABAgQIECBAQFD7AQIECBAgQIAAAQIECBAgEAQEdUAzIUCAAAECBAgQIECAAAECgtoPECBAgAABAgQIECBAgACBICCoA5oJAQIECBAgQIAAAQIECBAQ1H6AAAECBAgQIECAAAECBAgEAUEd0EwIECBAgAABAgQIECBAgICg9gMECBAgQIAAAQIECBAgQCAICOqAZkKAAAECBAgQIECAAAECBAS1HyBAgAABAgQIECBAgAABAkFAUAc0EwIECBAgQIAAAQIECBAgIKj9AAECBAgQIECAAAECBAgQCAKCOqCZECBAgAABAgQIECBAgAABQe0HCBAgQIAAAQIECBAgQIBAEBDUAc2EAAECBAgQIECAAAECBAgIaj9AgAABAgQIECBAgAABAgSCgKAOaCYECBAgQIAAAQIECBAgQEBQ+wECBAgQIECAAAECBAgQIBAEBHVAMyFAgAABAgQIECBAgAABAoLaDxAgQIAAAQIECBAgQIAAgSAgqAOaCQECBAgQIECAAAECBAgQENR+gAABAgQIECBAgAABAgQIBAFBHdBMCBAgQIAAAQIECBAgQICAoPYDBAgQIECAAAECBAgQIEAgCAjqgGZCgAABAgQIECBAgAABAgQEtR8gQIAAAQIECBAgQIAAAQJBQFAHNBMCBAgQIECAAAECBAgQICCo/QABAgQIECBAgAABAgQIEAgCgjqgmRAgQIAAAQIECBAgQIAAAUHtBwgQIECAAAECBAgQIECAQBAQ1AHNhAABAgQIECBAgAABAgQICGo/QIAAAQIECBAgQIAAAQIEgoCgDmgmBAgQIECAAAECBAgQIEBAUPsBAgQIECBAgAABAgQIECAQBAR1QDMhQIAAAQIECBAgQIAAAQKC2g8QIECAAAECBAgQIECAAIEgIKgDmgkBAgQIECBAgAABAgQIEBDUfoAAAQIECBAgQIAAAQIECAQBQR3QTAgQIECAAAECBAgQIECAgKD2AwQIECBAgAABAgQIECBAIAgI6oBmQoAAAQIECBAgQIAAAQIEBLUfIECAAAECBAgQIECAAAECQUBQBzQTAgQIECBAgAABAgQIECAgqP0AAQIECBAgQIAAAQIECBAIAoI6oJkQIECAAAECBAgQIECAAAFB7QcIECBAgAABAgQIECBAgEAQENQBzYQAAQIECBAgQIAAAQIECAhqP0CAAAECBAgQIECAAAECBIKAoA5oJgQIECBAgAABAgQIECBAQFD7AQIECBAgQIAAAQIECBAgEAQEdUAzIUCAAAECBAgQIECAAAECgtoPECBAgAABAgQIECBAgACBICCoA5oJAQIECBAgQIAAAQIECBAQ1H6AAAECBAgQIECAAAECBAgEAUEd0EwIECBAgAABAgQIECBAgICg9gMECBAgQIAAAQIECBAgQCAICOqAZkKAAAECBAgQIECAAAECBAS1HyBAgAABAgQIECBAgAABAkFAUAc0EwIECBAgQIAAAQIECBAgIKj9AAECBAgQIECAAAECBAgQCAKCOqCZECBAgAABAgQIECBAgAABQe0HCBAgQIAAAQIECBAgQIBAEBDUAc2EAAECBAgQIECAAAECBAgIaj9AgAABAgQIECBAgAABAgSCgKAOaCYECBAgQIAAAQIECBAgQEBQ+wECBAgQIECAAAECBAgQIBAEBHVAMyFAgAABAgQIECBAgAABAoLaDxAgQIAAAQIECBAgQIAAgSAgqAOaCQECBAgQIECAAAECBAgQENR+gAABAgQIECBAgAABAgQIBAFBHdBMCBAgQIAAAQIECBAgQICAoPYDBAgQIECAAAECBAgQIEAgCAjqgGZCgAABAgQIECBAgAABAgQEtR8gQIAAAQIECBAgQIAAAQJBQFAHNBMCBAgQIECAAAECBAgQICCo/QABAgQIECBAgAABAgQIEAgCgjqgmRAgQIAAAQIECBAgQIAAAUHtBwgQIECAAAECBAgQIECAQBAQ1AHNhAABAgQIECBAgAABAgQICGo/QIAAAQIECBAgQIAAAQIEgoCgDmgmBAgQIECAAAECBAgQIEBAUPsBAgQIECBAgAABAgQIECAQBAR1QDMhQIAAAQIECBAgQIAAAQKC2g8QIECAAAECBAgQIECAAIEgIKgDmgkBAgQIECBAgAABAgQIEBDUfoAAAQIECBAgQIAAAQIECAQBQR3QTAgQIECAAAECBAgQIECAgKD2AwQIECBAgAABAgQIECBAIAgI6oBmQoAAAQIECBAgQIAAAQIEBLUfIECAAAECBAgQIECAAAECQUBQBzQTAgQIECBAgAABAgQIECAgqP0AAQIECBAgQIAAAQIECBAIAoI6oJkQIECAAAECBAgQIECAAAFB7QcIECBAgAABAgQIECBAgEAQENQBzYQAAQIECBAgQIAAAQIECAhqP0CAAAECBAgQIECAAAECBIKAoA5oJgQIECBAgAABAgQIECBAQFD7AQIECBAgQIAAAQIECBAgEAQEdUAzIUCAAAECBAgQIECAAAECgtoPECBAgAABAgQIECBAgACBICCoA5oJAQIECBAgQIAAAQIECBAQ1H6AAAECBAgQIECAAAECBAgEAUEd0EwIECBAgAABAgQIECBAgICg9gMECBAgQIAAAQIECBAgQCAICOqAZkKAAAECBAgQIECAAAECBAS1HyBAgAABAgQIECBAgAABAkFAUAc0EwIECBAgQIAAAQIECBAgIKj9AAECBAgQIECAAAECBAgQCAKCOqCZECBAgAABAgQIECBAgAABQe0HCBAgQIAAAQIECBAgQIBAEBDUAc2EAAECBAgQIECAAAECBAgIaj9AgAABAgQIECBAgAABAgSCgKAOaCYECBAgQIAAAQIECBAgQEBQ+wECBAgQIECAAAECBAgQIBAEBHVAMyFAgAABAgQIECBAgAABAoLaDxAgQIAAAQIECBAgQIAAgSAgqAOaCQECBAgQIECAAAECBAgQENR+gAABAgQIECBAgAABAgQIBAFBHdBMCBAgQIAAAQIECBAgQICAoPYDBAgQIECAAAECBAgQIEAgCAjqgGZCgAABAgQIECBAgAABAgQEtR8gQIAAAQIECBAgQIAAAQJBQFAHNBMCBAgQIECAAAECBAgQICCo/QABAgQIECBAgAABAgQIEAgCgjqgmRAgQIAAAQIECBAgQIAAAUHtBwgQIECAAAECBAgQIECAQBAQ1AHNhAABAgQIECBAgAABAgQICGo/QIAAAQIECBAgQIAAAQIEgoCgDmgmBAgQIECAAAECBAgQIEBAUPsBAgQIECBAgAABAgQIECAQBAR1QDMhQIAAAQIECBAgQIAAAQKC2g8QIECAAAECBAgQIECAAIEgIKgDmgkBAgQIECBAgAABAgQIEBDUfoAAAQIECBAgQIAAAQIECAQBQR3QTAgQIECAAAECBAgQIECAgKD2AwQIECBAgAABAgQIECBAIAgI6oBmQoAAAQIECBAgQIAAAQIEBLUfIECAAAECBAgQIECAAAECQUBQBzQTAgQIECBAgAABAgQIECAgqP0AAQIECBAgQIAAAQIECBAIAoI6oJkQIECAAAECBAgQIECAAAFB7QcIECBAgAABAgQIECBAgEAQENQBzYQAAQIECBAgQIAAAQIECAhqP0CAAAECBAgQIECAAAECBIKAoA5oJgQIECBAgAABAgQIECBAQFD7AQIECBAgQIAAAQIECBAgEAQEdUAzIUCAAAECBAgQIECAAAECgtoPECBAgAABAgQIECBAgACBICCoA5oJAQIECBAgQIAAAQIECBAQ1H6AAAECBAgQIECAAAECBAgEAUEd0EwIECBAgAABAgQIECBAgICg9gMECBAgQIAAAQIECBAgQCAICOqAZkKAAAECBAgQIECAAAECBAS1HyBAgAABAgQIECBAgAABAkFAUAc0EwIECBAgQIAAAQIECBAgIKj9AAECBAgQIECAAAECBAgQCAKCOqCZECBAgAABAgQIECBAgAABQe0HCBAgQIAAAQIECBAgQIBAEBDUAc2EAAECBAgQIECAAAECBAgIaj9AgAABAgQIECBAgAABAgSCgKAOaCYECBAgQIAAAQIECBAgQEBQ+wECBAgQIECAAAECBAgQIBAEBHVAMyFAgAABAgQIECBAgAABAoLaDxAgQIAAAQIECBAgQIAAgSAgqAOaCQECBAgQIECAAAECBAgQENR+gAABAgQIECBAgAABAgQIBAFBHdBMCBAgQIAAAQIECBAgQICAoPYDBAgQIECAAAECBAgQIEAgCAjqgGZCgAABAgQIECBAgAABAgQEtR8gQIAAAQIECBAgQIAAAQJBQFAHNBMCBAgQIECAAAECBAgQICCo/QABAgQIECBAgAABAgQIEAgCgjqgmRAgQIAAAQIECBAgQIAAAUHtBwgQIECAAAECBAgQIECAQBAQ1AHNhAABAgQIECBAgAABAgQICGo/QIAAAQIECBAgQIAAAQIEgoCgDmgmBAgQIECAAAECBAgQIEBAUPsBAgQIECBAgAABAgQIECAQBAR1QDMhQIAAAQIECBAgQIAAAQKC2g8QIECAAAECBAgQIECAAIEgIKgDmgkBAgQIECBAgAABAgQIEBDUfoAAAQIECBAgQIAAAQIECAQBQR3QTAgQIECAAAECBAgQIECAgKD2AwQIECBAgAABAgQIECBAIAgI6oBmQoAAAQIECBAgQIAAAQIEBLUfIECAAAECBAgQIECAAAECQUBQBzQTAgQIECBAgAABAgQIECAgqP0AAQIECBAgQIAAAQIECBAIAoI6oJkQIECAAAECBAgQIECAAAFB7QcIECBAgAABAgQIECBAgEAQENQBzYQAAQIECBAgQIAAAQIECAhqP0CAAAECBAgQIECAAAECBIKAoA5oJgQIECBAgAABAgQIECBAQFD7AQIECBAgQIAAAQIECBAgEAQEdUAzIUCAAAECBAgQIECAAAECgtoPECBAgAABAgQIECBAgACBICCoA5oJAQIECBAgQIAAAQIECBAQ1H6AAAECBAgQIECAAAECBAgEAUEd0EwIECBAgAABAgQIECBAgICg9gMECBAgQIAAAQIECBAgQCAICOqAZkKAAAECBAgQIECAAAECBAS1HyBAgAABAgQIECBAgAABAkFAUAc0EwIECBAgQIAAAQIECBAgIKj9AAECBAgQIECAAAECBAgQCAKCOqCZECBAgAABAgQIECBAgAABQe0HCBAgQIAAAQIECBAgQIBAEBDUAc2EAAECBAgQIECAAAECBAgIaj9AgAABAgQIECBAgAABAgSCgKAOaCYECBAgQIAAAQIECBAgQEBQ+wECBAgQIECAAAECBAgQIBAEBHVAMyFAgAABAgQIECBAgAABAoLaDxAgQIAAAQIECBAgQIAAgSAgqAOaCQECBAgQIECAAAECBAgQENR+gAABAgQIECBAgAABAgQIBAFBHdBMCBAgQIAAAQIECBAgQICAoPYDBAgQIECAAAECBAgQIEAgCAjqgGZCgAABAgQIECBAgAABAgQEtR8gQIAAAQIECBAgQIAAAQJBQFAHNBMCBAgQIECAAAECBAgQICCo/QABAgQIECBAgAABAgQIEAgCgjqgmRAgQIAAAQIECBAgQIAAAUHtBwgQIECAAAECBAgQIECAQBAQ1AHNhAABAgQIECBAgAABAgQICGo/QIAAAQIECBAgQIAAAQIEgoCgDmgmBAgQIECAAAECBAgQIEBAUPsBAgQIECBAgAABAgQIECAQBAR1QDMhQIAAAQIECBAgQIAAAQKC2g8QIECAAAECBAgQIECAAIEgIKgDmgkBAgQIECBAgAABAmb1CSEAAAEVSURBVAQIEBDUfoAAAQIECBAgQIAAAQIECAQBQR3QTAgQIECAAAECBAgQIECAgKD2AwQIECBAgAABAgQIECBAIAgI6oBmQoAAAQIECBAgQIAAAQIEBLUfIECAAAECBAgQIECAAAECQUBQBzQTAgQIECBAgAABAgQIECAgqP0AAQIECBAgQIAAAQIECBAIAoI6oJkQIECAAAECBAgQIECAAAFB7QcIECBAgAABAgQIECBAgEAQENQBzYQAAQIECBAgQIAAAQIECAhqP0CAAAECBAgQIECAAAECBIKAoA5oJgQIECBAgAABAgQIECBAQFD7AQIECBAgQIAAAQIECBAgEAQEdUAzIUCAAAECBAgQIECAAAECB1asAbne2906AAAAAElFTkSuQmCC') {
			form_data.append("b64img", $('#creativity-sketch').get(0).toDataURL());
		}
		$.ajax({
			url : '/creativity/post?f=json',
			type : 'POST',
			data: form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				$('#upload-hint').fadeIn(500, function() {
					setTimeout(function() {
						location.reload();
					}, 1500);
				});
			}
		});
	}
})
