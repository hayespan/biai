$(document).ready(function() {
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
		// var target_id = parseInt(this.dataset.id);
		console.log(target_id);
		$.ajax({
			url : '/admin/product_category/delete?f=json',
			type : 'POST',
			data : {
				'id' : target_id
			},
			success : function(result) {
				console.log(result);
				target_item.fadeOut();
			}
		});
	});

	$('.product-category-add form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		$.ajax({
			url : '/admin/product_category/create?f=json',
			type : 'POST',
			data : {
				data : form_data
			},
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				$('.product-category-form')[0].reset();
				$('.product-category-add').addClass('hidden');
				$('.product-category-display').removeClass('hidden');
			}
		});
	});

	function checkForm(form_data) {
		if ($('#name').val() == '') {
			$('#name').siblings('.alert-hint').text('产品名不能为空噢');
			$('#name').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('name', $('#name').val());
		}
		if ($('#weight').val() == '') {
			$('#weight').siblings('.alert-hint').text('产品权重不能为空噢');
			$('#weight').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('weight', $('#weight').val());
		}
		return true;
	}
});