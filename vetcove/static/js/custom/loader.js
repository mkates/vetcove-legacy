//Creates a loader at the specified location

function createLoader(div,color) {
	//Create Hexagonal Loader Parameters
	var hexagonal_loader = {
		width: 100,
		height: 100,
		stepsPerFrame: 10,
		fillColor: color,
		trailLength: .7,
		pointDistance: .01,
		fps: 30,
		path: [
			['line',50,15,70,30],
			['line', 70,30,70,50],
			['line', 70,50,50,65],
			['line', 50,65,30,50],
			['line', 30,50,30,30],
			['line', 30,30,50,15]
		]
	};

	// Adds sonic loader to the div and plays it.
	loader = div;
	loader_div = $("<div>")
	sonic = new Sonic(hexagonal_loader);
	$(loader_div).append(sonic.canvas);
	$(loader).append(loader_div);
	sonic.play();
}