//*************************************************
//************** Logo Effect **********************
//*************************************************
$(document).ready(function(){
	$(".header-logo").hover(function(){
		$("#main-logo-alt").stop();
		$("#main-logo-alt").animate({
			opacity:1
		},500);
	},function(){
		$("#main-logo-alt").stop();
		$("#main-logo-alt").animate({
			opacity:0
		},500)
	});
});

//*************************************************
//************** Dropdowns and Categories *********
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
//*************************************************
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