function headerHover(){
	let h = document.getElementById("header-hover-change");

	/* change background*/
/*
	h.addEventListener('mousemove', (event) => {
		h.classList.add("milk-white_bg");
	});
	h.addEventListener('mouseleave', (event) => {
		h.classList.remove("milk-white_bg");
	});
*/

/* change logo*/
	let logo = document.getElementsByClassName("navbar-brand");

	h.addEventListener('mousemove', (event) => {
		for (var i = 0; i < logo.length; i++) {
    		logo[i].classList.remove("white");
		};
	});
	h.addEventListener('mouseleave', (event) => {
		for (var i = 0; i < logo.length; i++) {
    		logo[i].classList.add("white");
		};
	});

/* change nav items */
	let nl = document.getElementsByClassName('nav-link');

	h.addEventListener('mousemove', (event) => {
		for (var i = 0; i < nl.length; i++) {
    		nl[i].classList.remove("white");
		};
	});
	h.addEventListener('mouseleave', (event) => {
		for (var i = 0; i < nl.length; i++) {
    		nl[i].classList.add("white");
		};
	});

/* change icons */
	let ih = document.getElementsByClassName('icon-header');

	h.addEventListener('mousemove', (event) => {
		for (var i = 0; i < ih.length; i++) {
    		ih[i].classList.remove("white");
		};
	});
	h.addEventListener('mouseleave', (event) => {
		for (var i = 0; i < ih.length; i++) {
    		ih[i].classList.add("white");
		};
	});


}

headerHover();
