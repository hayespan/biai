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
	var news_content = $('.news-content').html();

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
		form_data.append('id', this.dataset.id);
		console.log(form_data);
		$.ajax({
			url : '/admin/news/update?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				location.reload();
				// $('.news-display h1').text($('#title').val());
				// $('.news-display h2').text($('#news_category_id').find("option:selected").text());
				// $('.news-content').html(ue.getContent());
				// $('.news-form')[0].reset();
				// $('.news-modify').addClass('hidden');
				// $('.news-display').removeClass('hidden');
			}
		});
	});

	function initForm() {
		$.ajax({
			url : '/admin/news_category_json?f=json',
			type : 'GET',
			success : function(result) {
				var category_list = result.data.news_category_list;
				for (var i = 0; i < category_list.length; i++) {
					var new_option = document.createElement("option");
					$(new_option).attr('value', category_list[i].id);
					$(new_option).text(category_list[i].name);
					$('#news_category_id').append(new_option);
				}
				$('#news_category_id').val($('#news_category_id')[0].dataset.choice);
			}
		});
	}

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
});
