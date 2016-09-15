$(document).ready(function() {
	// var img = $('.about-text img');
	// var ratio = 3/10;
	// for (var i = 0; i < img.length; i++) {
	// 	var width = Math.floor(img[i].offsetWidth*ratio);
	// 	var height = Math.floor(img[i].offsetHeight*ratio);
	// 	img[i].style.width = width+'px';
	// 	img[i].style.height = height+'px';
	// 	console.log(width);
	// 	console.log(height);
	// }
	var img = $('.about-content img');
	var ratio = 3/10;
	for (var i = 0; i < img.length; i++) {
		var width = img[i].offsetWidth;
		var height = img[i].offsetHeight;
		var maxWidth = $('.about-content')[0].offsetWidth;
		var img_ratio = height/width;
		img[i].style.maxWidth = maxWidth+'px';
		img[i].style.height = Math.floor(img[i].offsetWidth*img_ratio)+'px';
	}
});