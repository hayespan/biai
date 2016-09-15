$(document).ready(function() {

	$('.modify-btn').on('click', function() {
		$('.setting-display').addClass('hidden');
		$('.setting-modify').removeClass('hidden');
	});

	$('.cancel-btn').on('click', function() {
		$('.setting-form')[0].reset();
		$('.setting-modify').addClass('hidden');
		$('.setting-display').removeClass('hidden');
	});

	$('.setting-modify form').on('submit', function(e) {
		e.preventDefault();
		var form_data = new FormData();
		if (!checkForm(form_data)) {
			return false;
		}
		console.log(form_data);
		$.ajax({
			url : '/admin/setting?f=json',
			type : 'POST',
			data : form_data,
		    processData: false,
		    contentType: false,
			success : function(result) {
				location.reload();
			}
		});
	});

	function checkForm(form_data) {
		if ($('#site_name').val() == '') {
			$('#site_name').siblings('.alert-hint').text('网站名字不能为空噢');
			$('#site_name').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('site_name', $('#site_name').val());
		}
		if ($('#site_domain').val() == '') {
			$('#site_domain').siblings('.alert-hint').text('网站域名不能为空噢');
			$('#site_domain').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('site_domain', $('#site_domain').val());
		}
		if ($('#site_filing_num').val() == '') {
			$('#site_filing_num').siblings('.alert-hint').text('网站备案号不能为空噢');
			$('#site_filing_num').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('site_filing_num', $('#site_filing_num').val());
		}
		if ($('#site_locale').val() == '') {
			$('#site_locale').siblings('.alert-hint').text('网站站点不能为空噢');
			$('#site_locale').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('site_locale', $('#site_locale').val());
		}
		if ($('#company_name').val() == '') {
			$('#company_name').siblings('.alert-hint').text('公司全称不能为空噢');
			$('#company_name').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('company_name', $('#company_name').val());
		}
		if ($('#service_phone').val() == '') {
			$('#service_phone').siblings('.alert-hint').text('公司全称不能为空噢');
			$('#service_phone').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('service_phone', $('#service_phone').val());
		}
		if ($('#company_location').val() == '') {
			$('#company_location').siblings('.alert-hint').text('公司地址不能为空噢');
			$('#company_location').siblings('.alert-hint').removeClass('hidden');
			return false;
		} else {
			form_data.append('company_location', $('#company_location').val());
		}
		return true;
	}
});
