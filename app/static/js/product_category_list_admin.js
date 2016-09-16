$(document).ready(function() {
	var img_reader = new FileReader();

	img_reader.onload = function (e) {
		$(".img-block img").attr('src', e.target.result);
	};

	$('.add-btn').on('click', function() {
		$('.product-category-display').addClass('hidden');
		$('.product-category-add').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$('.product-category-form')[0].reset();
		$('.product-category-add').addClass('hidden');
		$('.product-category-display').removeClass('hidden');
	});

	$('.delete-btn').on('click', function() {
		var target_item = $(this).parent().parent();
		var target_id = this.dataset.id;
		$.ajax({
			url : '/admin/product_category/delete?f=json',
			type : 'POST',
			data : {
				id : target_id
			},
			success : function(result) {
				console.log(result);
				target_item.fadeOut('slow', function() {
					this.remove();
				})
			}
		});
	});

	$(".img-block button").on('click', function(e) {
		e.preventDefault();
		$(this).siblings('#img').click();
	});

	$('#img').on('change', function() {
		img_reader.readAsDataURL($(this)[0].files[0]);
		// var form_data = new FormData();
		// form_data.append('pic', $(this)[0].files[0]);
		// console.log(form_data.get('pic'));
		// $.ajax({
		// 	url : '/admin/product/upload?f=json',
		// 	type : 'POST',
		// 	data : form_data,
		//     processData: false,
		//     contentType: false,
		// 	success : function(result) {
		// 		if (result.data.file_id) {
		// 			console.log(result.data.file_id);
		// 			$('#file_id').attr('value', result.data.file_id);
		// 			$(".img-block img").attr('src', '/static/'+result.data.file_path);
		// 		} else {
		// 			console.log(result);
		// 		}
		// 	}
		// });
	});

	$('.product-category-add form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		console.log(form_data);
		$.ajax({
			url : '/admin/product_category/create?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				refreshCategory(result.data.id, $('#name').val());
				$('.product-category-form')[0].reset();
				$('.product-category-add').addClass('hidden');
				$('.product-category-display').removeClass('hidden');
			}
		});
	});

	function checkForm(form_data) {
		if ($('#name').val() == '') {
			$('#name').siblings('.alert-hint').text('分类名不能为空噢');
			$('#name').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('name', $('#name').val());
		}
		if ($('#weight').val() == '') {
			$('#weight').siblings('.alert-hint').text('分类权重不能为空噢');
			$('#weight').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('weight', $('#weight').val());
		}
		if ($('#img').val() == '') {
			$('#img').siblings('.alert-hint').text('请选择分类图片');
			$('#img').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('img', $('#img')[0].files[0]);
		}
		return true;
	}

	function refreshCategory(id, name) {
		var new_item = $('.category-list').children().first().clone(true);
		new_item.children().first().attr('href', '/admin/product_category/'+id);
		new_item.children().first().text(name);
		new_item.find('.delete-btn').attr('data-id', id);
		$('.category-list').append(new_item);
		new_item.show();
	}
});
