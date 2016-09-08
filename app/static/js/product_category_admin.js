$(document).ready(function() {
	$('.modify-btn').on('click', function() {
		$('.product-category-display').addClass('hidden');
		$('.product-category-modify').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$('.product-category-form')[0].reset();
		$('.product-category-modify').addClass('hidden');
		$('.product-category-display').removeClass('hidden');
	});

	$("input[type='image']").on('click', function(e) {
		e.preventDefault();
		$(this).siblings('#file_select').click();
	});

	$('#file_select').on('change', function() {
		var form_data = new FormData();
		form_data.append('pic', $(this)[0].files[0]);
		console.log(form_data.get('pic'));
		$.ajax({
			url : '/admin/product/upload?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				if (result.data.file_id) {
					console.log(result.data.file_id);
					// $('#file_id').val(result.file_id);
					// $("input[type='image']").attr('src', result.file_id);
				} else {
					console.log(result);
				}
			}
		});
	});

	$('.product-category-modify form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		form_data.append('id', this.dataset.id);
		$.ajax({
			url : '/admin/product_category/update?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
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
		return true;
	}
});
