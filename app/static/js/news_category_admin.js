$(document).ready(function() {
	$('.modify-btn').on('click', function() {
		$('.news-category-display').addClass('hidden');
		$('.news-category-modify').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$('.news-category-form')[0].reset();
		$('.news-category-modify').addClass('hidden');
		$('.news-category-display').removeClass('hidden');
	});

	$('.news-category-modify form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		form_data.append('id', this.dataset.id);
		$.ajax({
			url : '/admin/news_category/update?f=json',
			type : 'POST',
			data : {
				data : form_data
			},
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				$('.news-category-form')[0].reset();
				$('.news-category-modify').addClass('hidden');
				$('.news-category-display').removeClass('hidden');
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
