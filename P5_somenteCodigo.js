// //For ... of
//   for (let item of obj) {
//     item.display();
//     item.move();
//   };

//----------

// //Classes: exemplo setando o parametro 'size' das bolhas
// function setup() {
//     createCanvas(700, 500);
  
//     bubbles = {}
//     for (var i = 0; i < 50; i++) {
//       bubbles[i] = new Bubble(15); //O argumento passado aqui sera o argumento utilizado pelo constructor()
//     }
//   }
//   .
//   .
//   .
//   class Bubble {
//     constructor(tempSize) { 
//       var topSpeed = 10;
//       var minSpeed = 0.1;
//       this.x = random(width);
//       this.y = random(height);
//       this.xspeed = random(minSpeed, topSpeed);
//       this.yspeed = random(minSpeed, topSpeed);
//       this.size = tempSize;
//       this.r = random(255);
//       this.g = random(255);
//       this.b = random(255);
//         }
//   }

//----------

// //Classes:
// function setup() {
//     createCanvas(700, 500);
  
//     bubbles = {}
//     for (var i = 0; i < 50; i++) { // Cria-se 50 bolhas
//       bubbles[i] = new Bubble;
//     }
//   }
  
//   function draw() {
//     background(0);
//     for (var i = 0; i < 50; i++) { // excuta a funcao move() e show() para cada uma das 50 bolhas criadas
//       bubbles[i].move();
//       bubbles[i].show()
//     }
  
  
//   }
  
//   class Bubble {
//     constructor() { //Inicializa os parametros que o objeto pertencente a essa calsse terao
//       var topSpeed = 10;
//       var minSpeed = 0.1;
//       this.x = random(width);
//       this.y = random(height);
//       this.xspeed = random(minSpeed, topSpeed);
//       this.yspeed = random(minSpeed, topSpeed);
//       this.size = random(10, 25);
//       this.r = random(255);
//       this.g = random(255);
//       this.b = random(255);
//         }
  
//     move() { // funcao que a classe Bubble terá 
//       this.y += this.yspeed;
//       this.x += this.xspeed;
//       if (this.x > width || this.x < 0) {
//         this.xspeed = -this.xspeed
//       }
//       if (this.y > height || this.y < 0) {
//         this.yspeed = -this.yspeed
//       }
//     }
  
//     show() {
//       noStroke();
//       fill(this.r, this.b, this.b);
//       ellipse(this.x, this.y, this.size, this.size);
//     }
//   }
//----------

// // Desenha um Pirulito
// function setup() {
//     createCanvas(400, 400);
//   }
  
//   function draw() {
//     background(0);
//     lollipop(width/2, height/2, 100);
//     lollipop(50,50,50);
//   }
  
//   function lollipop(x, y, headSize) {
//     fill(0, 200, 255);
//     rect(x - 10, y , 20, 150);
    
//     fill(250, 0, 200);
//     ellipse(x, y, headSize, headSize);
//   }

//----------  

// //Bola que quica utilizando funcoes
// var ball = {
//     x: 50,
//     y: 50,
//     xspeed: 3,
//     yspeed: -4
//   }
  
//   function setup() {
//     createCanvas(400, 400);
//   }
  
//   function draw() {
//     background(0);
//     move(ball);
//     bounce(ball);
//     display(ball);
    
//   }
  
//   function move(ball) {
//     ball.x += ball.xspeed;
//     ball.y += ball.yspeed;
//   }
  
  
//   function bounce(ball) {
//     if (ball.x > width || ball.x < 0) {
//       ball.xspeed = -ball.xspeed;
//     }
  
//     if (ball.y > height || ball.y < 0) {
//       ball.yspeed = -ball.yspeed;
//     }
//   }
  
  
//   function display(ball) {
//     stroke(255);
//     strokeWeight(4);
//     noFill();
//     ellipse(ball.x, ball.y, 24, 24);
//   }

//----------

// //Desenha uma malha de Bolinhas
// var offset = 0;
// function setup() {
//   createCanvas(600, 400);
// }

