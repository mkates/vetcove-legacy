###########################
Static File Structure
###########################

Less
============================

We use less to generate our stylesheets. We import all Less files into one master file, main.less. We **NEVER** directly write to the CSS files, which are overwritten when we compress the Less to CSS

.. Using bootstrap -> use the bootstrap less file (customize at getbootstrap.com, and override all bootstrap elements with our own files

Less File Structure
----------------------------

**Plugins**

	all 3rd party plugins

**Generic (Includes all generic formatting -> No CSS output)**

	mixins.less -> Includes all the generic mixins we use (nothing specific)

	utilities.less -> Includes utilities (centered, clear, etc)

**General (Project specific global styling)**

	resets.less -> Override any bootstrap defaults here

	variables.less -> All the project specific variables

	type.less -> fonts and header styles

**Layout (Page layout files)**

	base.less -> General page layout options and formatting (page width, etc.)

	layout.less -> Includes all layout base styles (columns, table cells, grids etc.)

	header.less
	
	footer.less
	
	sidebar.less
	
	// Page Specific Layout Styles
	
	member.less -> Login/Logout/Signup/SignIn/etc.
	
	search.less -> Search page layout

**Modules ( Try to make more modules, and less page specific CSS )**

	widgets.less (ribbons, stars, etc.)
	
	forms.less
	
	buttons.less
	
	dropdowns.less
	
	product.less -> Include all the different ways to display a product (list, search, cart, etc.)

**Custom CSS (that's not in a module)**


*Pointer:* Using ~"Blah Blah Blah" prevents less from processing, good for calc() units


---------------------------------

Images
============================

general
    backgrounds
   		stylebackgrounds
   		imagebackg
   	gradients
   	transparency
   	shadows
modules
    logo
    error (404,500,etc.)
	noimage
    banner
    loaders
    slider
    stars
    icons
pages
	login
	rewards (will be uploaded with media not static eventually)
	corporate (static images)
plugins
	balanced


