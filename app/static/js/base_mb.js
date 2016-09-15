$(document).ready(function() {
	$('.dropdown-btn').on('click', function() {
		// $(this).siblings('.dropdown').toggleClass('hidden');
		$(this).siblings('.dropdown').slideToggle();
	});

	$('.nav-button').on('click', function() {
		$('.header-nav').toggleClass('hidden');
	});
});
