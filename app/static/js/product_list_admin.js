$(document).ready(function() {
	var ue = UE.getEditor('editor', {
	    serverUrl: "/upload/",
		toolbars: [[
		            'fullscreen', 'source', '|', 'undo', 'redo', '|',
		            'bold', 'italic', 'underline', 'fontborder', 'strikethrough', 'superscript', 'subscript', 'removeformat', '|', 'forecolor', 'backcolor', 'insertorderedlist', 'insertunorderedlist', 'selectall', 'cleardoc', '|',
		            'rowspacingtop', 'rowspacingbottom', 'lineheight', '|',
		            'customstyle', 'paragraph', 'fontfamily', 'fontsize', '|',
		            'directionalityltr', 'directionalityrtl', 'indent', '|',
		            'justifyleft', 'justifycenter', 'justifyright', 'justifyjustify', '|', 'touppercase', 'tolowercase', '|',
		            'link', 'unlink', 'anchor', '|', 'imagenone', 'imageleft', 'imageright', 'imagecenter', '|',
		            'simpleupload', 'insertimage', 'emotion', 'insertvideo', 'music', 'attachment', 'map', 'gmap', 'insertframe', 'insertcode', 'pagebreak', 'template', 'background', '|',
		            'horizontal', 'date', 'time', '|',
		            'inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols', 'charts'
		]],
		initialFrameWidth: 760,
		initialFrameHeight: 300,
		minFrameHeight: 300,
		autoHeightEnabled: false
	});

	initForm();

	$('.add-btn').on('click', function() {
		$('.product-list-display').addClass('hidden');
		$('.product-add').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$('.product-form')[0].reset();
		$('.product-add').addClass('hidden');
		$('.product-list-display').removeClass('hidden');
	});

	$('.delete-btn').on('click', function() {
		var target_item = $(this).parent().parent();
		var target_id = this.dataset.id;
		$.ajax({
			url : '/admin/product/delete?f=json',
			type : 'POST',
			data : {
				id : target_id
			},
			success : function(result) {
				console.log(result);
				target_item.fadeOut('slow', function() {
					this.remove();
				});
			}
		});
	});

	$('.add-category').on('click', function(e) {
		e.preventDefault();
		var new_category = $(this).siblings('.category-block').children().first().clone(true).hide();
		new_category.val('');
		$(this).siblings('.category-block').append(new_category);
		new_category.fadeIn();
	});

	$('.delete-category').on('click', function(e) {
		e.preventDefault();
		if ($(this).siblings('.category-block').children().length > 1) {
			$(this).siblings('.category-block').children().last().fadeOut('slow', function() {
				this.remove();
			});
		} else {
			return false;
		}
	});

	$('.add-attr').on('click', function(e) {
		e.preventDefault();
		var new_attr = $(this).siblings('.attr-block').children().first().clone(true).hide();
		new_attr.find('.attr-name').val('');
		new_attr.find('.attr-value').val('');
		$(this).siblings('.attr-block').append(new_attr);
		new_attr.fadeIn();
	});

	$('.delete-attr').on('click', function(e) {
		e.preventDefault();
		if ($(this).siblings('.attr-block').children().length > $(this).siblings('.attr-block')[0].dataset.min) {
			$(this).siblings('.attr-block').children().last().fadeOut('slow', function() {
				this.remove();
			});
		} else {
			return false;
		}
	});

	$('.add-img').on('click', function(e) {
		e.preventDefault();
		$(this).siblings('.file-select').click();
	});

	$('.delete-img').on('click', function(e) {
		e.preventDefault();
		$(this).parent().fadeOut('slow', function() {
			this.remove();
		});
	})

	$('.change-img').on('click', function(e) {
		e.preventDefault();
		$(this).siblings('.file_change').click();
	})

	$('.file_change').on('change', function() {
		var form_data = new FormData();
		var that = $(this);
		form_data.append('pic', this.files[0]);
		$.ajax({
			url : '/admin/product/upload?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				that.siblings('img').attr('src', '/static/'+result.data.file_path);
				that.siblings('.file_id').attr('value', result.data.file_id);
				console.log(that.siblings('img'));
				console.log(that.siblings('.file_id'));
			}
		});
	});

	$('.file-select').on('change', function() {
		var new_img = $('#product_img').children().first().clone(true);
		var form_data = new FormData();
		form_data.append('pic', this.files[0]);
		$.ajax({
			url : '/admin/product/upload?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				new_img.find('img').attr('src', '/static/'+result.data.file_path);
				new_img.find('.file_id').attr('value', result.data.file_id);
				$('#product_img').append(new_img);
				new_img.show();
			}
		});
	});

	$('.product-add form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		console.log(form_data);
		$.ajax({
			url : '/admin/product/create?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				refreshCategory(result.data.id, $('#name').val());
				$('.product-form')[0].reset();
				$('.product-add').addClass('hidden');
				$('.product-list-display').removeClass('hidden');
			}
		});
	});

	function initForm() {
		$.ajax({
			url : '/admin/product_category_json?f=json',
			type : 'GET',
			success : function(result) {
				var category_list = result.data.product_category_list;
				for (var i = 0; i < category_list.length; i++) {
					var new_option = document.createElement("option");
					$(new_option).attr('value', category_list[i].id);
					$(new_option).text(category_list[i].name);
					$('.product_category_id').append(new_option);
				}
			}
		});
	}

	function checkForm(form_data) {
		if ($('#name').val() == '') {
			$('#name').siblings('.alert-hint').text('产品名字不能为空噢');
			$('#name').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('name', $('#name').val());
		}
		if ($('#buy_link').val() == '') {
			$('#buy_link').siblings('.alert-hint').text('购买链接不能为空噢');
			$('#buy_link').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('buy_link', $('#buy_link').val());
		}
		var category_id = [];
		var category_ids = $('.product_category_id');
		for (var i = 0; i < category_ids.length; i++) {
			if (category_ids[i].value) {
				category_id.push(category_ids[i].value);
			}
		}
		form_data.append('category_ids', JSON.stringify(category_id));
		var attr_item_name = $('#attrs_ .attr-name');
		var attr_item_value = $('#attrs_ .attr-value');
		var attrs = new Object();
		for (var i = 0; i < attr_item_name.length; i++) {
			if (attr_item_name[i].value) {
				attrs[attr_item_name[i].value] = attr_item_value[i].value;
			}
		}
		form_data.append('attrs', JSON.stringify(attrs));
		var oth_attr_item_name = $('#oth_attrs_ .attr-name');
		var oth_attr_item_value = $('#oth_attrs_ .attr-value');
		var oth_attrs = new Object();
		for (var i = 0; i < oth_attr_item_name.length; i++) {
			if (oth_attr_item_name[i].value) {
				oth_attrs[oth_attr_item_name[i].value] = oth_attr_item_value[i].value;
			}
		}
		form_data.append('oth_attrs', JSON.stringify(oth_attrs));
		var file_id = [];
		var file_ids = $('.file_id');
		for (var i = 0; i < file_ids.length; i++) {
			if (file_ids[i].value) {
				file_id.push(file_ids[i].value);
			}
		}
		form_data.append('file_ids', JSON.stringify(file_id));
		var description = ue.getContent();
		if (description == '') {
			return false;
		} else {
			form_data.append('description', description);
		}
		return true;
	}

	function refreshCategory(id, name) {
		var new_item = $('.product-list').children().first().clone(true);
		new_item.children().first().attr('href', '/admin/product/'+id);
		new_item.children().first().text(name);
		new_item.find('.delete-btn').attr('data-id', id);
		$('.product-list').append(new_item);
		new_item.show();
	}
});
