$(document).ready(function() {
	var img_reader = new FileReader();

	img_reader.onload = function (e) {
		$(".preview").attr('src', e.target.result);
		$(".preview").removeClass('hidden');
	};

	$('.add-btn').on('click', function() {
		var new_item = $('.banner-list').children().first().clone(true);
		new_item.find('.banner-img img').addClass('preview');
		$('.banner-list').append(new_item);
		new_item.fadeIn();
		$(this).attr('disabled', 'disabled');
	});

	$('.delete-btn').on('click', function() {
		var that = $(this);
		var id = this.dataset.id;
		$.ajax({
			url : '/admin/banner/delete?f=json',
			type : 'POST',
			data : {
				id : id
			},
			success : function(result) {
				console.log(result);
				that.parents('.banner-item').fadeOut('slow', function() {
					this.remove();
				});
			}
		});
	});

	$('.pic').on('change', function() {
		img_reader.readAsDataURL($(this)[0].files[0]);
	});

	$('.cancel-btn').on('click', function() {
		$(this).parents('.banner-item').fadeOut('slow', function() {
			this.remove();
		});
		$('.add-btn').removeAttr('disabled');
	});

	$('.submit-btn').on('click', function() {
		var that = $(this);
		var name = $(this).parents('.banner-item').find('.name').val();
		var weight = $(this).parents('.banner-item').find('.weight').val();
		var pic = $(this).parents('.banner-item').find('.pic')[0].files[0];
		var form_data = new FormData();
		form_data.append('name', name);
		form_data.append('weight', weight);
		form_data.append('pic', pic);
		$.ajax({
			url : '/admin/banner/create?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				that.parents('.banner-item').find('.banner-name span').text(name);
				that.parents('.banner-item').find('.banner-weight span').text(weight);
				that.addClass('hidden');
				that.siblings('.cancel-btn').addClass('hidden');
				that.siblings('.delete-btn').attr('data-id', result.data.id);
				that.siblings('.delete-btn').removeClass('hidden');
				that.parents('.banner-item').find('.item-input').addClass('hidden');
				that.parents('.banner-item').find('.item-display').removeClass('hidden');
				$('.add-btn').removeAttr('disabled');
			}
		});
	});
});
