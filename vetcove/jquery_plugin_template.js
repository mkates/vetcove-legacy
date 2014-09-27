
;(function($) {

    $.fn.formValidation = function(options) {

        var defaults = {
            age: '43',
            onSomeEvent: function() {}
        }

        var plugin = this;

        plugin.settings = {}

        var init = function() {
            plugin.settings = $.extend({}, defaults, options);
            // code goes here
        }

        plugin.foo_public_method = function() {
        	console.log(this.age);
            console.log(plugin);
        }

        plugin.setBorder = function(color) {
        	$(this).css('border','1px solid blue');
        }
        plugin.set_age = function(age) {
        	plugin.age = age;
        }
        var foo_private_method = function() {
            // code goes here
        }

        init();
        return this

    }