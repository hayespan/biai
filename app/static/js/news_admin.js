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

	var news_content = $('.news-content-hidden').html();

	$('.modify-btn').on('click', function() {
		ue.setContent(news_content);
		$('.news-display').addClass('hidden');
		$('.news-modify').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$('.news-form')[0].reset();
		$('.news-modify').addClass('hidden');
		$('.news-display').removeClass('hidden');
	});

	$('.news-modify form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		$.ajax({
			url : '/admin/news/update?f=json',
			type : 'POST',
			data : {
				data : form_data
			},
		    processData: false,
		    contentType: false,
			success : function(result) {
				console.log(result);
				$('.news-form')[0].reset();
				$('.news-modify').addClass('hidden');
				$('.news-display').removeClass('hidden');
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
