/**************************************************/
/****** Ajax Submitting of Forms  *****************/
/**************************************************/
/* Built by Mitchell Kates */

// IMPORTANT: A form that is submitted via ajax needs the class: ajaxform


// ****** The standard form submitting via ajax *******
$(document).ready(function() { 

    // Add validation to all the forms with class form-validation
    $('.form-validation').formValidator();

    // All ajax forms get the class ajaxform
    $('.ajaxform').submit(function() { 
        $(this).ajaxSubmit({
            dataType:      'json', // Required! or success callback will fail
            async :         false,
            beforeSubmit:  preSubmit,  // Pre submit callback, for final client side validation
            success:       showSuccess, // On success actions
            error:         showError, // On error actions
        }); 
        return false; // DO NOT CHANGE THIS!
    }); 

    // Pre-Submit Checks
    function preSubmit(formData, jqForm, options) {
        buttonStartSubmitting(jqForm);
        return true
        // Validated forms get checked before submitting
        if (jqForm.hasClass('form-validation')) { 
            form = jqForm.formValidator();
            all_valid = form.checkSubmit();
            if (!all_valid) {
                buttonFinishSubmitting(jqForm);
                return false
            }
        }
        return true // No validation, so just submit it
    } 

    // Post-Submit Error Callbacks
    function showError(responseText, statusText, xhr, $form)  { 
        buttonFinishSubmitting($form);
        // Display an error message
        errors_div = $form.find(".non-field-errors").html("We encountered an error. Please fix the fields highlighted in red");
        // Update individual fields
        error_dict = JSON.parse(responseText.responseText);
        for (var key in error_dict) {
            element = $form.find("[name="+key+"]").closest(".form-group");
            element._addClass('has-error');
            element.find('.error-message').html(error_dict[key]);
        }     
    } 
    // Post-Submit Success Callback
    function showSuccess(responseText, statusText, xhr, $form)  { 
        // Return button to normal
        buttonFinishSubmitting($form);
        $("#clinicform").fadeOut();
        // Clear the form
        $form[0].reset();
        // Bring in the thank you message
        $(".lead-thanks").fadeIn();
    } 
}); 


function buttonStartSubmitting(jqForm) {
    handle = jqForm.find('.submit')
    handle.html("<i class='fa fa-15x fa-inline fa-spin fa-spinner'></i>");
    handle.attr('disabled','disabled');
}
function buttonFinishSubmitting(jqForm) {
    handle = jqForm.find('.submit')
    handle.html("Submit");
    handle.attr('disabled',false);
}