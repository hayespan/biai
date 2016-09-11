$(document).ready(function() {
	$('.add-btn').on('click', function() {
		$('.news-category-display').addClass('hidden');
		$('.news-category-add').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$('.news-category-form')[0].reset();
		$('.news-category-add').addClass('hidden');
		$('.news-category-display').removeClass('hidden');
	});

	$('.delete-btn').on('click', function() {
		var target_item = $(this).parent().parent();
		var target_id = this.dataset.id;
		console.log(target_id);
		$.ajax({
			url : '/admin/news_category/delete?f=json',
			type : 'POST',
			data : {
				id : target_id
			},
			success : function(result) {
				target_item.fadeOut();
			}
		});
	});

	$('.news-category-add form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		$.ajax({
			url : '/admin/news_category/create?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				refreshCategory(result.data.id, $('#name').val());
				$('.news-category-form')[0].reset();
				$('.news-category-add').addClass('hidden');
				$('.news-category-display').removeClass('hidden');
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

	function refreshCategory(id, name) {
		var new_item = $('.category-list').children().first().clone(true);
		new_item.children().first().attr('href', '/admin/news_category/'+id);
		new_item.children().first().text(name);
		new_item.find('.delete-btn').attr('data-id', id);
		$('.category-list').append(new_item);
	}
});
