

// Chart for Supplier Static Page
$(document).ready(function(){
	if ($("#supplierchart").length) { //Only call function if div is present, otherwise amcharts error
		var chart_two = AmCharts.makeChart("supplierchart", {
		    "type": "serial",
		    "theme": "none",
		    "titles": [
				{
					"text": "Equizone 100 Phenylbutazone Powder Performance",
					"size": 13
				}
			],
			 "legend": {
		        "equalWidths": false,
		        "position": "bottom",
		        "valueAlign": "left",
		        "valueWidth": 0
		    },
		    "pathToImages": STATIC_URL+"img/amcharts/",
		    "dataProvider": [{
		        "date": "2015-03-01",
		        "visits": 26,
		        "purchases": 10,
		    }, {
		        "date": "2015-03-08",
		        "visits": 15,
		        "purchases": 8
		    }, {
		        "date": "2015-03-15",
		        "visits": 32,
		        "purchases": 5
		    },{
		        "date": "2015-03-22",
		        "visits": 24,
		        "purchases": 7
		    }, {
		        "date": "2015-03-29",
		        "visits": 26,
		        "purchases": 10
		    }, {
		        "date": "2015-04-05",
		        "visits": 125,
		        "purchases": 25
		    }, {
		        "date": "2015-04-12",
		        "visits": 185,
		        "purchases": 32,
		    }, {
		        "date": "2015-04-19",
		        "visits": 42,
		        "purchases": 21
		    }, {
		        "date": "2015-04-26",
		        "visits": 27,
		        "purchases": 17
		    },{
		        "date": "2015-05-03",
		        "visits": 34,
		        "purchases": 15
		    }, {
		        "date": "2015-05-10",
		        "visits": 31,
		        "purchases": 13
		    }, {
		        "date": "2015-05-17",
		        "visits": 20,
		        "purchases": 16
		    },
		    ],
		    "valueAxes": [{
		        "axisAlpha": 0.2,
		        "dashLength": 1,
		        "position": "left"
		    }],
		    "graphs": [{
		        "id":"g1",
		        "balloonText": "[[category]]<br /><b><span style='font-size:14px;'>Weekly Page Views: [[value]]</span></b>",
		        "bullet": "round",
		        "lineColor": '#afcc5a',
		        "bulletBorderAlpha": 1,
				"bulletColor":"#FFFFFF",
		        "hideBulletsCount": 50,
		        "title": "Page Views",
		        "hidden":true,
		        "valueField": "visits",
				"useLineColorForBulletBorder":true
		    },{
		        "id":"g2",
		        "balloonText": "[[category]]<br /><b><span style='font-size:14px;'>Weekly Purchases: [[value]]</span></b>",
		        "bullet": "round",
		        "lineColor": '#809ae5',
		        "bulletBorderAlpha": 1,
				"bulletColor":"#FFFFFF",
		        "hideBulletsCount": 50,
		        "title": "Purchases",
		        "valueField": "purchases",
				"useLineColorForBulletBorder":true
		    }],
		    "chartScrollbar": {
		        "autoGridCount": true,
		        "graph": "g2",
		        "scrollbarHeight": 30
		    },
		   	"chartCursor": {
		        "cursorAlpha": 0
		    },
		    "categoryField": "date",
			"categoryAxis": {
				"parseDates":true,
				"startOnAxis": true,
		        "axisColor": "#DADADA",
		        "gridAlpha": 0.07,
		        "guides": [{
		            date: new Date(2015,2,29),
		            toDate: new Date(2015,3,12),
		            lineColor: "#809ae5",
		            lineAlpha: 1,
		            fillAlpha: 0.2,
		            fillColor: "#809ae5",
		            dashLength: 2,
		            inside: true,
		            labelRotation: 90,
		            label: "Vetcove Credit Promotion"
		        }]
		    },
		});
	}
});


$(document).ready(function(){
	if ($("#featureschart").length) {
		var chart_three = AmCharts.makeChart("featureschart", {
		    "type": "serial",
		    "theme": "none",
		    "pathToImages": STATIC_URL+"img/amcharts/",
		    "legend": {
		        "equalWidths": false,
		        "periodValueText": "",
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
	}
});