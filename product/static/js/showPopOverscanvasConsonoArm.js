function showPopOverscanvasConsonoArm(event){
  console.log(mouse.x, mouse.y);
  var canvasConsonoArm = document.getElementById("canvasConsonoArm");
  var ctx = canvasConsonoArm.getContext('2d');

  console.log('Hey! You ll see armchair');


  const canvasConsonoArm_width = canvasConsonoArm.width = 1600;
  const canvasConsonoArm_heigh = canvasConsonoArm.height = 800;

/* сделать эту штуку вариативной из массива */

  var pinStitchesConsonoArm = new Image();
  pinStitchesConsonoArm.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
  pinStitchesConsonoArm.onload = function(){
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pinStitchesConsonoArm, 0, 0, 50, 50);
  }
  var pinPillowConsonoArm = new Image();
  pinPillowConsonoArm.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
  pinPillowConsonoArm.onload = function(){
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pinPillowConsonoArm, 590, 260, 50, 50);
  }
  var pinFrontConsonoArm = new Image();
  pinFrontConsonoArm.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
  pinFrontConsonoArm.onload = function(){
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pinFrontConsonoArm, 760, 470, 50, 50);
  }
  var pinBackConsonoArm = new Image();
  pinBackConsonoArm.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
  pinBackConsonoArm.onload = function(){
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pinBackConsonoArm, 890, 180, 50, 50);
  }
  var pinPawConsonoArm = new Image();
  pinPawConsonoArm.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
  pinPawConsonoArm.onload = function(){
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pinPawConsonoArm, 1070, 620, 50, 50);
  }

  canvasConsonoArm.style.width = canvasConsonoArm.offsetWidth + 'px';
  canvasConsonoArm.style.height = canvasConsonoArm.offsetHeight + 'px';

  let popAboutStitchesConsonoArm = document.getElementById('popAboutStitchesConsonoArm');     
  let popAboutPillowConsonoArm = document.getElementById('popAboutPillowConsonoArm');
  let popAboutFrontConsonoArm = document.getElementById('popAboutFrontConsonoArm');
  let popAboutBackConsonoArm = document.getElementById('popAboutBackConsonoArm');
  let popAboutPawConsonoArm = document.getElementById('popAboutPawConsonoArm');

  const mouse = {
    x:0,
    y:0,
    left: false,
    right: false,
    over: false,
  }; 

  canvasConsonoArm.addEventListener('mousemove', function(e) {
    const rect = canvasConsonoArm.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
    /*console.log(mouse.x, mouse.y);*/

    if (mouse.x >= 0 && mouse.x <= 50 && mouse.y >= 0 && mouse.y <= 50) {
      popAboutStitchesConsonoArm.style.display = 'block';
    }
    else if (mouse.x >= 370 && mouse.x <= 430 && mouse.y >= 260 && mouse.y <= 310) {
      popAboutPillowConsonoArm.style.display = 'block';
    }
    else if (mouse.x >= 760 && mouse.x <= 810 && mouse.y >= 470 && mouse.y <= 520) {
      popAboutFrontConsonoArm.style.display = 'block';
    }
    else if (mouse.x >= 890 && mouse.x <= 940 && mouse.y >= 180 && mouse.y <= 230) {
      popAboutBackConsonoArm.style.display = 'block';
    }
    else if (mouse.x >= 1070 && mouse.x <= 1120 && mouse.y >= 620 && mouse.y <= 670) {
      popAboutPawConsonoArm.style.display = 'block';
    }

    else {
      popAboutStitchesConsonoArm.style.display = 'none';
      popAboutPillowConsonoArm.style.display = 'none'; 
      popAboutFrontConsonoArm.style.display = 'none'; 
      popAboutFrontConsonoArm.style.display = 'none'; 
      popAboutBackConsonoArm.style.display = 'none'; 
      popAboutPawConsonoArm.style.display = 'none';   
    }
  });
}
showPopOverscanvasConsonoArm()