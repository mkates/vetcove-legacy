
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
	$(".dashboard-item").hover(function(){
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