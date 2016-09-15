$(document).ready(function() {
	$('.delete-btn').on('click', function() {
		var that = $(this);
		var id = this.dataset.id;
		$.ajax({
			url : '/admin/cooperation/delete?f=json',
			type : 'POST',
			data : {
				id : id
			},
			success : function(result) {
				console.log(result);
				that.parents('.cooperation-item').fadeOut('slow', function() {
					this.remove();
				});
			}
		});
	});
});