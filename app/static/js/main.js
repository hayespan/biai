$(document).ready(function() {
	var bannerSwiper = new Swiper('.banner-block .swiper-container', {
		prevButton:'.banner-block .swiper-button-prev',
		nextButton:'.banner-block .swiper-button-next',
		autoplay: 5000,
		loop: true,
	});

	var videoSwiper = new Swiper('.video-menu .swiper-container', {
		direction: 'vertical',
		prevButton:'.video-menu .swiper-button-prev',
		nextButton:'.video-menu .swiper-button-next',
        slidesPerView: 3,
        spaceBetween: 12
	});
})

