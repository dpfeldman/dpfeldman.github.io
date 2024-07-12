// This script calculates the time series for the logistic equation
// It then prints the time series to the browser and makes
// a time series plot
//
// David P. Feldman
// December 2013
//
// This work is licensed under a Creative Commons 
// Attribution-NonCommercial-ShareAlike 3.0 Unported License.
// http://creativecommons.org/licenses/by-nc-sa/3.0/
//
// You are free:
//
//    to Share — to copy, distribute and transmit the work
//    to Remix — to adapt the work
//
// Under the following conditions:
//
//    Attribution — You must attribute the work in the manner specified 
//    by the author or licensor (but not in any way that suggests that 
//    they endorse you or your use of the work).
//
//    Noncommercial — You may not use this work for commercial purposes.
//
//    Share Alike — If you alter, transform, or build upon this work, you 
//    may distribute the resulting work only under the same or similar 
//    license to this one. 


function f(x,r)
{
    // return the value of x_n+1
    return (+r)*(+x)*(1-x);
}

function roundNumber(num, dec) {
    // function that rounds num to dec decimal places
    var result = Math.round(num*Math.pow(10,dec))/Math.pow(10,dec);
    //result = num.toFixed(dec);
    // i think both methods work.  not sure which one i should use
    return result;
}

function makeBifurcation(nPlot,nSkip,rInitial,rFinal,rStep) 
{
 //   alert("1")
    //var error_msg=n + " " + x0 + " " + y0 + " " + r + "<br>";
    var error_msg = "";
    //perform some sanity checks
    if(nPlot>10000){
	error_msg = error_msg +  "<b>Error: n must be less than 10,000.</b><br><br>";
	nPlot=0;
	nSkip=0;
	//document.getElementById("error").innerHTML=error_msg;
    }
    if( (rInitial<0) || (rFinal>4.0) ){
	error_msg = error_msg + "<b>Error: r must be between 0 and 4.0.</b><br><br>";
	nPlot=0;
	nSkip=0;
    }
//    if( (x0<0) || (x0>1) ){
//	error_msg = error_msg + "<b>Error: x<sub>0</sub> must be between 0 and 1.0.</b><br><br>";
//	n=0;
//    }
    if( rStep < 0.0001 ){
	error_msg = error_msg + "<b>Error: r<sub>steps</sub> must be greater than 0.0001.</b><br><br>";
	nPlot=0;
	nSkip=0;
    }
    document.getElementById("error").innerHTML=error_msg;

    var B = [ [1,2] ]; // holds the data for the bifurcation diagram
    var x = 0.44444; // initial value of x
    var r = (+rInitial)
//    B.push([1,2])
//    B.push([3,4])
    alert(B)
    //r = Number(r)
    alert(r)
    r = Number(r)
    alert(r)
    alert(rStep)
    r += Number(rStep)
    alert(r)
    //rStep = Number(rStep)
    var q = 7
    alert(q)
    q += rStep
    alert(q)
 //   var Tx = [ [0,x0] ]; // holds the timeseries for x
    
    while(r<=rFinal){
	// loop for required number of iterations
	for(var t = 1; t <= nSkip; t++)
	{
            x = f(x,r);
	}
	for(var t = 1;t<= nPlot; t++){
	    x = f(x,r);
	    B.push([r,x]);
	}
	alert(B)
	alert(rStep)
	alert(rStep + 4)
	r += Number(rStep)
    }
    // print out the time series values
    // document.getElementById("data").innerHTML=data_msg;

    // MAKE THE INFO AND DISPLAY
    var info_msg = '<p>The purple curve is the time series for ' + x0 + '. ';
    info_msg += 'The green curve is the time series for ' + y0 + '. ';
    info_msg += 'The blue curve (below) is the difference between the two time series.</p>.';

    document.getElementById("info").innerHTML=info_msg;

    // MAKE THE PLOT OF THE TWO TIME SERIES
    // I first need to set delta T, the spacing on the x axis
    var deltaT = 2
    if(n<=40)
	deltaT=2;
    if(n<20)
	deltaT=1;
    if(n>40)
	deltaT = Math.ceil(n/10)
    
    
    $(document).ready(function(){
	    // first clear out the old plot
	    $('#placeholder').empty();
	    var plot1 = $.jqplot ('placeholder',[Tx,Ty], 
    {
	series:[
	    {showMarker:true,
	     color:"purple" },
	    {showMarker:true,
	     color:"green"
	}],
	    axesDefaults: {
		labelRenderer: $.jqplot.CanvasAxisLabelRenderer
	    },
	    axes:{
		xaxis:{
		    label:"Time t",
		    min:0,
		    max:n,
		    pad: 20,
		    tickInterval:deltaT,
		    labelRenderer: $.jqplot.CanvasAxisLabelRenderer,
		    labelOptions:{
			    fontSize: '16pt',
			    textColor: '#333333'
			}
		},
		yaxis:{
		    label:"x_t, y_t",
		    min:0,
		    max:1,
		    pad: 20,
		    labelRenderer: $.jqplot.CanvasAxisLabelRenderer,
		    labelOptions:{
			    fontSize: '16pt',
			    textColor: '#333333'
			}
		},
	    }
	}
				  );
	});
    
    // MAKE THE PLOT OF THE DIFFERENCE BETWEEN THE TWO TIME SERIES
    $(document).ready(function(){
	    // first clear out the old plot
	    $('#placeholder2').empty();
	    var plot1 = $.jqplot ('placeholder2',[D,[[0,0],[n,0]]], 
    {
	series:[
	    {showMarker:true,
	     color:"blue" },
	    {color:"grey",
	     lineWidth:1,
	     markerOptions: {size: 0}},
	    ],
	    axesDefaults: {
		labelRenderer: $.jqplot.CanvasAxisLabelRenderer
	    },
	    axes:{
		xaxis:{
		    label:"Time t",
		    min:0,
		    max:n,
		    pad: 20,
		    tickInterval:deltaT,
		    labelRenderer: $.jqplot.CanvasAxisLabelRenderer,
		    labelOptions:{
			    fontSize: '16pt',
			    textColor: '#333333'
			}
		},
		yaxis:{
		    label:"x_t - y_t",
		    min:-1,
		    max:1,
		    pad: 20,
		    labelRenderer: $.jqplot.CanvasAxisLabelRenderer,
		    labelOptions:{
			    fontSize: '16pt',
			    textColor: '#333333'
			}
		},
	    }
	}
				  );
	});
    


}
	 
