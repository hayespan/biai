$(document).ready(function() {
	var img_reader = new FileReader();

	img_reader.onload = function (e) {
		$(".preview").attr('src', e.target.result);
		$(".preview").removeClass('hidden');
	};

	$('.add-btn').on('click', function() {
		var new_item = $('.admin-list').children().first().clone(true);
		$('.admin-list').append(new_item);
		new_item.fadeIn();
		$(this).attr('disabled', 'disabled');
	});

	$('.delete-btn').on('click', function() {
		var that = $(this);
		var id = this.dataset.id;
		$.ajax({
			url : '/admin/admin/delete?f=json',
			type : 'POST',
			data : {
				id : id
			},
			success : function(result) {
				console.log(result);
				that.parents('.admin-item').fadeOut('slow', function() {
					this.remove();
				});
			}
		});
	});

	$('.cancel-btn').on('click', function() {
		$(this).parents('.admin-item').fadeOut('slow', function() {
			this.remove();
		});
		$('.add-btn').removeAttr('disabled');
	});

	$('.submit-btn').on('click', function() {
		var that = $(this);
		var username = $(this).parents('.admin-item').find('.username').val();
		var password = $(this).parents('.admin-item').find('.password').val();
		var realname = $(this).parents('.admin-item').find('.realname').val();
		var form_data = new FormData();
		form_data.append('username', username);
		form_data.append('password', password);
		form_data.append('real_name', realname);
		$.ajax({
			url : '/admin/admin/create?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				that.parents('.admin-item').find('.admin-username span').text(username);
				that.parents('.admin-item').find('.admin-password span').text(password);
				that.parents('.admin-item').find('.admin-realname span').text(realname);
				that.addClass('hidden');
				that.siblings('.cancel-btn').addClass('hidden');
				that.siblings('.delete-btn').attr('data-id', result.data.id);
				that.siblings('.delete-btn').removeClass('hidden');
				that.parents('.admin-item').find('.item-input').addClass('hidden');
				that.parents('.admin-item').find('.item-display').removeClass('hidden');
				$('.add-btn').removeAttr('disabled');
			}
		});
	});
});
