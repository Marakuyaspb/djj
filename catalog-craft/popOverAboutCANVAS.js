function showPopOvers(event){
  var canvasBig = document.getElementById("canvasBig");
  var ctx = canvasBig.getContext('2d');

  const canvasBig_width = canvasBig.width = 1600;
  const canvasBig_heigh = canvasBig.height = 800;

/* сделать эту штуку вариативной из массива */

  var pinStitchesBig = new Image();
  pinStitchesBig.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
  pinStitchesBig.onload = function(){
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pinStitchesBig, 280, 400, 50, 50);
  }
  var pinPillowBig = new Image();
  pinPillowBig.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
  pinPillowBig.onload = function(){
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pinPillowBig, 370, 260, 50, 50);
  }
  var pinFrontBig = new Image();
  pinFrontBig.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
  pinFrontBig.onload = function(){
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pinFrontBig, 760, 470, 50, 50);
  }
  var pinBackBig = new Image();
  pinBackBig.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
  pinBackBig.onload = function(){
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pinBackBig, 890, 180, 50, 50);
  }
  var pinPawBig = new Image();
  pinPawBig.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
  pinPawBig.onload = function(){
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pinPawBig, 1070, 620, 50, 50);
  }

  canvasBig.style.width = canvasBig.offsetWidth + 'px';
  canvasBig.style.height = canvasBig.offsetHeight + 'px';

  let popAboutStitchesBig = document.getElementById('popAboutStitchesBig');     
  let popAboutPillowBig = document.getElementById('popAboutPillowBig');
  let popAboutFrontBig = document.getElementById('popAboutFrontBig');
  let popAboutBackBig = document.getElementById('popAboutBackBig');
  let popAboutPawBig = document.getElementById('popAboutPawBig');

  const mouse = {
    x:0,
    y:0,
    left: false,
    right: false,
    over: false,
  }; 

  canvasBig.addEventListener('mousemove', function(e) {
    const rect = canvasBig.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
    /*console.log(mouse.x, mouse.y);*/

    if (mouse.x >= 280 && mouse.x <= 330 && mouse.y >= 400 && mouse.y <= 450) {
      popAboutStitchesBig.style.display = 'block';
    }
    else if (mouse.x >= 370 && mouse.x <= 430 && mouse.y >= 260 && mouse.y <= 310) {
      popAboutPillowBig.style.display = 'block';
    }
    else if (mouse.x >= 760 && mouse.x <= 810 && mouse.y >= 470 && mouse.y <= 520) {
      popAboutFrontBig.style.display = 'block';
    }
    else if (mouse.x >= 890 && mouse.x <= 940 && mouse.y >= 180 && mouse.y <= 230) {
      popAboutBackBig.style.display = 'block';
    }
    else if (mouse.x >= 1070 && mouse.x <= 1120 && mouse.y >= 620 && mouse.y <= 670) {
      popAboutPawBig.style.display = 'block';
    }

    else {
      popAboutStitchesBig.style.display = 'none';
      popAboutPillowBig.style.display = 'none'; 
      popAboutFrontBig.style.display = 'none'; 
      popAboutFrontBig.style.display = 'none'; 
      popAboutBackBig.style.display = 'none'; 
      popAboutPawBig.style.display = 'none';   
    }
  });
}