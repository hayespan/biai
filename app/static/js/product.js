$(document).ready(function() {
	var big_pic = $('.big');
	$('.small').on('click', function() {
		var src = $(this).attr('src');
		big_pic.attr('src', src);
	});
});