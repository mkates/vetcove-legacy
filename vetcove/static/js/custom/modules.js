
// String prototype that adds a string at a specified index in another strings
String.prototype.insert = function (index, string) {
  if (index >= 0 && index <= this.length) {
    return this.substring(0, index) + string + this.substring(index, this.length);
  }
  return this
};



// Helper class to add a class, but checks first if the element already has the class
$.fn._addClass = function(class_name) {
	if (!($(this).hasClass(class_name))) {
		$(this).addClass(class_name);
	}
}