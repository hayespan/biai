$(document).ready(function() {
	$('.user-button').on('click', function(e) {
		e.preventDefault();
		$('.user-controller').toggleClass('hidden');
	});

	$('.add-btn').on('click', function() {
		$('.news-category-display').addClass('hidden');
		$('.news-category-add').removeClass('hidden');
	});
});
