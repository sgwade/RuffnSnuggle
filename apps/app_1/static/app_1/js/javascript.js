    const width = 64;
    const height = 64;
    const cycleLoop = [0,1,0,1];
    const movement_speed = 0.1;
    
    let currentLoopIndex = 0;
    let frameCount = 0;
    let positionX = 0; 
    let positionY = 356; 

    var sprite = new Image ();
    sprite.src = "images/fullspritesheet.png";
    sprite.onload = function(){
            init();
        };
    
    let canvas = document.querySelector('canvas');
    let ctx = canvas.getContext('2d');

    function drawFrame(frameX, frameY, canvasX, canvasY){
        ctx.drawImage(sprite, frameX * width, frameY * height, width, height, canvasX, canvasY, width, height);
    }

    function init(){
        window.requestAnimationFrame(walk);
        
    }

    function walk(){
        frameCount++;
        positionX += movement_speed;
        if(frameCount<15){
            window.requestAnimationFrame(walk);
            return;
        }
        frameCount=0;
        ctx.clearRect(0,0, canvas.width, canvas.height);
        drawFrame(cycleLoop[currentLoopIndex], 0, positionX, positionY);
        currentLoopIndex++;
        if (currentLoopIndex >= cycleLoop.length){
            currentLoopIndex = 0;
        }
        window.requestAnimationFrame(walk);
        }
