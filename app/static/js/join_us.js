$(document).ready(function() {
	var cooperatePage = $('.join-cooperate');
	var recruitPage = $('.join-recruit');
	var cooperate = $('.cooperate');
	var recruit = $('.recruit');

	cooperate.on('click', function(e) {
		e.preventDefault();
		$(this).addClass('chosen')
		recruit.removeClass('chosen');
		cooperatePage.removeClass('hidden');
		recruitPage.addClass('hidden');
	});
	recruit.on('click', function(e) {
		e.preventDefault();
		$(this).addClass('chosen')
		cooperate.removeClass('chosen');
		recruitPage.removeClass('hidden');
		cooperatePage.addClass('hidden');
	});

	$('.form-item input[type=text]').on('click', function() {
		$(this).siblings('.alert-hint').addClass('hidden');
	});

	$('.form-item textarea').on('click', function() {
		$(this).siblings('.alert-hint').addClass('hidden');
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

	$('form').on('submit', function(e) {
		e.preventDefault();
		var valid_code = $('#valid-code').val();
		$.ajax({
			url : '/captcha/mobile_check?f=json',
			type : 'POST',
			data : {
				code : valid_code
			},
			success : function(result) {
				if (result.data.correct) {
					submit_info();
				} else {
					// submit_info();
					$('#verify-code').siblings('.alert-hint').text('验证码有误请重试');
					$('#verify-code').siblings('.alert-hint').removeClass('hidden');
				}
			}
		});
	});

	function submit_info() {
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		console.log(form_data);
		$.ajax({
			url : '/join_us/cooperation/post?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				if (result.data.msg== "captcha code error") {
					$('#valid-code').siblings('.alert-hint').text('验证码错误');
					$('#valid-code').siblings('.alert-hint').removeClass('hidden');
				} else {
					location.reload();
				}
			}
		});
	}

	function checkForm(form_data) {
		if ($('#name').val() == '') {
			$('#name').siblings('.alert-hint').text('姓名不能为空噢');
			$('#name').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('name', $('#name').val());
		}
		if ($('#contact').val() == '') {
			$('#contact').siblings('.alert-hint').text('联系方式不能为空噢');
			$('#contact').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('contact', $('#contact').val());
		}
		if ($('#zone').val() == '') {
			$('#zone').siblings('.alert-hint').text('地区不能为空噢');
			$('#zone').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('zone', $('#zone').val());
		}
		if ($('#shop_range').val() == '') {
			$('#shop_range').siblings('.alert-hint').text('店铺主管不能为空噢');
			$('#shop_range').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('shop_range', $('#shop_range').val());
		}
		if ($('#develop_plan').val() == '') {
			$('#develop_plan').siblings('.alert-hint').text('发展规划不能为空噢');
			$('#develop_plan').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('develop_plan', $('#develop_plan').val());
		}
		if ($('#cooperation_intention').val() == '') {
			$('#cooperation_intention').siblings('.alert-hint').text('合作意向不能为空噢');
			$('#cooperation_intention').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('cooperation_intention', $('#cooperation_intention').val());
		}
		if ($('#mobile').val() == '') {
			$('#mobile').siblings('.alert-hint').text('手机号码不能为空噢');
			$('#mobile').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('mobile', $('#mobile').val());
		}
		if ($('#valid-code').val() == '') {
			$('#valid-code').siblings('.alert-hint').text('请输入验证码');
			$('#valid-code').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('code', $('#valid-code').val());
		}
		return true;
	}
});