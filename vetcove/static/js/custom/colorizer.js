//************************************************
//**** Text Colorizer gives an apple text effect *
//************************************************
// The div must only contain text

$.fn.textColorizer = function(original,highlight) {
	// Split up the text
	handle = $(this);
	text = $(handle).text();
	handle.empty();
	for ( var i = 0; i < text.length; i++ ) {
	  handle.append("<span class='text_colorizer' data-timeout='"+i+"'>"+text.charAt(i)+"</span>");
	}
	// Start colorizing function
	$.each($(handle).children(".text_colorizer"),function(index,value) {
		id = parseInt($(value).attr('data-timeout'));
		timeout = 2000+(80*id);
		setTimeout(function() {colorize(value)},timeout);
	});

	// Function loops and colorizes the text
	function colorize(letter) {
		$(letter).animate({color: highlight}, 120, 
			function() {
	        	$(letter).animate({color: original},120,
	        		function() {
	        			setTimeout(function() {colorize(letter)},5000);
	        		}
	        	);
	        }
	    );
	}
}
