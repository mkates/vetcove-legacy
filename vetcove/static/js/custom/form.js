 /*************************************************/
/* Custom Built Form Validator For All Forms *****/
/*************************************************/
/* Built by Mitchell Kates */

// Each form elements needs the following elements :
// data-required: is it required
// data-type: the type of the form. The following data-types are accepted:
// text, email, password, confirmpassword, promocode, file, number, phonenumber, checkbox, select

;(function($) {

	$.fn.formValidator = function() {

		// Handle for the plugin
		var plugin = this;

		// Initialization
		var init = function() {

			// Takes the data attribute data-invalid and sets the error message
			$.each(plugin.find("input, select, textarea"),function(index,value) {
				error_message = $(value).attr('data-invalid');
				$(value).closest('.form-group').find(".error-message").html(error_message);
			});

			// Format phone numbers on any change
			$("input[data-type='phonenumber']").keyup(function(e) {
				$(this).val(formatPhoneNumber(e,$(this).val()));

			});

			// On all form blur events, trigger a check
			plugin.find("input, select, textarea").blur(function() {
				validateInput($(this),'blur');
				$(this).data('activated',true);
			});

			// On all changes to an input and textarea
			plugin.find("input, textarea, select").on('change keyup paste',function() {
				validateInput($(this),'change');
				// Also check the confirmpassword when a password is changed
				if ($(this).hasClass('password')) {
					validateInput($('.confirmpassword'),'keyup');
				}
			});

			// For checkboxes, we provide a special call
			plugin.find("input[type='checkbox']").change(function() {
				validateInput($(this),'check');
			});

			// Deactivate the error message when we focus on a field
			plugin.find("input, select, textarea").focus(function() {
				deactivateMessage();
			});

			// Finally, on submit, let's do one more check if it is not an ajaxform,
			// Ajax forms are checked in the forms file
			if (!(plugin.hasClass('ajaxform'))) {
				plugin.submit(function() {
					return checkSubmit();
				});
			} 
		}

		// Takes in the input handle and the action  (change, check, blur, submit, etc.)
		// Runs it through the appropriate validator
		var validateInput = function(input,action) {
			data_type = input.attr("data-type");
			required = input.attr('data-required') == 'True' ? true : false;
			if (data_type == 'text') {
				var valid = input.val().length >= 2;
			} else if (data_type == 'email') {
				var valid = checkEmail(input);
			} else if (data_type == 'password') {
				var valid = input.val().length > 5 ;
			} else if (data_type == 'confirmpassword') {
				original_password = input.closest('form').find("input.password");
				passwords_match = ($(original_password).val() == input.val());
				var valid = (input.val().length >= 1 && passwords_match);
			} else if (data_type == 'promocode') {
				var valid = checkPromoCode(input);
			}  else if (data_type == 'file') {
				var valid = input.val().length >= 1;
			}  else if (data_type == 'number') {
				var valid = parseInt(input.val()) >= 0;
			} else if (data_type == 'phonenumber') {
				var valid = input.val().length >= 14;
			} else if (data_type == 'checkbox') {
				var valid = input.is(":checked");
			} else if (data_type == 'select') {
				var valid = (input.val() != ''); //Selects only valid if not a null value
			} 
			valid ? updateCSS(input,true,required,action) : updateCSS(input,false,required,action);
			return (valid || !(required));
		}

		// Update the CSS based on the input,if its valid, whether its required, and the action
		// Parameters: (1) Input Handle, (2) Is the field valid, 
		// (3) Is it required, (4) The action that triggered the validation
		var updateCSS = function(input,valid,required,action) {
			// Form Group Handle
			form_group = input.closest('.form-group');

			// Activated is used so only X's appear after a blur
			// Activated is always true when going to submit

			activated = action=='submit' ? true : input.data('activated')
			if (valid) {
				addCheck(form_group);
			} else if (!(valid) && !(required)) { // Not valid, but not required
				addNothing(form_group);
			} else if (!(valid) && activated) { // Not valid, required, and activated
				addError(form_group);
			}
			if (action=="check" && !(valid) && required) { // Required checkboxes: invalid
				addError(form_group);
			} else if (action=="check" && valid && required){ // Required checkboxes: valid
				addCheck(form_group);
			}
		}

		// Success Formatting
		function addCheck(input) {
			$(input).removeClass('has-error');
			$(input)._addClass('has-check');
		}
		// Error Formatting
		function addError(input) {
			$(input).removeClass('has-check');
			$(input)._addClass('has-error');
		}
		// Remove Success/Error Formatting
		function addNothing(input) {
			$(input).removeClass('has-check');
			$(input).removeClass('has-error');
		}


		// Checks if an email is valid
		var checkEmail = function(input) {
			var email = $(input).val();
			var validemail = (isEmail(email) && email.length >0);
			if (!(validemail)) {
				$(input).parent().find('.error').text("Invalid Email");
				return false;
			}
			return true;
		}

		// Regex for emails
		function isEmail(email) {
			var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
		 	return emailReg.test(email);
		}


		// Checks every input in the form
		var checkAllInputs = function(element) {
			// Grab all the elements
			inputs = $(element).find("input, textarea, select")
			// Iterate through each field
			all_valid = true
			$.each(inputs,function(index,value) {
				valid = validateInput($(value),'submit');
				if (!(valid)) {
					all_valid = false;
				}
			});
			// If an error, trigger an error message
			if (!all_valid) {
				activateMessage('error',"We need you to complete all of the required fields");
			}
			// Return valid status
			return all_valid;
		}


		// Public Method to call before submitting the form via ajax
		this.checkSubmit = function() {
			all_valid = checkAllInputs(plugin);
			return all_valid ? true : false;
		}

		// Takes in a key press ID and the value of the field and reformats the text
		var formatPhoneNumber = function(key_id, value) {
			if (key_id.keyCode != 46 && key_id.keyCode != 8) { //Delet or backspace
				phonenumber = value.replace(/[^0-9]/g, '');
				//If they hit space after the last digit
				phonenumber = (phonenumber.length == 10 && value.slice(-1) == ' ')? phonenumber+" " : phonenumber;
				// Add an extension code x digit
				phonenumber = phonenumber.length > 10 ? phonenumber.insert(10," x ") : phonenumber;
				// Add parenthesis and dashes
				phonenumber = phonenumber.insert(0,"(").insert(4,") ").insert(9,"-");
				// Trim numbers that are too long
				phonenumber = phonenumber.substring(0,21);
				// Redraw phone number
				return phonenumber
			}
		}

		// Run the initialization
		init();

		// Return a handle of the object
		return this 

	} 
})(jQuery);

