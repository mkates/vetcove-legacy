// *********  Supplier Lead Form ************ //

$(document).ready(function() { 

    // bind to the form's submit event 
    $('#LeadSupplierForm').submit(function() { 
        $(this).ajaxSubmit({
            target:        '#response',   // target element(s) to be updated with server response 
            beforeSubmit:  showRequest,  // pre-submit callback 
            error:         showResponse,
            success:       showResponse  // post-submit callback 
        }); 
        return false; //DO NOT CHANGE!
    }); 
}); 
 
// pre-submit callback 
function showRequest(formData, jqForm, options) { 
    var queryString = $.param(formData); 
    
    // Validate here, return false if invalid form!

    return true;  //Form is valid, so submit
} 
 
// post-submit callback 
function showResponse(responseText, statusText, xhr, $form)  { 
    console.log(xhr);
    console.log("here")
    alert('status: ' + statusText + '\n\nresponseText: \n' + responseText + 
        '\n\nThe output div should have already been updated with the responseText.'); 
} 