$(document).ready(function() {
	var cooperatePage = $('.join-cooperate');
	var recruitPage = $('.join-recruit');
	var cooperate = $('.cooperate');
	var recruit = $('.recruit');
	console.log(cooperate);
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
});