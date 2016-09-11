$(document).ready(function() {
	var img_reader = new FileReader();

	img_reader.onload = function (e) {
		$(".img-block img").attr('src', e.target.result);
	};

	$('.modify-btn').on('click', function() {
		$('.product-category-display').addClass('hidden');
		$('.product-category-modify').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$('.product-category-form')[0].reset();
		$('.product-category-modify').addClass('hidden');
		$('.product-category-display').removeClass('hidden');
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

	$('.product-category-modify form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		form_data.append('id', this.dataset.id);
		console.log(form_data);
		$.ajax({
			url : '/admin/product_category/update?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				$('.category-name').text($('#name').val());
				$('.category-weight').text($('#weight').val());
				$('.category-img').attr('src', $(".img-block img").attr('src'));
				$('.product-category-display h1').text($('#name').val());
				$('.product-category-form')[0].reset();
				$('.product-category-modify').addClass('hidden');
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
});
