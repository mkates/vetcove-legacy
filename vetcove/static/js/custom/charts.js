
$(document).ready(function(){
	$("#featurechart").css('min-height','400px');
	var chart = AmCharts.makeChart("featurechart", {
	    "type": "serial",
	    "theme": "none",
	    "titles": [
			{
				"text": "Injectable NSAID Orders",
				"size": 13
			}
		],
	    "pathToImages": STATIC_URL+"img/amcharts/",
	    "legend": {
	        "equalWidths": false,
	        "position": "bottom",
	        "valueAlign": "left",
	        "valueWidth": 0
	    },
	    "dataProvider": [{
	        "date": "2014-08",
	        "Phenylbutazone": 5587,
	        "Flunixin": 1650,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 4200,
	        "Fibrocoxib":1241
	    }, {
	        "date": "2014-09",
	        "Phenylbutazone": 5823,
	        "Flunixin": 1950,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 4500,
	        "Fibrocoxib":941
	    }, {
	        "date": "2014-10",
	        "Phenylbutazone": 5612,
	        "Flunixin": 2113,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 4700,
	        "Fibrocoxib":641
	    },{
	        "date": "2014-11",
	        "Phenylbutazone": 6111,
	        "Flunixin": 2345,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 4600,
	        "Fibrocoxib":541
	    }, {
	        "date": "2014-12",
	        "Phenylbutazone": 7121,
	        "Flunixin": 2463,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 5000,
	        "Fibrocoxib":741
	    }, {
	        "date": "2015-01",
	        "Phenylbutazone": 6943,
	        "Flunixin": 2812,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 5200,
	        "Fibrocoxib":341
	    },{
	        "date": "2015-02",
	        "Phenylbutazone": 6191,
	        "Flunixin": 2612,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 5600,
	        "Fibrocoxib":121
	    }, {
	        "date": "2015-03",
	        "Phenylbutazone": 7342,
	        "Flunixin": 2312,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 5820,
	        "Fibrocoxib":80
	    },{
	        "date": "2015-04",
	        "Phenylbutazone": 7423,
	        "Flunixin": 2101,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 5910,
	        "Fibrocoxib":54
	    },{
	        "date": "2015-05",
	        "Phenylbutazone": 7182,
	        "Flunixin": 1854,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 6012,
	        "Fibrocoxib":240
	    }, {
	        "date": "2015-06",
	        "Phenylbutazone": 7298,
	        "Flunixin": 1911,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 5400,
	        "Fibrocoxib":360
	    },{
	        "date": "2015-07",
	        "Phenylbutazone": 8162,
	        "Flunixin": 2012,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 5612,
	        "Fibrocoxib":40
	    },{
	        "date": "2015-08",
	        "Phenylbutazone": 8642,
	        "Flunixin": 1843,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 5843,
	        "Fibrocoxib":100
	    }, {
	        "date": "2015-09",
	        "Phenylbutazone": 8813,
	        "Flunixin": 1650,
	        "Ketoprofen":2221,
	        "Sodium Salicylate": 6451,
	        "Fibrocoxib":700
	    }],
	    "valueAxes": [{
	        "stackType": "regular",
	        "gridAlpha": 0.07,
	        "position": "left",
	        "title": "Purchase Volume ($)"
	    }],
	    "graphs": [{
	        "balloonText": "Phenylbutazone: <span style='font-size:14px; color:#000000;'><b>$[[value]]</b></span>",
	        "fillAlphas": 0.6,
	        "lineAlpha": 0.4,
	        "title": "Phenylbutazone",
	        "valueField": "Phenylbutazone"
	    }, {
	        "balloonText": "Flunixin: <span style='font-size:14px; color:#000000;'><b>$[[value]]</b></span>",
	        "fillAlphas": 0.6,
	        "lineAlpha": 0.4,
	        "hidden": true,
	        "title": "Flunixin",
	        "valueField": "Flunixin"
	    }, {
	        "balloonText": "Sodium Salicylate: <span style='font-size:14px; color:#000000;'><b>$[[value]]</b></span>",
	        "fillAlphas": 0.6,
	        "lineAlpha": 0.4,
	        "title": "Sodium Salicylate",
	        "valueField": "Sodium Salicylate"
	    },{
	        "balloonText": "Ketoprofen: <span style='font-size:14px; color:#000000;'><b>$[[value]]</b></span>",
	        "fillAlphas": 0.6,
	        "lineAlpha": 0.4,
	        "title": "Ketoprofen",
	        "valueField": "Ketoprofen"
	    },{
	        "balloonText": "Fibrocoxib: <span style='font-size:14px; color:#000000;'><b>$[[value]]</b></span>",
	        "fillAlphas": 0.6,
	        "lineAlpha": 0.4,
	        "title": "Fibrocoxib",
	        "valueField": "Fibrocoxib"
	    }],
	    "plotAreaBorderAlpha": 0,
	    "marginTop": 10,
	    "marginLeft": 0,
	    "marginBottom": 0,
	    "chartScrollbar": {},
	    "chartCursor": {
	        "cursorAlpha": 0
	    },
	    "categoryField": "date",
	    "categoryAxis": {
	    	"parseDates": true,
	        "startOnAxis": true,
	        "axisColor": "#DADADA",
	        "gridAlpha": 0.07,
	        "title":'Month'
	    }
	});
});
