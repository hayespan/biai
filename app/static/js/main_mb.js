$(document).ready(function() {
	var bannerSwiper = new Swiper('.banner-block .swiper-container', {
		autoplay: 5000,
		loop: true
	});

	var videoSwiper = new Swiper('.video-content .swiper-container', {
		prevButton:'.swiper-controller .button-prev',
		nextButton:'.swiper-controller .button-next',
		// effect : 'fade',
  //       slidesPerView: 1.1,
  //       spaceBetween: 12
	});

	var productSwiper = new Swiper('.img-info .swiper-container', {
		autoplay: 5000,
		loop: true,
		pagination : '.swiper-pagination'
	});
})

