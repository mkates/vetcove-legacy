
//*************************************************
//************** Dropdown Functionality ***********
//*************************************************
$(document).ready(function() {

	//Activates/Deactivates a dropdown as well as hide all other dropdown
	$(".dropdown-trigger").click(function() {
		$(".dropdown-box").css('display','none');
		var active = $(this).hasClass('active');
		$(".dropdown-trigger").removeClass('active');
		if (!(active)) {
			$(this).addClass('active');
			$("#"+$(this).attr('data-dropdown')).fadeIn(300);
		} 
	});

	//Displays the subcategories on the category select
	$(".category-box .category-menu-item").click(function(){
		// Display appropriate subcategory
		var data_name = $(this).attr("data-name");
		$(".category-info").css('display','none');
		$("#menu-"+data_name).css('display','block');
		
		// Add active to category-menu-item
		$(".category-box .category-menu-item").removeClass('active');
		$(this).addClass("active");
	});
});

//Hides all the dropdowns when there is a click outside of a dropdown
$(document).click(function(event) { 
    if(!$(event.target).closest('.dropdown-container').length) {
        if($('.dropdown-box').is(":visible")) {
            $('.dropdown-box').hide();
            $(".dropdown-trigger").removeClass('active');
        }
    }        
})

//*************************************************
//********** Scroll to Top ************************
//*************************************************

$(document).ready(function() {
    var offset = 220;
    var duration = 500;
    $(window).scroll(function() {
        if ($(this).scrollTop() > offset) {
            $('.back-to-top').fadeIn(duration);
        } else {
            $('.back-to-top').fadeOut(duration);
        }
    });
    
    $('.back-to-top').click(function(event) {
        event.preventDefault();
        $('html, body').animate({scrollTop: 0}, duration);
        return false;
    });
});

// *************************************************
// ********** Menu-Aim *****************************
//**************************************************

$(document).ready(function(){
	$(function(){
		$("#category-menu-ul").menuAim({
			activate: function(handle){
				// Display appropriate subcategory
				var data_name = $(handle).children('a').attr("data-name");
				$(".category-info").css('display','none');
				$("#menu-"+data_name).css('display','block');
				// Add active to category-menu-item
				$(".category-box .category-menu-item").removeClass('activate');
				$(handle).children('a').addClass("activate");
			},  // fired on row activation
			deactivate: function(handle){
				//DEACTIVATE FUNCTION
			}  // fired on row deactivation
		});
	});
});

// *************************************************
// ********** Enable all tooltips ******************
// *************************************************

$(document).ready(function(){
	$('.tooltip-div').tooltip();
});


// *************************************************
// ********** Create Loaders ***********************
// *************************************************

$(document).ready(function(){
	createLoader($(".loader"),'#5ecadf');
});

// *************************************************
// ********** Footer Effect ************************
// *************************************************

$(document).ready(function(){
	$(".footer-links a").hover(function() {
		$(".footer-links a").addClass('faded');
		$(this).removeClass('faded');
	},function() {
		$(".footer-links a").removeClass('faded');
	});
});

// *************************************************
// ********** Message X Functionality **************
// *************************************************

// A user can dismiss the message bar
$(document).ready(function(){
	$('.message-container .x').click(function() {
		$(this).closest('.message-container').slideToggle();
	});
});

// Activates the message bar
// Takes two parameters: a message type and a message text
function activateMessage(type,text) {
	// Remove all formatting classes
	$(".message-container").removeClass("success");
	$(".message-container").removeClass("error");
	$(".message-container").removeClass("info");

	// Add the appropriate tag
	if (type=='error') {
		$(".message-container")._addClass("error");
	} else if (type=='success') {
		$(".message-container")._addClass("success");
	} else if (type=='info') {
		$(".message-container")._addClass("error");
	}

	// Add the appropriate text
	$(".message-container p").text(text);

	// Slide Toggle the element
	$(".message-container").stop();
	if ($(".message-container").is(':visible')) {
		$(".message-container").css('display','block');
	} else {
		$(".message-container").slideToggle();
	}
}

