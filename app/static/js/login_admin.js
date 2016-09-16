$(document).ready(function() {
	$('.login-form').on('submit', function(e) {
		
	});

	$('.login-form').on('submit', function(e) {
		e.preventDefault();
		// var form_data = new FormData();
		if (!checkForm()) {
			return false;
		}
		this.submit();
		// $.ajax({
		// 	url : '/admin/admin/create?f=json',
		// 	type : 'POST',
		// 	data : form_data,
		//     processData: false,
		//     contentType: false,
		// 	success : function(result) {
		// 		console.log(result);
		// 		that.parents('.admin-item').find('.admin-username span').text(username);
		// 		that.parents('.admin-item').find('.admin-password span').text(password);
		// 		that.parents('.admin-item').find('.admin-realname span').text(realname);
		// 		that.addClass('hidden');
		// 		that.siblings('.cancel-btn').addClass('hidden');
		// 		that.siblings('.delete-btn').attr('data-id', result.data.id);
		// 		that.siblings('.delete-btn').removeClass('hidden');
		// 		that.parents('.admin-item').find('.item-input').addClass('hidden');
		// 		that.parents('.admin-item').find('.item-display').removeClass('hidden');
		// 		$('.add-btn').removeAttr('disabled');
		// 	}
		// });
	});

	function checkForm(form_data) {
		if ($('#username').val() == '') {
			// $('#name').siblings('.alert-hint').text('姓名不能为空噢');
			// $('#name').siblings('.alert-hint').removeClass('hidden');
			alert('姓名不能为空噢');
			return false;
		} else {
			// form_data.append('username', $('#username').val());
		}
		if ($('#password').val() == '') {
			// $('#contact').siblings('.alert-hint').text('联系方式不能为空噢');
			// $('#contact').siblings('.alert-hint').removeClass('hidden');
			alert('密码不能为空噢');
			return false;
		} else {
			// form_data.append('password', $('#password').val());
		}
		return true;
	}
});
