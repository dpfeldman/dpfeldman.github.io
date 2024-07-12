//************************ Creating the preamble  ************************

	function callScripts()
	{

//		<!-- Call CSS -->
//		document.write('<link rel="stylesheet" type="text/css" href="math116.css" />');
		
//		<!-- Favicon -->
//		document.write('<link rel="shortcut icon" href="favicon.ico" />');
	
//		<!-- Call MathJax stuff -->	
		document.write('<SCRIPT SRC="http://palmer.wellesley.edu/MathJax/MathJax.js">');
		document.write('MathJax.Hub.Config({ extensions: ["tex2jax.js","TeX/AMSmath.js","TeX/AMSsymbols.js"], jax: ["input/TeX","output/HTML-CSS"], tex2jax: {inlineMath: [["$","$"]]} });');
		document.write('</SCRIPT>');

//		<!-- General jQuery stuff -->
		document.write('<script type="text/javascript" src="scripts/jquery.min.js"></script>');

//		<!-- Call Fancybox stuff -->
		document.write('<link rel="stylesheet" href="scripts/fancybox/jquery.fancybox-1.3.4.css" type="text/css" media="screen" />');
		document.write('<script type="text/javascript" src="scripts/fancybox/jquery.fancybox-1.3.4.pack.js"></script>');
		document.write('<script type="text/javascript" src="scripts/fancybox/fancyboxcall.js"></script>');
		document.write('<style type="text/css">#fancybox-left-ico {left: 20px; }');
		document.write('#fancybox-right-ico {  right: 20px;  left: auto; } </style> ');
		
//		<!-- Call folding/unfolding stuff -->
// 		See http://www.adipalaz.com/experiments/jquery/expand.html for more info
		document.write('<!--[if lte IE 6]><style type="text/css">h3 a, .demo {position:relative; height:1%}</style>--><![endif]--> ');
		document.write('<!--[if lte IE 6]><script type="text/javascript"> try { document.execCommand( "BackgroundImageCache", false, true); } catch(e) {};</script><![endif]-->');
		document.write('<!--[if !lt IE 6]><!-->');
		document.write('<script type="text/javascript" src="scripts/expand.js"></script>');
		document.write('<script type="text/javascript">$(function() {$("dt.expand").toggler();});</script>');
		document.write('<!--<![endif]-->');

// 		<!-- Call cycle stuff -->
// 		See http://jquery.malsup.com/cycle/ for more info
		document.write('<script type="text/javascript" src="http://malsup.github.com/chili-1.7.pack.js"></script>');
		document.write('<script type="text/javascript" src="scripts/jquery.cycle.all.js"></script>');
		document.write('<script type="text/javascript" src="scripts/cyclecall.js"></script>');
	}


//*********************************************************************


	function makeTitle() 
	{
		document.write('<title>Math 116, Fall 2020 -- ' +currentPage+ '</title>');	
	}

	
	function makeLogo()
	{
		document.write('<div id="logo">');
//		document.write('<hr width=100%>')
		document.write('<h1>Math 116: Calculus II</h1>');
		document.write('<h2>Fall 2020</h2>');
//		document.write('<hr width=100%>')
		document.write('</div>');
	}

	var Pages = new Array (
		new Array('Home','./'),
		new Array('Syllabus','syllabus.html'),
//		new Array('Calendar','calendar.html'),
		new Array('Lecture Outlines','lectureoutlines.html'),
		new Array('Homework','homework.html'),
		new Array('Quizzes','quizzes.html'),
		new Array('Tests','tests.html')
	);

	function mailScramble(address,suffix) { 
		var a,b,c,d,e;
 		a='<a href=\"mai';
 		b=address; 
 		c='\">'; 
 		a+='lto:'; 
 		b+='&#64;'; 
 		e='</a>';
 		b+=suffix;
 		b+='.e';
 		b+='du';
 		d=b;
 		document.write(a+b+c+d+e);
	}

	function toggleDiv(divid)
	{
		if (document.getElementById(divid).style.display == 'none') {
			document.getElementById(divid).style.display = 'block';
   		} else {
			document.getElementById(divid).style.display = 'none';
		}
	}
	
	function makeNavbar()
	{
		document.write('<div id="navbar">');
		document.write('<ul>');
		for(var i = 0; i < Pages.length; i++)
		{
			var page = Pages[i];
			if (currentPage == page[0]) {
				document.write('<li id="uberlink">');
			} else {
				document.write('<li>');
			}
			document.write('<a href="');
			document.write(level); 
			document.write(page[1]+'">'+page[0]);
			document.write('</a></li>');
		}
		document.write('</ul>');
		document.write('</div>');
	}
	
	function makeFooter()
	{
		document.write('<div id="footer">');
		document.write('<hr width=100%>')
		document.write('Fall 2020 -- <a href="http://palmer.wellesley.edu/~aschultz">Andrew Schultz</a>');
		document.write('</div>');
	
	}	
