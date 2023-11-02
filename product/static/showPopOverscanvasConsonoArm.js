function showPopOverscanvasConsonoArm(event){
       
        var canvasConsonoArm = document.getElementById("canvasConsonoArm");
        var ctx = canvasConsonoArm.getContext('2d');

      /*  console.log('Hey! You ll see armchair');*/

        const canvasConsonoArm_width = canvasConsonoArm.width = 1600;
        const canvasConsonoArm_heigh = canvasConsonoArm.height = 800;

      /* сделать эту штуку вариативной из массива */

        var pinStitchesConsonoArm = new Image();
        pinStitchesConsonoArm.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
        pinStitchesConsonoArm.onload = function(){
          ctx.imageSmoothingEnabled = false;
          ctx.drawImage(pinStitchesConsonoArm, 496, 533, 50, 50);
        }
        var pinPillowConsonoArm = new Image();
        pinPillowConsonoArm.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
        pinPillowConsonoArm.onload = function(){
          ctx.imageSmoothingEnabled = false;
          ctx.drawImage(pinPillowConsonoArm, 622, 415, 50, 50);
        }
        var pinFrontConsonoArm = new Image();
        pinFrontConsonoArm.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
        pinFrontConsonoArm.onload = function(){
          ctx.imageSmoothingEnabled = false;
          ctx.drawImage(pinFrontConsonoArm, 852, 550, 50, 50);
        }
        var pinBackConsonoArm = new Image();
        pinBackConsonoArm.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
        pinBackConsonoArm.onload = function(){
          ctx.imageSmoothingEnabled = false;
          ctx.drawImage(pinBackConsonoArm, 710, 470, 50, 50);
        }
        var pinPawConsonoArm = new Image();
        pinPawConsonoArm.src = 'http://temp.decona.ru/wp-content/uploads/2023/02/pin.svg';
        pinPawConsonoArm.onload = function(){
          ctx.imageSmoothingEnabled = false;
          ctx.drawImage(pinPawConsonoArm, 875, 734, 50, 50);
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
          console.log(mouse.x, mouse.y);

          if (mouse.x >= 496 && mouse.x <= 546 && mouse.y >= 533 && mouse.y <= 583) {
            popAboutStitchesConsonoArm.style.display = 'block';
          }
          else if (mouse.x >= 622 && mouse.x <= 672 && mouse.y >= 415 && mouse.y <= 465) {
            popAboutPillowConsonoArm.style.display = 'block';
          }
          else if (mouse.x >= 852 && mouse.x <= 902 && mouse.y >= 550 && mouse.y <= 600) {
            popAboutFrontConsonoArm.style.display = 'block';
          }
          else if (mouse.x >= 710 && mouse.x <= 760 && mouse.y >= 470 && mouse.y <= 520) {
            popAboutBackConsonoArm.style.display = 'block';
          }
          else if (mouse.x >= 875 && mouse.x <= 925 && mouse.y >= 734 && mouse.y <= 824) {
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