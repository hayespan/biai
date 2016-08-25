$(document).ready(function() {
	var bannerSwiper = new Swiper('.banner-block .swiper-container', {
		prevButton:'.swiper-button-prev',
		nextButton:'.swiper-button-next',
		autoplay: 5000,
		loop: true,
	});

	var videoSwiper = new Swiper('.video-menu .swiper-container', {
		direction: 'vertical',
        slidesPerView: 3,
        spaceBetween: 12,
		autoplay: 5000
	});
})

