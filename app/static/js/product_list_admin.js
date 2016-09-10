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
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				target_item.fadeOut();
				target_item.remove();
			}
		});
	});

	$('.add-attr').on('click', function(e) {
		e.preventDefault();
		var new_attr = $(this).siblings('.attr-block').children().first().clone(true).hide();
		new_attr.find('.attr-name').val('');
		new_attr.find('.attr-value').val('');
		$(this).siblings('.attr-block').append(new_attr);
		new_attr.fadeIn();
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
				// $('.product-category-form')[0].reset();
				// $('.product-category-add').addClass('hidden');
				// $('.product-category-display').removeClass('hidden');
			}
		});
	});

	function checkForm(form_data) {
		if ($('#name').val() == '') {
			$('#name').siblings('.alert-hint').text('产品名字不能为空噢');
			$('#name').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('name', $('#name').val());
		}
		var category_ids = [];
		if ($('#product_category_id').val() == '') {
			$('#product_category_id').siblings('.alert-hint').text('产品分类不能为空噢');
			$('#product_category_id').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			category_ids.push($('#product_category_id').val());
		}
		form_data.append('category_ids', JSON.stringify(category_ids));
		var attr_item_name = $('#attrs_ .attr-name');
		var attr_item_value = $('#attrs_ .attr-value');
		var attrs = new Object();
		for (var i = 0; i < attr_item_name.length; i++) {
			if (attr_item_name[i].value) {
				attrs[attr_item_name[i].value] = attr_item_value[i].value;
			}
		}
		form_data.append('attrs_', JSON.stringify(attrs));
		var oth_attr_item_name = $('#oth_attrs_ .attr-name');
		var oth_attr_item_value = $('#oth_attrs_ .attr-value');
		var oth_attrs = new Object();
		for (var i = 0; i < oth_attr_item_name.length; i++) {
			if (oth_attr_item_name[i].value) {
				oth_attrs[oth_attr_item_name[i].value] = oth_attr_item_value[i].value;
			}
		}
		form_data.append('oth_attrs_', JSON.stringify(oth_attrs));
		var file_id = [];
		var file_ids = $('.file_id');
		for (var i = 0; i < file_ids.length; i++) {
			if (file_ids[i].value) {
				file_id.push(file_ids[i].value);
			}
		}
		form_data.append('file_ids', JSON.stringify(file_id));
		var content = ue.getContent();
		if (content == '') {
			return false;
		} else {
			form_data.append('content', content);
		}
		return true;
	}

	function json_to_string(data) {
		var json_string = '';
		return json_string;
	}
});
