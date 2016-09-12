$(document).ready(function() {
	$('.modify-btn').on('click', function() {
		$(this).parents('.subnav-item').find('.item-display').addClass('hidden');
		$(this).parents('.subnav-item').find('.item-input').removeClass('hidden');
		$(this).siblings('.delete-btn').addClass('hidden');
		$(this).addClass('hidden');
		$(this).siblings('.submit-btn').removeClass('hidden');
		$(this).siblings('.cancel-btn').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$(this).parents('.subnav-item').find('.item-display').removeClass('hidden');
		$(this).parents('.subnav-item').find('.item-input').addClass('hidden');
		$(this).siblings('.delete-btn').removeClass('hidden');
		$(this).siblings('.modify-btn').removeClass('hidden');
		$(this).addClass('hidden');
		$(this).siblings('.submit-btn').addClass('hidden');
	});

	$('.submit-btn').on('click', function() {
		var that = $(this);
		var id = this.dataset.id;
		var new_title = $(this).parents('.subnav-item').find('.title').val();
		var new_link = $(this).parents('.subnav-item').find('.link').val();
		$.ajax({
			url : '/admin/subnav/modify?f=json',
			type : 'POST',
			data : {
				id : id,
				title : new_title,
				link : new_link
			},
			success : function(result) {
				that.parents('.subnav-item').find('.subnav-title span').text(new_title);
				that.parents('.subnav-item').find('.subnav-link span').text(new_link);
				that.siblings('.cancel-btn').click();
				console.log(result);
			}
		});
	})
});
