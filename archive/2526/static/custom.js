


$(document).ready(function() {

	$('.toggle').click(function(){

		// Hack to load iframe, otherwise MathJax issues
		var id = $(this).attr("data-target")
		var iframe = $("iframe"+id)
		if(iframe.attr("src")=="about:blank"){
			iframe.attr("src", iframe.data("src")); 
		}

		// Set bg color
		iframe.contents().find('body').css('background-color','rgba(255,255,255,0.2)')
	    iframe.on('load', function(){
	        $(this).contents().find('body').css('background-color','rgba(255,255,255,0.2)')
	    });

		// change the button text
	    $(this).find('span#txt').text(function(i,old){
	        return old=='Show' ?  'Hide' : 'Show';
	    });
	});

	$( "<img src='../../static/images/phy2039-logo.png' style='width: 400px; border: 0; box-shadow: none;'>" ).insertBefore( "#title-slide h1" );

	// $("iframe").each(function() {
	//      $(this).on('load', function(){
	//              var src = $(this).attr('src');
	//              $(this).contents().find('body').css('background-color','rgba(255,255,255,0.2)')
	//      });
	// });


	window.addEventListener('message', function(event) {
	    //alert('got a message');   
	     if (event.origin !== "https://mas-coursebuild.ncl.ac.uk"){
	        console.log('child source not trusted')
	        return;
	     }

	     var frames = document.getElementsByTagName('iframe');
	     for (var i = 0; i < frames.length; i++) {
	         if (frames[i].contentWindow === event.source) {
	         		var id = $(frames[i])[0].id
	               	//console.log('changing frame height for frame id ' + id)
	                var pass_data = JSON.parse(event.data);
	                $(frames[i])[0].style.height = parseInt(pass_data['documentHeight']+100) + "px";
	                
	             break;
	         }
	     }



	}, false );


});