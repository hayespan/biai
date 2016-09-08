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
		// var target_id = parseInt(this.dataset.id);
		console.log(target_id);
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
			}
		});
	});

	$('.product-add form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		$.ajax({
			url : '/admin/product/create?f=json',
			type : 'POST',
			data : form_data,
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
		if ($('#title').val() == '') {
			$('#title').siblings('.alert-hint').text('新闻标题不能为空噢');
			$('#title').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('title', $('#title').val());
		}
		if ($('#cat').val() == '') {
			$('#name').siblings('.alert-hint').text('新闻分类不能为空噢');
			$('#name').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('name', $('#name').val());
		}
		var content = ue.getContent();
		if (content == '') {
			return false;
		} else {
			form_data.append('content', content);
		}
		return true;
	}
});