// function draw() {
//   background(0);
//   noStroke();

//   // desenha uma malha
//   for (var x = 0; x <= width; x += 50) {
//     for (var y = 0; y <= height; y += 50) {
//       fill(random(127), 0, random(127));
//       ellipse(x + offset, y, 25, 25);
//     }
//   }      
// }

//----------

// //Loops for e while
// function setup() {
//     createCanvas(600, 400);
//   }
  
//   function draw() {
//     background(0);
//     var x = 0;
  
//     //desenha bolinhas de golfe na horizontal
//     while (x <= 600) {
//       fill(255);
//       ellipse(x, height / 2, 50, 50);
//       x += 50;
//     }
  
//     //desenha bolinhas de golfe na vertical
//     for (var y = 0; y <= height; y += 50) {
//       fill(255, 255, 0);
//       ellipse(width / 2, y, 50, 50);
//       y += 50;
//     }
//   }

//----------

// // Interruptor de luz
// var lightSwitch = false

// function setup() {
//   createCanvas(400, 400);
// }

// function draw() {

//   if (lightSwitch) {
//     background(255);
//   } else {
//     background(0);
//   }

//   rectMode(CENTER);
//   noFill();
//   strokeWeight(4);
//   stroke(127);
//     rect(width / 2, height / 2, 100, 100)
// }

// function mousePressed() {
//   if (mouseX < 250 && mouseX > 150 && mouseY < 250 && mouseY > 150) {
//      lightSwitch = !lightSwitch
//   }
// }

//----------

// //AND e OR
// function setup() {
//   createCanvas(400, 400);
// }

// function draw() {
//   background(220);
//   // OR
//   if (width < mouseX || height < mouseY) {
//     fill(255, 0, 0)
//   }
  
//   // AND
//   // if (200 < mouseX && 200 < mouseY) {
//   //   fill(0, 255, 0)
//   // } 
  
  
//   else {
//     fill(0, 0, 255)
//   }
//   ellipse(width / 2, height / 2, 150, 150)
// }

//----------

// //Bola que quica
// var x = 0;
// var y = 0;
// var speedx = 10;
// var speedy = 10;


// function setup() {
//   createCanvas(600, 400);
//   x = random(0, width / 2);
//   y = random(0, height / 2);
//   //background(0);
// }


// function draw() {
//   background(0);
  
//   ellipseMode(CENTER);
//   noFill();
//   stroke(255);
//   strokeWeight(4);
//   ellipse(x, y, 50, 50);

//   //Quicada em X
//   if (x < 0) {
//     speedx = -speedx;
//   } else if (x > width) {
//     speedx = -speedx;
//   }
//   // Quicada em Y
//   if (y < 0) {
//     speedy = -speedy;
//   } else if (y > height) {
//     speedy = -speedy;
//   }
  
//   y = y + speedy;
//   x = x + speedx;
// }

//----------

// // Expressoes Booleanas: IF/ELSE
// function setup() {
//   createCanvas(600, 400);
// };

// function draw() {
//   background(0);
//   stroke(255);
//   strokeWeight(4);
//   noFill();

//   //Inicio do bloco IF
//   if (mouseX > 300) {
//     fill(200, 0, 200);
//   };
//   // Fim do bloco IF

//   ellipse(width / 2, height / 2, 150, 150);
// };

//----------

// // Shapes & Drawing
// // Code! Programming with p5.js
// // The Coding Train / Daniel Shiffman
// // https://thecodingtrain.com/beginners/p5js/1.3-shapes-and-drawing.html
// // https://youtu.be/c3TeLi6Ns1E
// // https://editor.p5js.org/codingtrain/sketches/HJ1WjEPwQ

// function setup() {
//     createCanvas(400, 300);
//   }
  
//   function draw() {
//     background(220, 0, 200);
  
//     line(0, 50, 400, 300);
//     rectMode(CENTER);
//     rect(200, 150, 150, 150);
  
//   }