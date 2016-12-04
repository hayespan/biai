$(document).ready(function() {
	var img_reader = new FileReader();

	img_reader.onload = function (e) {
		$(".preview").attr('src', e.target.result);
		$(".preview").removeClass('hidden');
	};

	$('.add-btn').on('click', function() {
		var new_item = $('.video-list').children().first().clone(true);
		new_item.find('.video-img img').addClass('preview');
		$('.video-list').append(new_item);
		new_item.fadeIn();
		$(this).attr('disabled', 'disabled');
	});

	$('.delete-btn').on('click', function() {
		var that = $(this);
		var id = this.dataset.id;
		$.ajax({
			url : '/admin/video/delete?f=json',
			type : 'POST',
			data : {
				id : id
			},
			success : function(result) {
				console.log(result);
				that.parents('.video-item').fadeOut('slow', function() {
					this.remove();
				});
			}
		});
	});

	$('.pic').on('change', function() {
		img_reader.readAsDataURL($(this)[0].files[0]);
	});

	$('.cancel-btn').on('click', function() {
		$(this).parents('.video-item').fadeOut('slow', function() {
			this.remove();
		});
		$('.add-btn').removeAttr('disabled');
	});

	$('.submit-btn').on('click', function() {
		var that = $(this);
		var name = $(this).parents('.video-item').find('.name').val();
		var weight = $(this).parents('.video-item').find('.weight').val();
		var pic = $(this).parents('.video-item').find('.pic')[0].files[0];
		var video = $(this).parents('.video-item').find('.video')[0].files[0];
		var bar = $(this).parents('.video-item').find('.process-bar');
		var form_data = new FormData();
		form_data.append('name', name);
		form_data.append('weight', weight);
		form_data.append('pic', pic);
		form_data.append('video', video);
		$(this).parents('.video-item').find('.item-controller').hide();
		$(this).parents('.video-item').find('.process-bar-container').show();
		$.ajax({
			url : '/admin/video/create?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			xhr: function() {
				var xhr = $.ajaxSettings.xhr();
				xhr.upload.onprogress = function(evt) {
					var progress = evt.loaded/evt.total*100;
					bar.text(Math.floor(progress)+'%');
					bar.css('width', 135*progress/100+'px');
					// if (progress == 100) {
					// 	location.reload();
					// }
				};
				return xhr;
			},
			success : function(result) {
				location.reload();
			}
		});
	});
});
