function adaptationWidth(){
	
/* Adaptation */
	const content_left = document.getElementById('content_left');
	const content_right = document.getElementById('content_right');
	const f_icons = document.getElementById('fabric_icons');


	/* Rectangles */

	if (content_left.classList.contains('arm' || 'poufl' || 'poufs')) {
  		content_left.classList.add('col-md-6');
  		content_right.classList.add('col-md-6');
  	} 


  	/* Left bigger */

	else if (content_left.classList.contains('cornerl' || 'str')) {
  		content_left.classList.add('col-md-8');
  		content_right.classList.add('col-md-4');
	} 


	/* Full */

	else if (content_left.classList.contains('mod1' || 'bed')) {
  		content_left.classList.add('col-md-12');
  		content_right.remove();
	}

	/* Without fabric icons */
	if (content_left.classList.contains('accessory' || 'table')) {
  		content_left.classList.add('col-md-6');
  		content_right.classList.add('col-md-6');
  		f_icons.remove();
  	} 
}