// Deactivated the message bar 
function deactivateMessage() {
	$(".message-container").fadeOut();
}

// *************************************************
// ********** Supplier Demographic Tool ************
// *************************************************

$(document).ready(function(){
	$(".demographic").change(function(){
		one = parseFloat($(".demographic_one").val());
		two = parseFloat($(".demographic_two").val());
		three = parseFloat($(".demographic_three").val());
		number = parseInt(one*two*three*10000);
		$(".sp .reach span").html(number+" veterinarians");
	})

});

// *************************************************
// ********** JQuery Knobs *************************
// *************************************************
$(document).ready(function(){
	$(function() {
    	$(".dial").knob({
    		'min':0,
    		'thickness':.2,
    		"fgColor":'#45b9f3',
    		'inputColor':'#45b9f3',
    		'fontWeight':200,
    		'width':100,
    		'height':80,
    		'angleOffset':-120,
			'angleArc':240,
    		'readOnly':true, 
    		'draw' : function () { 
				if ($(this.$).attr('data-type')=='dollar') {
					$(this.i).val(this.cv+"%");
				} else {
		       		$(this.i).val(this.cv + ' of '+$(this.$).attr('data-max'));
		       	}
		      }
    	});
    	$(".dial").css('font-size','16px');
    });
});

// *************************************************
// ********** Dashboard Question Box ***************
// *************************************************
$(document).ready(function(){
	$(".dashboard-question").click(function(){
		$('.dashboard-item-overlay').fadeOut('fast');
		$(this).closest('.dashboard-item').find('.dashboard-item-overlay').fadeIn('fast');
	});
	$(".dashboard-item-overlay .exit").click(function(){
		$(this).closest('.dashboard-item-overlay').fadeOut('fast');
	});

	// For static usage
	$(".dashboard-item-container").hover(function(){
		$(this).find('.dashboard-item-overlay').fadeIn('fast');
	}, function() {
		$(this).find('.dashboard-item-overlay').stop();
		$(this).find('.dashboard-item-overlay').fadeOut('fast');

	});
});

// *************************************************
// ********** Support Center ***********************
// *************************************************
// Functionality for the support center question filtering
$(document).ready(function(){
	$('.support-sidebar a').click(function(){
		//Activate the css for the sidebar
		$('.support-sidebar a').removeClass('active');
		$(this).addClass('active');
		// Set the title to the main of the sidebar span element
		$('.help-title').html($(this).find('span').html());
		// Get the sidebar's tag name
		tag_name = $(this).attr('data-tag');
		// Only show questions with that tag
		$.each($(".question"),function(idx,value){
			has_tag = $(value).attr('data-tag-'+tag_name);
			if (has_tag) {
				$(value).css('display','block');
			} else {
				$(value).css('display','none');
			}
		});

	});
});

// *************************************************
// ********** Activate the side menu ***************
// *************************************************
$(document).ready(function() {
	$('#sidr-menu').sidr();
	//If menu is open and resized to larger, close the side menu
	$(window).resize(function() {
		if ($(window).width() > 568) {
			$.sidr('close', 'sidr');
		}
	});
	$(document).click(function(event){
		 if(!$(event.target).closest('.sidr').length) {
		 	$.sidr('close', 'sidr');
		 };
	});

});


// *************************************************
// ********** Image Upload Preview *****************
// *************************************************

