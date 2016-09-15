$(document).ready(function() {
	var img = $('.news-content img');
	var ratio = 3/10;
	for (var i = 0; i < img.length; i++) {
		var width = img[i].offsetWidth;
		var height = img[i].offsetHeight;
		var maxWidth = $('.news-content')[0].offsetWidth;
		var img_ratio = height/width;
		img[i].style.maxWidth = maxWidth+'px';
		img[i].style.height = Math.floor(img[i].offsetWidth*img_ratio)+'px';
	}
});