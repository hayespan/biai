$(document).ready(function() {
	var bannerSwiper = new Swiper('.banner-block .swiper-container', {
		autoplay: 5000,
		loop: true,
	});

	$('.nav-button').on('click', function() {
		$('.header-nav').toggleClass('hidden');
	});
})

