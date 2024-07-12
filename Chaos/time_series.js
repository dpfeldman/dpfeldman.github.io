// This script calculates the time series for the logistic equation
// It then prints the time series to the browser and makes
// a time series plot
//
// David P. Feldman
// July 2012
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

function timeseries(n,x0,r) 
{
    var error_msg="<br>";
    //document.getElementById("error").innerHTML=error_msg;
    //perform some sanity checks
    if(n>10000){
	error_msg = error_msg +  "<b>Error: n must be less than 10,000.</b><br><br>";
	n=0;
	//document.getElementById("error").innerHTML=error_msg;
    }
   if(r<0 || r>4.0){
	error_msg = error_msg + "<b>Error: r must be between 0 and 4.0.</b><br><br>";
	n=0;
    }
   if(x0<0 || x0>1){
	error_msg = error_msg + "<b>Error: x<sub>0</sub> must be between 0 and 1.0.</b><br><br>";
	n=0;
    }
    document.getElementById("error").innerHTML=error_msg;
    

    var T = [ [0,x0] ] // holds the timeseries
    var x = (+x0);      // initial value of x is 0
    // Prepare the output for reporting
    var msg = '<table border="0.5"><tr><td width="150">Time <i>t</i></td><td width="200">x<sub>t</sub></td></tr>';
    msg += '<tr><td>0</td><td>'+x0+'</td></tr>';        
    // loop for required number of iterations
    for (var t = 1; t <= n; t++)
    {
        x = f(x,r);
	T.push([t,x]);
        // record the t and x_t values
        msg += '<tr><td>'+t+'</td><td>'+roundNumber(x,5)+'</td></tr>';
//        msg += '<tr><td>'+t+'</td><td>'+x+'</td></tr>';
    }
    msg += '</table>';
    // print out the time series values
    document.getElementById("msg").innerHTML=msg;
    // Make the plot
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
	var plot1 = $.jqplot ('placeholder',[T], {
	    series:[{
		showMarker:true,
		color:"purple"
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
		    label:"x_t",
		    min:0,
		    max:1,
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
    
    //plot1.replot({resetAxes:true});
}
	 