$(document).ready(function() {

	// Need to manually register the jquery dataTransfer event
	$.event.props.push('dataTransfer');

	var dropZone = $('.upload-container');
  	dropZone.on('dragover', function(event){
  		event.stopPropagation();
	    event.preventDefault();
	    event.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
  	});
  	dropZone.on('drop', function(event){
  		event.stopPropagation();
	    event.preventDefault();

	    var files = event.dataTransfer.files; // FileList object.
	    console.log(files);
  	});




	// Check if there already is an image file selected
	// If so, display the preview box instead
	$.each($('.file-input'),function(index,value) {
		value = $(value);
		if (value.val() != "") {
			PreviewImage(value);
			upload_container = value.closest(".upload-container");
			upload_container.find('.upload-preview').css('display','block');
			upload_container.find('.upload-box').css('display','none');
		}
	});



	$('.upload-button').click(function(){
		// Trigger an input click on an upload button click
		 $(this).closest(".upload-container").find('input[type=file]').trigger('click');
	});
	$('.file-input').change(function(){
		// Get the container's handle
		upload_container = $(this).closest(".upload-container");
		// Generate an image preview
		PreviewImage(upload_container.find('input[type=file]'));
		// Show the upload preview and hide the upload box
		upload_container.find('.upload-box').fadeOut('fast',function(){
			upload_container.find('.upload-preview').fadeIn('fast');
		})
	});
	$('.upload-clear').click(function(){
		// Get the container's handle
		upload_container = $(this).closest(".upload-container");
		// Clear the file input
		upload_container.find('input[type=file]').val("");
		// Show the upload box and hide the preview
		upload_container.find('.upload-preview').fadeOut('fast',function(){
			upload_container.find('.upload-box').fadeIn('fast');
		})
	});

});

function PreviewImage(handle) {
	// Create an instance of file reader
    var oFReader = new FileReader();
    // Get an instance of the file
    oFReader.readAsDataURL(handle.prop("files")[0]);
    // Get the handle for the image preview img
    image_preview = handle.closest('.upload-container').find('.upload-preview-image');
    // Populate the image's src with the filereader result
    oFReader.onload = function (oFREvent) {
        image_preview.attr('src',oFREvent.target.result);
    };
};




// ******* The Dropzone for use in uploading images and pdfs for products ******* //
Dropzone.options.easyDropdown = {
  paramName: "file", // The name that will be used to transfer the file
  //forceFallback: true, //Used to test the fallback
  clickable: false, // Make the drop zone not clickable
  previewTemplate: $("#dz-template").html(),
  acceptedFiles: "image/jpeg,image/png,image/gif,application/pdf",
  previewsContainer: "#uploads", // Define the container to display the previews
  clickable: ".fileinput-button", // Define the element that should be used as click trigger
  accept: function(file, done) {
  	MAX_FILE_SIZE = 5 //MB
  	ACCEPTED_FILES = ['image/png','image/jpeg','image/gif','application/pdf']
    if (file.size > MAX_FILE_SIZE *1024*1024) {
      filesize = Math.floor(parseFloat(file.size/1048576.0) * 100 ) /100
      done("Maximum file size accepted is "+MAX_FILE_SIZE +"MB. Your file was "+filesize+"MB");
    }
    else if (ACCEPTED_FILES.indexOf(file.type) == -1) {
      done("We only accept PNG, JPEG, GIF and PDF files");
    }
    else {
    	dropzoneRemoveError($("#easyDropdown"));
    	done();
    }
  },
  init: function() {
  	this.on("addedfile", function(file) { 
  		$("#easyDropdown .loader").fadeIn('fast');
  	});
  	this.on("error", function(file,errorMessage) { 
  		$("#easyDropdown .loader").stop();
  		$("#easyDropdown .loader").fadeOut('fast');
  		dropzoneAddError($("#easyDropdown"),errorMessage['message'])
  	});
  	this.on("success", function(file,response) { 
  		$("#easyDropdown .loader").fadeOut('fast');
  	});
  	// Hide the dropdone content if falling back to the standard uploader
  	if ($("#easyDropdown .fallback").length > 0) {
		$("#easyDropdown .dropdown-content").css('display','none');
	}
  }
};

function dropzoneAddError(dropzone,message) {
	dropzone.find('.upload-error').html(String(message));
}

function dropzoneRemoveError(dropzone) {
	dropzone.find('.upload-error').html("");
}



