

//-----------------------------------------------------------

// var showPlayerName = function (playerName) {
//     console.log("* " + playerName + " *");
// };

// var showPlayerHealth = function (playerName, playerHealth) {
//     console.log(playerName + " has health " + playerHealth);
// };

// var showPlayerPlace = function (playerName, playerPlace) {
//     console.log(playerName + " is in " + playerPlace);
// };

// var showLine = function (playerName) {
//     var line = "***********************************";
//     line = line.substring(0, playerName.length + 4);
//     console.log(line);
// };

// var showPlayerInfo = function (playerName, playerPlace, playerHealth) {
//     console.log("");
//     showLine(playerName);
//     showPlayerName(playerName);
//     showLine(playerName);
    
//     console.log("----------------------------");

//     showPlayerPlace(playerName, playerPlace);
//     showPlayerHealth(playerName, playerHealth);

//     console.log("----------------------------");
//     console.log("");
// };

// var player1 = {
//     name: "Kandra",
//     place: "The Dungeon of Doom",
//     health: 50
// };

// var player2 = {
//     name: "Dax",
//     place: "The Old Library",
//     health: 40
// };

// showPlayerInfo(player1.name, player1.place, player1.health);
// showPlayerInfo(player2.name, player2.place, player2.health);

//-----------------------------------------------------------

// sqrt = function (numberToSqrt) {
//     console.log("SqRt of " + numberToSqrt + " is " + Math.sqrt(numberToSqrt));
// }
// cube = function (numberToCube){
//     var result;
//     result = numberToCube * numberToCube * numberToCube;
//     console.log(numberToCube + " * " + numberToCube + " * " + numberToCube + " = " + result);
// }
// square = function (numberToSquare) {
//   var result;
//   result = numberToSquare * numberToSquare;
//   console.log(numberToSquare + " * " + numberToSquare + " = " + result);
// };
// sqrt(9);
// sqrt(999);
// sqrt(7482);
// console.log("------------------------------------")
// cube(3);
// cube(999);
// cube(45);
// console.log("------------------------------------")
// square(10);
// square(-2);
// square(1111);

//-----------------------------------------------------------

// var showMessage;
// var myMessage = "oioioi!";

// showMessage = function (message) {
// 	console.log("The message is: ");
//     console.log(message);
//     console.log("--------------------------------------")
// };

// showMessage("It's full of stars!");
// showMessage("Hello to Jason Isaacs");
// showMessage("Hello to Jason Isaacs and Stephen Fry");
// showMessage(myMessage);

//-----------------------------------------------------------

// var showMessage;
// message = "oi meu nome é bruce!";
// showMessage = function (message, message2, message3) {
// 	console.log("A mensagem no.1 é: " + message);
//     console.log("A mensagem no.2 é: " + message2);
//     console.log("A mensagem no.3 é: " + message3);
// };

// showMessage("testando 1, 2...", "Aparentemente funcionou", "Sou um genio da computacao");
// console.log(message);

//-----------------------------------------------------------

// var filme1;
// var filme2;
// var filme3;
// var filme;

// filme1 = {
//     atores : "Boninho e Zabumba",
//     diretor : "Jose Bezerra",
//     ano : 2017
// };
// filme2 = {
//     atores : "Mirestella e Fernanda Montenegro",
//     diretor : "Homem - Plutão",
//     ano : 2015
// };
// filme3 = {
//     atores : "Claudia Raia e Sergio Mallandro",
//     diretor : "Angelica",
//     ano : 2008
// };

// function mostraDadosDoFilme () {
//     console.log("")
//     console.log("----------------------------------");
//     console.log("Atores Principais: " + filme.atores);
//     console.log("Diretor: " + filme.diretor);
//     console.log("Ano: " + filme.ano);
//     console.log("----------------------------------");
// };
// filme = filme1;
// mostraDadosDoFilme();
// filme = filme2;
// mostraDadosDoFilme();
// filme = filme3;
// mostraDadosDoFilme();

//-----------------------------------------------------------

// var sale1;
// var sale2;
// var sale3;
// var sale;
// var calculateTax;
// var displaySale;

// sale1 = { price: 140, taxRate: 15 };
// sale2 = { price: 40, taxRate: 10 };
// sale3 = { price: 120, taxRate: 20 };

// calculateTax = function () {
// 	sale.tax = sale.price * sale.taxRate / 100;
// 	sale.total = sale.price + sale.tax;
// };
// displaySale = function () { 
//   console.log("price = $" + sale.price);
//   console.log("tax @ " + sale.taxRate + "% = $" + sale.tax);
//   console.log("total cost = $" + sale.total);
// };
// function calculateAndDisplay () {
//     calculateTax();
//     displaySale();
// };

// sale = sale1;
// calculateAndDisplay();
// sale = sale2;
// calculateAndDisplay();
// sale = sale3;
// calculateAndDisplay();

//-----------------------------------------------------------

// function total (a, b) {
//     resultado = a + b;
//     console.log (resultado);
// };
// total(10, 10);
// console.log (resultado);

//-----------------------------------------------------------

// var filmes;
// filmes = {
//     nome : ["A volta dos que nao se foram", "Tranças de um careca", "Poeira em alto mar"],
//     nota : ["10","9","4"],
//     diretor : ["Zezinho Perneta","Cuca Beludo","Joselito Boça"]
// };

// function mostraDados (indice) {
//     console.log("Nome: " + filmes.nome[indice] + ". Diretor: "+ filmes.diretor[indice]   + ". Nota: " + filmes.nota[indice]);
// };

// mostraDados(0);
// mostraDados(1);
// mostraDados(2);

//-----------------------------------------------------------

// var filmes;
// var indice;

// filmes = {
//     nome : ["A volta dos que nao se foram", "Tranças de um careca", "Poeira em alto mar"],
//     nota : ["10","9","4"],
//     diretor : ["Zezinho Perneta","Cuca Beludo","Joselito Boça"]
// };

// function mostraDados () {
//     console.log("Nome: " + filmes.nome[indice] + ". Diretor: "+ filmes.diretor[indice]   + ". Nota: " + filmes.nota[indice]);
// };

// indice = 0;
// mostraDados();
// indice = 1;
// mostraDados();
// indice = 2;
// mostraDados();

//-----------------------------------------------------------

// var filmes;
// var indice;
// filmes = {
//     nome : ["A volta dos que nao se foram", "Tranças de um careca", "Poeira em alto mar"],
//     nota : ["10","9","4"],
//     diretor : ["Zezinho Perneta","Cuca Beludo","Joselito Boça"]
// };
// indice = 0;
// console.log("Nome: " + filmes.nome[indice] + ". Diretor: "+ filmes.diretor[indice]   + ". Nota: " + filmes.nota[indice]);
// indice = 1;
// console.log("Nome: " + filmes.nome[indice] + ". Diretor: "+ filmes.diretor[indice]   + ". Nota: " + filmes.nota[indice]);
// indice = 2;
// console.log("Nome: " + filmes.nome[indice] + ". Diretor: "+ filmes.diretor[indice]   + ". Nota: " + filmes.nota[indice]);

//-----------------------------------------------------------

// var jogador;
// jogador = {
//    nome : 'Leo',
//    vida : 50,
//    score : 100,
//   };
// console.log('Parabens ' + jogador.nome + ', voce fez ' + jogador.score + ' pontos! voce terminou com ' + jogador.vida + ' de HP.');
// jogador.nome = 'Blebliu';
// jogador.peso = 150;
// console.log(jogador.nome);
// console.log(jogador.peso);
// jogador.peso = jogador.peso + 20