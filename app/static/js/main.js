$(document).ready(function() {
	$('.banner-block .swiper-container').css('height', window.innerWidth/2.5+'px');
	var bannerSwiper = new Swiper('.banner-block .swiper-container', {
		autoplay: 5000,
		loop: true,
	});

	$('.banner-block .swiper-button-prev').on('click', function(e){
		bannerSwiper.swipePrev();
	})
	$('.banner-block .swiper-button-next').on('click', function(e){
		bannerSwiper.swipeNext();
	})


	var videoSwiper = new Swiper('.video-menu .swiper-container', {
		mode: 'vertical',
        slidesPerView: 3,
        spaceBetween: 12
	});

	$('.video-menu .swiper-button-prev').on('click', function(e){
		videoSwiper.swipePrev();
	})
	$('.video-menu .swiper-button-next').on('click', function(e){
		videoSwiper.swipeNext();
	})

	$('.video-menu input').on('click', function() {
		$('.video-content video').attr('src', '/static/video/mainpage/'+this.dataset.video);
	});
});

