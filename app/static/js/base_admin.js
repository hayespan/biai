$(document).ready(function() {
	switch ($('title').text()) {
		case '管理员列表':
			$('.sidebar .admin').addClass('active');
			break;
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
		case '首页轮播管理':
			$('.sidebar .banner').addClass('active');
			break;
		case '视频管理':
			$('.sidebar .video').addClass('active');
			break;
		case '首页资讯管理':
			$('.sidebar .information').addClass('active');
			break;
		case '创意中心管理':
			$('.sidebar .creativity').addClass('active');
			break;
		case '联系我们管理':
			$('.sidebar .contact').addClass('active');
			break;
		case '合作加盟管理':
			$('.sidebar .cooperation').addClass('active');
			break;
		case '人才招聘管理':
			$('.sidebar .join_us').addClass('active');
			break;
		case '关于我们管理':
			$('.sidebar .about').addClass('active');
			break;
		case '网站信息管理':
			$('.sidebar .setting').addClass('active');
			break;
	}
	$('.user-button').on('click', function(e) {
		e.preventDefault();
		$('.user-controller').toggleClass('hidden');
	});
});
