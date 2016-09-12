$(document).ready(function() {
	$('.add-btn').on('click', function() {
		var new_item = $('.subnav-list').children().first().clone(true);
		$('.subnav-list').append(new_item);
		new_item.fadeIn();
	});

	$('.delete-btn').on('click', function() {
		var that = $(this);
		var id = this.dataset.id;
		$.ajax({
			url : '/admin/nav/subnav/delete?f=json',
			type : 'POST',
			data : {
				id : id
			},
			success : function(result) {
				console.log(result);
				that.parents('.subnav-item').fadeOut('slow', function() {
					this.remove();
				});
			}
		});
	});


	$('.submit-btn').on('click', function() {
		$(this).parents('.subnav-item').find('.item-display').addClass('hidden');
		$(this).parents('.subnav-item').find('.item-input').removeClass('hidden');
		$(this).siblings('.delete-btn').addClass('hidden');
		$(this).addClass('hidden');
		$(this).siblings('.submit-btn').removeClass('hidden');
		$(this).siblings('.cancel-btn').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$(this).parents('.subnav-item').fadeOut('slow', function() {
			this.remove();
		});
	});

	$('.submit-btn').on('click', function() {
		var that = $(this);
		var nav_id = this.dataset.navid;
		var title = $(this).parents('.subnav-item').find('.title').val();
		var link = $(this).parents('.subnav-item').find('.link').val();
		$.ajax({
			url : '/admin/nav/subnav/create?f=json',
			type : 'POST',
			data : {
				nav_id : nav_id,
				title : title,
				link : link
			},
			success : function(result) {
				console.log(result);
				that.parents('.subnav-item').find('.subnav-title span').text(title);
				that.parents('.subnav-item').find('.subnav-link span').text(link);
				that.addClass('hidden');
				that.siblings('.cancel-btn').addClass('hidden');
				that.siblings('.delete-btn').attr('data-id', result.data.id);
				that.siblings('.delete-btn').removeClass('hidden');
				that.parents('.subnav-item').find('.item-input').addClass('hidden');
				that.parents('.subnav-item').find('.item-display').removeClass('hidden');
			}
		});
	});
});
