$(document).ready(function() {
	initForm();

	$('.add-btn').on('click', function() {
		var new_item = $('.information-list').children().first().clone(true);
		new_item.find('.information-img img').addClass('preview');
		$('.information-list').append(new_item);
		new_item.fadeIn();
		$(this).attr('disabled', 'disabled');
	});

	$('.delete-btn').on('click', function() {
		var that = $(this);
		var id = this.dataset.id;
		$.ajax({
			url : '/admin/information/delete?f=json',
			type : 'POST',
			data : {
				id : id
			},
			success : function(result) {
				console.log(result);
				that.parents('.information-item').fadeOut('slow', function() {
					this.remove();
				});
			}
		});
	});

	$('.cancel-btn').on('click', function() {
		$(this).parents('.information-item').fadeOut('slow', function() {
			this.remove();
		});
		$('.add-btn').removeAttr('disabled');
	});

	function initForm() {
		$.ajax({
			url : '/admin/news_json?f=json',
			type : 'GET',
			success : function(result) {
				var news_list = result.data.news_list;
				for (var i = 0; i < news_list.length; i++) {
					var new_option = document.createElement("option");
					$(new_option).attr('value', news_list[i].id);
					$(new_option).text(news_list[i].title);
					$('.news_id').append(new_option);
				}
			}
		});
	}

	$('.submit-btn').on('click', function() {
		var that = $(this);
		var title = $(this).parents('.information-item').find('.title').val();
		var weight = $(this).parents('.information-item').find('.weight').val();
		var news_id = $(this).parents('.information-item').find('.news_id').val();
		var form_data = new FormData();
		form_data.append('title', title);
		form_data.append('weight', weight);
		form_data.append('news_id', news_id);
		$.ajax({
			url : '/admin/information/create?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				that.parents('.information-item').find('.information-title span').text(title);
				that.parents('.information-item').find('.information-weight span').text(weight);
				that.parents('.information-item').find('.information-news span').text(news_id);
				that.addClass('hidden');
				that.siblings('.cancel-btn').addClass('hidden');
				that.siblings('.delete-btn').attr('data-id', result.data.id);
				that.siblings('.delete-btn').removeClass('hidden');
				that.parents('.information-item').find('.item-input').addClass('hidden');
				that.parents('.information-item').find('.item-display').removeClass('hidden');
				$('.add-btn').removeAttr('disabled');
			}
		});
	});
});
