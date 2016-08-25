$(document).ready(function() {
	var bannerSwiper = new Swiper('.banner-block .swiper-container', {
		autoplay: 5000,
		loop: true
	});

	var productSwiper = new Swiper('.img-info .swiper-container', {
		autoplay: 5000,
		loop: true,
		pagination : '.swiper-pagination'
	});

	$('.nav-button').on('click', function() {
		$('.header-nav').toggleClass('hidden');
	});

	var cooperatePage = $('.join-cooperate');
	var recruitPage = $('.join-recruit');
	var cooperate = $('.cooperate');
	var recruit = $('.recruit');
	cooperate.on('click', function(e) {
		e.preventDefault();
		$(this).addClass('chosen')
		recruit.removeClass('chosen');
		cooperatePage.removeClass('hidden');
		recruitPage.addClass('hidden');
	});
	recruit.on('click', function(e) {
		e.preventDefault();
		$(this).addClass('chosen')
		cooperate.removeClass('chosen');
		recruitPage.removeClass('hidden');
		cooperatePage.addClass('hidden');
	});
})

