function adaptationWidth(){
	
/* Adaptation */
	const content_left = document.getElementById('content_left');
	const content_right = document.getElementById('content_right');

	if (content_left.classList.contains("arm")) {
  		content_left.classList.add("col-md-8");
  		content_right.classList.add("col-md-4");
  	} 
	else if (content_left.classList.contains("str")) {
  		content_left.classList.add("col-md-8");
  		content_right.classList.add("col-md-4");
	} 
	else if (content_left.classList.contains("pouf")) {
  		content_left.classList.add("col-md-8");
  		content_right.classList.add("col-md-4");
	} 
	else if (content_left.classList.contains("corner")) {
  		content_left.classList.add("col-md-8");
  		content_right.classList.add("col-md-4");
	} 
	else if (content_left.classList.contains("bed")) {
  		content_left.classList.add("col-md-8");
  		content_right.classList.add("col-md-4");
	} 
	else if (content_left.classList.contains("k1r")) {
  		content_left.classList.add("col-md-8");
  		content_right.classList.add("col-md-4");
  		content_right.classList.remove("no-padding-right");
	}
	else if (content_left.classList.contains("pillow")) {
  		content_left.classList.add("col-md-6");
  		content_right.classList.add("col-md-6");
  		content_right.classList.remove("no-padding-right");
	}
}