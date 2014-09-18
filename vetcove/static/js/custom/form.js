 /*************************************************/
/* Custom Built Form Validator For All Forms *****/
/*************************************************/
/* Built by Mitchell Kates */

// var states = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'Washington D.C.', 'West Virginia', 'Wisconsin', 'Wyoming'];


// Each form elements needs the following elements :
// data-required: is it required
// data-type: the type of the form (text,password,email,promocode,etc.)
// data-activated = set at the element level

//TODO
// At least one checkbox
// Radio errors
// Clear the input field
// A list of the incomplete fields above
// Show/Hide Password (http://cloudfour.github.io/hideShowPassword/)

$.fn.formValidator = function() {

	// Aggregate all the potential form actions

	$(this).find("input").blur(function() {
		validateInput($(this),'blur');
		$(this).data('activated',true);
	});
	$(this).find("input").keyup(function() {
		validateInput($(this),'keyup');
		if ($(this).hasClass('password')) { // Recheck confirmpassword on any password change
			validateInput($('.confirmpassword'),'keyup');
		}
	});
	$(this).find("select").change(function() {
		validateInput($(this),'change');
	});
	$(this).find("select").blur(function() {
		validateInput($(this),'blur');
		$(this).data('activated',true);
	});
	$(this).find("textarea").blur(function() {
		validateInput($(this),'blur');
		$(this).data('activated',true);
	});
	$(this).find("textarea").on('change keyup paste', function() {
		validateInput($(this),'keyup');
	});
	$(this).find("textarea").on('blur', function() {
		validateInput($(this),'blur');
		$(this).data('activated',true);
	});
	$(this).find("input[type='checkbox']").change(function() {
		validateInput($(this),'check');
	});
	$(this).find("input[type='file']").change(function() {
		validateInput($(this),'change');
	});
	$(this).find("input, select, textarea").focus(function() {
		deactivateMessage();
	});
	// On the form submit action
	$(this).submit(function() {
		all_valid = checkAllInputs($(this)); // This highlights errors as well
		if (all_valid) {
			return true;
		} else {
			return false;
		}
	});

	// Takes in the input handle and the action used
	// Runs it through a series of validators
	var validateInput = function(input,action) {
		var data_type = $(input).attr("data-type");
		var required = $(input).attr('data-required') == 'true' ? true : false;
		if (data_type == 'text') {
			var valid = $(input).val().length >= 2;
		} else if (data_type == 'email') {
			var valid = checkEmail($(input));
		} else if (data_type == 'password') {
			var valid = $(input).val().length > 5 ;
		} else if (data_type == 'confirmpassword') {
			var original_password = $(input).closest('form').find("input.password");
			var passwords_match = ($(original_password).val() == $(input).val());
			var valid = ($(input).val().length >= 1 && passwords_match);
		} else if (data_type == 'promocode') {
			var valid = checkPromoCode($(input));
		}  else if (data_type == 'file') {
			var valid = $(input).val().length >= 1;
		}  else if (data_type == 'phonenumber') {
			var valid = $(input).val().length >= 10;
		} else if (data_type == 'checkbox') {
			var valid = $(input).is(":checked");
		} else if (data_type == 'select') {
			var valid = ($(input).val() != ''); //Selects only valid if not a null value
		} 
		valid ? updateCSS(input,true,required,action) : updateCSS(input,false,required,action);
		return (valid || !(required));
	}

	// Update the CSS based on the input,if its valid, whether its required, and the action
	var updateCSS = function(input,valid,required,action) {
		var form_group = $(input).closest('.form-group');
		var activated = $(input).data('activated');
		var only_good = (!(activated) && action =='keyup'); // Only good is used so X's do not appear as a user begins typing on every input
		if (valid) {
			addCheck(form_group);
		} else if (!(valid) && !(required)) {
			addNothing(form_group);
		} else if (!(valid) && !(only_good)) { // Not valid and it has been activated as a field (used so x doesnt appear before a blur event)
			addError(form_group);
		}
		if (action=="check" && !(valid) && required) { //Required checkboxes: invalid
			addError(form_group);
		} else if (action=="check" && valid && required){ //Required checkboxes: valid
			addCheck(form_group);
		}
	}
	function addCheck(input) {
		$(input).removeClass('has-error');
		if (!($(input).hasClass('has-check'))) {
			$(input).addClass('has-check');
		}
	}
	function addError(input) {
		$(input).removeClass('has-check');
		if (!($(input).hasClass('has-error'))) {
			$(input).addClass('has-error');
		}
	}
	function addNothing(input) {
		$(input).removeClass('has-check');
		$(input).removeClass('has-error');
	}


	var isEmail = function(email) {
		var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
	 	return emailReg.test(email);
	}

	var checkEmail = function(input) {
		var email = $(input).val();
		var validemail = (isEmail(email) && email.length >0);
		if (!(validemail)) {
			$(input).parent().find('.error').text("Invalid Email");
			return false;
		}
		// $.ajax({
		// 	type : "GET",
		// 	data : {'email':email},
		// 	url : "/checkemail",
		// 	success : function(data) {
		// 		if (data == 'valid') {
		// 			updateCSS(input,true,true,'email-check')
		// 		} else {
		// 			$(input).parent().find('.error').text("Email already in use. Please login instead");
		// 			updateCSS(input,false,true,'email-check')
		// 		}
		// 	}
		// });
		return true;
	}

	var checkPromoCode = function(input) {
		var promo = $(input).val();
		// $.ajax({
		// 	type : "GET",
		// 	data : {'promo':promo},
		// 	url : "/checkpromo",
		// 	success : function(data) {
		// 		if (data['status'] == 201) {
		// 			$(input).parent().find('.success').text(data['text']);
		// 			updateCSS(input,true,false,'promo-check')
		// 		} else {
		// 			$(input).parent().find('.success').text("");
		// 			updateCSS(input,false,false,'promo-check')
		// 		}
		// 	}
		// });
	}

	var checkAllInputs = function(element) {
		inputs = $(element).find("input, textarea, select")
		all_valid = true
		$.each(inputs,function(index,value) {
			valid = validateInput($(value),'submit');
			if (!(valid)) {
				all_valid = false;
			}
		});
		$.each($(element).find("select"),function(index,value) {
			valid = validateInput($(value),'submit');
			if (!(valid)) {
				all_valid = false;
			}
		});
		if (!all_valid) {
			activateMessage('error',"We need you to complete all of the required fields"); //Show a fixed message error
		}
		return all_valid;
	}
} 


$(document).ready(function() {
	$(".validated-form").formValidator();
});

