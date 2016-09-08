$(document).ready(function() {
	$('.user-button').on('click', function(e) {
		e.preventDefault();
		$('.user-controller').toggleClass('hidden');
	});
});
