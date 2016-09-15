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
		initialFrameWidth: 840,
		initialFrameHeight: 500,
		minFrameHeight: 300,
		autoHeightEnabled: false
	});

	var join_content = $('.join-content').html();

	$('.modify-btn').on('click', function() {
		ue.setContent(join_content);
		$('.join-display').addClass('hidden');
		$('.join-modify').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$('.join-modify').addClass('hidden');
		$('.join-display').removeClass('hidden');
	});

	$('.submit-btn').on('click', function(e) {
		e.preventDefault();
		var id = this.dataset.id;
		var content = ue.getContent();
		$.ajax({
			url : '/admin/join_us/modify?f=json',
			type : 'POST',
			data : {
				id : id,
				content : content
			},
			success : function(result) {
				location.reload();
			}
		});
	});
});