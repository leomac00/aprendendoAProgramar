const canvas = document.getElementById('ttr');
const context = canvas.getContext('2d');
let texts = [];
let lettersTyped = []
let score = 0;
let missed = 0;
let speed = 3000;

for(i = 0; i < 24; i++){
    texts.push(createString(3));
}

function random (floor, ceil) {
    return Math.floor(Math.random() * ceil) + floor;
}

function createString(length) {
    var result           = '';
    var characters       = 'abcdefghijklmnopqrstuvwxyz';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(random(0, charactersLength));
    }
    return result;
}

function renderBG() {
    context.fillStyle = 'lightblue';
    context.fillRect(0, 0, canvas.width, canvas.height)
}

function renderString() {
    context.font = "30px Arial";
    context.fillStyle = "black";
    context.textAlign = "center";
    context.fillText(texts[random(0, texts.length)], random(15, canvas.width-15), random(15, canvas.height-15));   
}

function renderScore() {
    let message = 'Pontuação: ' + score;
    context.font = "30px Arial";
    context.fillStyle = "red";
    context.fillText(message, 100, 35);   

}

function textMO(event) {
    letterPressed = event.key;
    lettersTyped.push(letterPressed)

    if(lettersTyped.length == 3){
        result = lettersTyped[0] + lettersTyped[1] + lettersTyped[2];
        lettersTyped = []
        lettersTyped[0] = result

    }
    if(lettersTyped[0].length > 3){
        lettersTyped.splice(0)
    }

    console.log(lettersTyped)
}

document.addEventListener('keydown', textMO)


function playGame() {
    renderBG();
    renderString();
    renderScore();
    let scoreC = score;
    let textsC = texts


    for(i = 0; i < textsC.length; i++) {
        if (textsC[i] == lettersTyped){
            score++;
            texts.splice(i);
            speed -= 100;
        } 
    }
    if(scoreC == score){
        missed++;
    }

    if(missed == 10 || speed < 50) {
        clearInterval(game);
        alert('Game Over! :(\n Score: ' + score)
    }

    lettersTyped = [];
}

//play games
renderScore();
renderBG();
let game = setInterval(playGame,  speed)