$(document).ready(function(){
	$("#mainForm").validate({
		errorPlacement: function(error, element) {
			// Append error within linked label
			$( element ).closest( "li" ).find('h5').append( error );
			$('.error').html('required filed!');
		},
		errorElement: "span"
	});
	$.validator.setDefaults({
	    submitHandler: function(form) {
	      form.submit();	    
	  }
	});
});