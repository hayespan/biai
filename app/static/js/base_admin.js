$(document).ready(function() {
	switch ($('title').text()) {
		case '新闻分类管理':
			$('.sidebar .news-category').addClass('active');
			break;
		case '新闻条目管理':
			$('.sidebar .news').addClass('active');
			break;
		case '产品分类管理':
			$('.sidebar .product-category').addClass('active');
			break;
		case '产品条目管理':
			$('.sidebar .product').addClass('active');
			break;
		case '导航栏管理':
			$('.sidebar .nav').addClass('active');
			break;
	}
	$('.user-button').on('click', function(e) {
		e.preventDefault();
		$('.user-controller').toggleClass('hidden');
	});
});
