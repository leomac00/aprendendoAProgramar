import { random } from "./utils.js"; 

function getQuiz (){
    var i = 0;
    var score = 0;
    var questions = [
    { question: "7 x 8", answer: "56" },
    { question: "12 x 12", answer: "144" },
    { question: "5 x 6", answer: "30" },
    { question: "9 x 3", answer: "27" }];

    var getQuestion = function (){
        console.log('Question number: ' + (i + 1));
        return questions[i].question;
    };
    var checkAnswer = function (userAnswer){
        if (i >= questions.length){
            console.log('The quiz is already over, pal.') ;
        }else{
            if (userAnswer == questions[i].answer){
                score++;
                console.log('Congratulations! Your answer was correct, your score now is ' + score);
            }else{
                console.log('Shame on you! Your input was the incorrect one, TRY HARDER NEXT TIME!');
            }
        }
        i++
        return ;
    };
    var getScore = function (){
        return 'Your score is: ' + score + '. You still have ' + (questions.length - i) + ' tries.';
    };

    return{
        quizMe: getQuestion(),
        submit: checkAnswer,
        myScore: getScore()
    };
};

  
window.quiz = getQuiz(); // fazemos isto para criar uma variavel 'quiz' no escopo global par apdoer ser acessada no console para podermos executar os comandos da função
