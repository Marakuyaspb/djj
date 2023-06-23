function filterFabricButtons(){
	const currCat = document.getElementById('content_left');
    const collection = document.getElementById('collection');
    let currCollection = collection.className;
    let fabricButtons = document.getElementsByClassName('fabric-var');

/* about desctop */

   if(currCollection == 'consono'){
        for (let i_0 = 0; i_0 < fabricButtons.length; i_0++) {
            const classes = fabricButtons[i_0].classList;
              
            if (classes.contains('COSMIC_08')) {
                classes.add('d-none');
            } 
            else if (classes.contains('HARMONY_SILVER')) {
                classes.add('d-none');
            } 
            else if (classes.contains('JAZZ_08')) {
                classes.add('d-none');
            } 
            else if (classes.contains('VELUTTO_16')) {
                classes.add('d-none');
            }
        }
    }
    else if (currCollection == 'giros'){
        for (let i_1 = 0; i_1 < fabricButtons.length; i_1++) {
            const classes = fabricButtons[i_1].classList;
        
            if (classes.contains('JAZZ_01')) {
                classes.add('d-none');
            } 
            else if (classes.contains('JAZZ_08')) {
                classes.add('d-none');
            } 
            else if (classes.contains('VELUTTO_16')) {
                classes.add('d-none');
            } 
            else if (classes.contains('VELUTTO_32')) {
                classes.add('d-none');
            }
        }
    }
   else if (currCollection == 'nadwig'){
        for (let i_2 = 0; i_2 < fabricButtons.length; i_2++) {
            const classes = fabricButtons[i_2].classList;
              
            if (classes.contains('COSMIC_08')) {
                classes.add('d-none');
            } 
            else if (classes.contains('HARMONY_SILVER')) {
                classes.add('d-none');
            } 
            else if (classes.contains('PIXEL_FOREST')) {
                classes.add('d-none');
            } 
            else if (classes.contains('VELUTTO_16')) {
                classes.add('d-none');
            }
        }
    }
}