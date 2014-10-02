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
				error_message = $(value).attr('data-errormessage');
				$(value).closest('.form-group').find(".error-message").html(error_message);
			});

			// Check all inputs that should be hidden and appropriately toggle them
			$.each(plugin.find("[data-toggle-name]"), function(idx,value) {
				updateToggle($(value));
			});
			// Format phone numbers on any change
			plugin.find("input[data-type='phonenumber']").keyup(function(e) {
				$(this).val(formatPhoneNumber(e,$(this).val()));

			});

			// On all form blur events, trigger a check
			plugin.find("input, select, textarea").blur(function() {
				$(this).data('activated',true);
				validateInput($(this),'blur');
			});

			// On all changes to an input and textarea
			plugin.find("input, textarea, select").on('change keyup paste',function() {
				validateInput($(this),'change');
				// Also check the confirmpassword when a password is changed
				if ($(this).attr('data-type') == 'password' || $(this).attr('data-type') == 'confirmpassword') {
					updatePasswordBlock($(this)); // Set the password strength
					validateInput(plugin.find($('input[data-type="confirmpassword"]'),'keyup'));
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
					return plugin.checkSubmit();
				});
			} 

		}

		// Takes in the input handle and the action  (change, check, blur, submit, etc.)
		// Runs it through the appropriate validator
		var validateInput = function(input,action) {
			data_type = input.attr("data-type");
			required = input.attr('data-required') == 'True' ? true : false;
			if (data_type == 'text') {
				var valid = input.val().length >= 1;
			} else if (data_type == 'email') {
				var valid = checkEmail(input);
			} else if (data_type == 'password') {
				var valid = input.val().length > 7 ;
			} else if (data_type == 'confirmpassword') {
				original_password = input.closest('form').find($('input[data-type="password"]'));
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
			} else if (data_type == 'postalcode') {
				var valid = input.val().length >= 5;
			} else if (data_type == 'checkbox') {
				var valid = input.is(":checked");
			} else if (data_type == 'select') {
				var valid = (input.val() != ''); //Selects only valid if not a null value
			} else if (data_type == 'file') {
				var valid = (input.val() != ''); // File only valid if it has a file name
			} 
			valid ? updateCSS(input,true,required,action) : updateCSS(input,false,required,action);
			// Toggle Inputs on every validation
			updateToggle(input);
			return (valid || !(required));
		}


		function updateToggle(input) {
			toggler = input.attr('data-toggle-name');
			toggle_handle = plugin.find(".id_"+toggler);
			if (toggler) {
				toggle_element = input.attr('data-toggle-value');
				if (toggle_element == input.val()) {
					toggle_handle.find("input,select").attr('data-required','True');
					toggle_handle.removeClass('hidden');
				} else {
					toggle_handle.addClass('hidden');
					toggle_handle.find("input,select").attr('data-required','False');
				}
			}
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
			} else if (!(valid) && required && !(activated)) { // Not valid, required, not activated
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
			if (key_id.keyCode != 46 && key_id.keyCode != 8) { //Delete or backspace
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
			return value
		}


		function updatePasswordBlock(handle) {
			// Calculate the strength and get the score
			strength = setPasswordStrength(handle.val());
			score = strength['score'];
			//Update password text
			password_block = handle.closest('.form-group').find(".password-meter");
			password_block.find('.password-text').html(strength['text']);
			// Set block colors
			colors = {1:'#e75656',2:'#edd532',3:'#bbec38',4:"#6add47"};
			color = colors[score]
			password_block.children('.password-block').css('background','#dadada');
			if (score >= 1) { password_block.children('.password-block-one').css('background',color) } 
			if (score >= 2) { password_block.children('.password-block-two').css('background',color) }
			if (score >= 3) { password_block.children('.password-block-three').css('background',color) }
			if (score >= 4) { password_block.children('.password-block-four').css('background',color) }
		}

		function setPasswordStrength(txtpass) {
			strength_text = {0:'Too Weak',1:'Weak',2:'Average',3:'Strong',4:'Really Strong'}
			score = 0 // Password score
			if (txtpass.length > 0) score++;
			// Over 4 characters and add a point
			if (txtpass.length > 3) score++;
			// Over 8 characters and add a point
			if (txtpass.length > 6) score++;
		    //if txtpass has both lower and uppercase characters give 1 point
		    if ( ( txtpass.match(/[a-z]/) ) && ( txtpass.match(/[A-Z]/) ) ) score++;
			//if txtpass has at least one number give 1 point
			if (txtpass.match(/\d+/)) score++;
			//if txtpass has at least one special caracther give 1 point
			if ( txtpass.match(/.[!,@,#,$,%,^,&,*,?,_,~,-,(,)]/) ) score++;
			//if txtpass bigger than 12 give another 1 point
			return {'score':score,'text':strength_text[score]}
		}

		// Run the initialization
		init();

		// Return a handle of the object
		return this 

	} 
})(jQuery);




