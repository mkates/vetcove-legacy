//****** Tabs ********* //

;(function($) {

	$.fn.tabs = function() {

		// Handle for the plugin
		var plugin = this;

		// Initialization
		var init = function() {
			tabs = plugin.find('.tab-option');
			contents = plugin.find('.tab-content');
			tabs.click(function() {
				reference = $(this).attr('data-ref');
				reference_handle = $(reference);
				if (!($(this).hasClass('active'))) {
					tabs.removeClass('active');
					$(this).addClass('active');
					contents.css('display','none');
					$(reference).css('display','block');
				}
			});
		}

		init();

		return this 

	} 
})(jQuery);
