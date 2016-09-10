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
		$('.news-list-display').addClass('hidden');
		$('.news-add').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$('.news-form')[0].reset();
		$('.news-add').addClass('hidden');
		$('.news-list-display').removeClass('hidden');
	});

	$('.delete-btn').on('click', function() {
		var target_item = $(this).parent().parent();
		var target_id = this.dataset.id;
		$.ajax({
			url : '/admin/news/delete?f=json',
			type : 'POST',
			data : {
				id : target_id
			},
			success : function(result) {
				target_item.fadeOut();
			}
		});
	});

	$('.news-add form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		$.ajax({
			url : '/admin/news/create?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				refreshCategory(result.data.id, $('#title').val());
				$('.news-form')[0].reset();
				$('.news-add').addClass('hidden');
				$('.news-list-display').removeClass('hidden');
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
		if ($('#news_category_id').val() == '') {
			$('#news_category_id').siblings('.alert-hint').text('新闻分类不能为空噢');
			$('#news_category_id').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('news_category_id', $('#news_category_id').val());
		}
		var content = ue.getContent();
		if (content == '') {
			return false;
		} else {
			form_data.append('content', content);
		}
		return true;
	}

	function refreshCategory(id, title) {
		var new_item = $('.news-list').children().first().clone(true);
		new_item.children().first().attr('href', '/admin/news/'+id);
		new_item.children().first().text(title);
		new_item.find('.delete-btn').attr('data-id', id);
		$('.news-list').append(new_item);
	}
});
