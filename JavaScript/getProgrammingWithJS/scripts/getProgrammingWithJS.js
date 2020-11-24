import utils from './utils.js'

//----------

//     return {
//         go: function (direction) {
//             var place = player.getPlace();
//             var destination = place.getExit(direction);
//             if (destination !== undefined) {
//             player.setPlace(destination);
//             render();
//             return "";
//             } else {
//             return "*** There is no exit in that direction ***";
//             }
//             },
//         get: function() {
//           var place = player.getPlace();
//           var item = place.getLastItem();
//           player.addItem(item);
//           render();
//           return "";
//         }
//       };

// ----------

// return {
//     go: function(direction) {
//       var place = player.getPlace();
//       var destination = place.getExit(direction);
//       player.setPlace(destination);
//       render();
//       return "";
//     },
//     get: function() {
//       var place = player.getPlace();
//       var item = place.getLastItem();
//       player.addItem(item);
//       render();
//       return "";
//     }
//   };

//----------

// //no cheating quiz
// var getQuiz = function() {
//     var score = 0,
//       qIndex = 0,
//       inPlay = true,
//       questions,
//       next,
//       getQuestion,
//       checkAnswer,
//       getHint,
//       submit;
  
//     questions = [{
//         question: "What is the highest mountain in the world?",
//         answer: "Everest",
//         hint: "___rest"
//       },
//       {
//         question: "What is the highest mountain in Scotland?",
//         answer: "Ben Nevis",
//         hint: "_en __vis"
//       }
//     ];
  
//     next = function() {
//       qIndex = qIndex + 1;
  
//       if (qIndex >= questions.length) {
//         inPlay = false;
//         console.log("You have finished the quiz.");
//       }
//     };
  
//     getQuestion = function() {
//       if (inPlay) {
//         return questions[qIndex].question;
//       } else {
//         return "You have finished the quiz.";
//       }
//     };
  
//     checkAnswer = function(userAnswer) {
//       if (userAnswer === questions[qIndex].answer) {
//         console.log("Correct!");
//         score = score + 1;
//       } else {
//         console.log("No, the answer is " + questions[qIndex].answer);
//       }
//     };
  
//     getHint = function() {
//       return console.log(questions[qIndex].hint);
//     };
  
//     submit = function(userAnswer) {
//       var message = "You have finished the quiz.";
  
//       if (inPlay) {
//         checkAnswer(userAnswer);
//         next();
//         message = "Your score is " + score + " out of " + qIndex;
//       }
  
//       return message;
//     };
  
//     return {
//       quizMe: getQuestion,
//       submit: submit,
//       helpMe: getHint
//     };
//   };
  
//   var quiz = getQuiz()

//----------

// //Adivinhe numero - com feedback
// var guessTheNumber = function() {
//     let rightNumber = Math.floor(Math.random() * 10);
//   //   console.log(rightNumber);
//     return function(guessedNumber) {
//       if (guessedNumber === rightNumber) {
//         console.log('You guessed correctly!');
//       } else if (guessedNumber > rightNumber) {
//         console.log('Wrong. Number too high.');
//       } else if (guessedNumber < rightNumber) {
//         console.log('Wrong. Number too low.');
//       }
//     };
//   };
//   var guess = guessTheNumber();

//----------

// //Adivinhe numero
// var guessTheNumber = function() {
//     let rightNumber = Math.floor(Math.random() * 10);
//   //   console.log(rightNumber);
//     return function(guessedNumber) {
//       if (guessedNumber === rightNumber) {
//         console.log('You guessed correctly!');
//       } else {
//         console.log('Wrong number, try again.');
//       }
//     };
//   };
//   var guess = guessTheNumber();

//----------

// //Condicoes
// let hello = 'Hello'
// if (hello === 'Hello'){
//     console.log('Hello World!')
// } else {
//     console.log('Not hello to you, sir')
// }

//----------

// //segunraça de dados - parametros dentro de funcoes
// var Person = function(name, age, pin = 123456) {
//     this.name = name;
//     this.age = age;
//     var pinNumber = pin;
//     this.showPin = function() {
//       return 'pin: ' + pinNumber;
//     }
//   }
  
//   var leo = new Person('leo', 25);

//----------

// // The Player constructor - user info hidden

// var Player = function (name, health) {
//     var newLine = spacer.newLine();
//     var items = [];
//     var place = null;


//     var getNameInfo = function () {
//         return name;
//     };

//     var getHealthInfo = function () {
//         return "(" + health + ")";
//     };

//     var getItemsInfo = function () {
//         var itemsString = "Items:" + newLine;
       
//         items.forEach(function (item, i) {
//             itemsString += "   - " + item + newLine;
//         });

//         return itemsString;
//     };
  
//     var getTitleInfo = function () {
//         return getNameInfo() + " " + getHealthInfo();
//     };

//     var getInfo = function () {
//         var info = spacer.box(getTitleInfo(), 40, "*");
//         info += "  " + getItemsInfo();
//         info += spacer.line(40, "*");
//         info += newLine;

//         return info;
//     }; 


//     this.addItem = function (item) {
//         items.push(item);
//     };
  
//     this.setPlace = function (destination) {
//         place = destination;
//     };
    
//     this.getPlace = function () {
//         return place;
//     };

//     this.showInfo = function (character) {
//         console.log(getInfo(character));
//     };
// };


//----------

// // The Player constructor - user can manipulate player info

// var Player = function (name, health) {
//     var newLine = spacer.newLine();
    
//     this.name = name;
//     this.health = health;
//     this.items = [];
//     this.place = null;
  
//     this.addItem = function (item) {
//       this.items.push(item);
//     };
  
//     this.getNameInfo = function () {
//       return this.name;
//     };
  
//     this.getHealthInfo = function () {
//       return this.name + " has health " + this.health;
//     };
  
//     this.getPlaceInfo = function () {
//       return this.name + " is in " + this.place.title;
//     };
  
//     this.getItemsInfo = function () {
//       var itemsString = "Items:" + newLine;
         
//       this.items.forEach(function (item, i) {
//         itemsString += "   - " + item + newLine;
//       });
  
//       return itemsString;
//     };
  
//     this.getInfo = function (character) {  
//       var place = this.getPlaceInfo();
//       var health = this.getHealthInfo();
//       var longest = Math.max(place.length, health.length) + 4;
  
//       var info = spacer.box(this.getNameInfo(), longest, character);
//       info += spacer.wrap(place, longest, character);
//       info += newLine + spacer.wrap(health, longest, character);
//       info += newLine + spacer.line(longest, character);
  
//       info += newLine;
//       info += "  " + this.getItemsInfo();
//       info += newLine;
//       info += spacer.line(longest, character);
//       info += newLine;
  
//       return info;
//     }; 
  
//     this.showInfo = function (character) {
//       console.log(this.getInfo(character));
//     };
//   };
  

//----------

// //Escondendo propriedades em escopos locais
// var getQuiz = function () {
//     var qIndex = 0;
//     var questions = [
//         {
//             question: "What is the highest mountain in the world?",
//             answer: "Everest"
//         },
//         {
//             question: "What is the highest mountain in Scotland?",
//             answer: "Ben Nevis"
//         },
//         {
//             question: "How many munros are in Scotland?",
//             answer: "284"
//         }
//     ];

//     return {
//         quizMe : function () {
//             return questions[qIndex].question;
//         },

//         showMe : function () {
//             return questions[qIndex].answer;
//         },

//         next : function () {
//             qIndex = qIndex + 1;
//             return "Ok";
//         },
        
//         showIndex : function () {
//             console.log("You're in question number: " + qIndex)
//     }
//     };
// };

// var quiz = getQuiz();

//----------

// //Contador seguro
// var getCounter = function () {
//     var counter = 0; //Agora a variavel count está dentro de uma funcao e nao pode ser acessada no escopo global, nao podendo ser alterada pelo usuario
    
//     var countUpBy1 =  function () {
//       counter = counter + 1;
//       return counter;
//     };
    
//     return countUpBy1;
//   };
  
//   var count = getCounter();

//----------

// // Contador nao seguro
// var counter = 0; //Sendo a variavel global, o usuario pode acessa-la e altera-la

// var count = function () {
//   counter = counter + 1;
//   return counter;
// };

//----------

// //Exemplo de criacao de saidas para lugares
// var Place = function (title, description) {
//     this.title = title;
//     this.exits = {};

//     this.addExit = function (direction, exit) {
//         this.exits[direction] = exit;
//     };

//     this.showExits = function () {  
//         console.log("Exits from " + this.title + ":");
  
//         Object.keys(this.exits).forEach(function (key) {
//             console.log(key);
//         });
//     };
// };

// var library = new Place("The Old Library");
// var kitchen = new Place("The Kitchen");
// var garden = new Place("The Kitchen Garden");

// kitchen.addExit("south", library);
// kitchen.addExit("west", garden);
// library.addExit("north",kitchen);
// garden.addExit("east",kitchen);

// kitchen.showExits();

//----------

// //Criando e Acessando lugares do jogo com bracket notation
// var Place = function (title) {
//     this.title = title;  
// };

// var kitchen = new Place("The Kitchen");
// var dungeon = new Place("The Dungeon");
// var hall = new Place("The entrance hall");
// var basement = new Place("The Basement");

// var exits = {};

// exits["north"] = kitchen;
// exits["the trapdoor"] = dungeon;
// exits["south"] = hall;
// exits["west"] = basement;

// var keys = Object.keys(exits);

// keys.forEach(function (key) {
//     console.log(key + " goes to " + exits[key].title);
// });

//----------

// //Contador de letras
// var letters = {};
// var tweetText = tweets.join(""); //Or just use " " o separate between words.
// tweetText = tweetText..toLowerCase();
// var tweetLetters = tweetText.split(""); //Or just use " " o separate between words.
  
// tweetLetters.forEach(function (letter) { //First we assign every letter/word the value 0
//     letters[letter] = 0;
// });

// tweetLetters.forEach(function (letter) { //Then when we find it again we add 1 to its property
//     letters[letter] += 1;
// });

// console.log(letters);

//----------

// // Como acessar valores de objetos 
// var ages = {
//     "Kandra Smith" : 56,
//     "Dax Aniaku"   : 21,
//     "Blinky"       : 36,
//     "Leo"          : 25,
//     };

// var keys = Object.keys(ages);

// ages["Nicolly"] = 24;
// ages.gato = 11;

// keys.forEach(function (key) {
//   console.log(key + ", " + ages[key] + ", Name Lenght: " + key.length);
//   console.log("----------");
// });

//----------

// //Demonstraçao de keys sendo strings
// var objeto = {};
// objeto["minas gerais"] = "Deu certo!";
// objeto["espaço 1"] = "Também deu certo!";
// console.log(objeto);

//----------

// var spacer = {
//   blank: function () {
//     return "";
//   },

//   newLine: function () {
//     return "\n";
//   },

//   line: function (length, character) {
//     var longString = "****************************************";
//     longString += "----------------------------------------";
//     longString += "========================================";
//     longString += "++++++++++++++++++++++++++++++++++++++++";
//     longString += "                                        ";

//     length = Math.max(0, length);
//     length = Math.min(40, length);
//     return longString.substr(longString.indexOf(character), length);
//   },
  
//   wrap : function (text, length, character) {
//     var padLength = length - text.length - 3;
//     var wrapText = character + " " + text;      
//     wrapText += spacer.line(padLength, " ");
//     wrapText += character;
//     return wrapText;
//   },

//   box: function (text, length, character) {
//     var boxText = spacer.newLine();
//     boxText += spacer.line(length, character) + spacer.newLine();
//     boxText += spacer.wrap(text, length, character) + spacer.newLine(); 
//     boxText += spacer.line(length, character) + spacer.newLine();
//     return boxText;
//   }
// };


// // The Place constructor

// var Place = function (title, description) {
//     var newLine = spacer.newLine();
  
//     this.title = title;
//     this.description = description;
//     this.items = [];
//     this.exits = [];
  
//     this.getItemsInfo = function () {
//         var itemsString = "Items: " + newLine;
//         this.items.forEach(function (item) {
//             itemsString += "   - " + item;
//             itemsString += newLine;
//         });
//         return itemsString;
//     };
  
//     this.getExitsInfo = function () {
//         var exitsString = "Exits from " + this.title;
//         exitsString += ":" + newLine;
        
//         this.exits.forEach(function (exit) {
//             exitsString += "   - " + exit.title;
//             exitsString += newLine;
//         });
      
//         return exitsString;
//     };

//     this.getTitleInfo = function () {
//         return spacer.box(
//             this.title,
//             this.title.length + 4,
//             "="
//         );
//     };

//     this.getInfo = function () {
//         var infoString = this.getTitleInfo();
//         infoString += this.description;
//         infoString += newLine + newLine;
//         infoString += this.getItemsInfo() + newLine;
//         infoString += this.getExitsInfo();
//         infoString += spacer.line(40, "=") + newLine;
//         return infoString;
//     };

  
//     this.showInfo = function () {
//         console.log(this.getInfo());
//     };

//     this.addItem = function (item) {
//         this.items.push(item);
//     };
  
//     this.addExit = function (exit) {
//         this.exits.push(exit);
//     };
// };


// // The Player constructor

// var Player = function (name, health) {
//   var newLine = spacer.newLine();
  
//   this.name = name;
//   this.health = health;
//   this.items = [];
//   this.place = null;

//   this.dropItem = function () {
//     this.items.pop();
//   };
//   this.addItem = function (item) {
//     this.items.push(item);
//       };

//   this.getNameInfo = function () {
//     return this.name;
//   };

//   this.getHealthInfo = function () {
//     return this.name + " has health " + this.health;
//   };

//   this.getPlaceInfo = function () {
//     return this.name + " is in " + this.place.title;
//   };

//   this.getItemsInfo = function () {
//     var itemsString = "Items:" + newLine;
       
//     this.items.forEach(function (item, i) {
//       itemsString += "   - " + item + newLine;
//     });

//     return itemsString;
//   };

//   this.getInfo = function (character) {  
//     var place = this.getPlaceInfo();
//     var health = this.getHealthInfo();
//     var longest = Math.max(place.length, health.length) + 4;

//     var info = spacer.box(this.getNameInfo(), longest, character);
//     info += spacer.wrap(place, longest, character);
//     info += spacer.newLine() + spacer.wrap(health, longest, character);
//     info += newLine + spacer.line(longest, character);

//     info += newLine;
//     info += "  " + this.getItemsInfo();
//     info += newLine;
//     info += spacer.line(longest, character);
//     info += newLine;

//     return info;
//   }; 

//   this.showInfo = function (character) {
//     console.log(this.getInfo(character));
//   };
// };


// // Testing Player

// var library = new Place(
//     "The Old Library",
//     "You are in a library. Dusty books line the walls."
// );

// var player1 = new Player("Kandra", 50);
// player1.place = library;
// player1.addItem("a rusty key");
// player1.addItem("The Sword of Doom");

// player1.showInfo("=");


// //----------

// //Criador de lugares para o jogo, exemplo do livro utilizando funcoes já criadas para formatacao de textos.
// // The spacer namespace

// var spacer = {
//     blank: function () {
//       return "";
//     },
  
//     newLine: function () {
//       return "\n";
//     },
  
//     line: function (length, character) {
//       var longString = "****************************************";
//       longString += "----------------------------------------";
//       longString += "========================================";
//       longString += "++++++++++++++++++++++++++++++++++++++++";
//       longString += "                                        ";
  
//       length = Math.max(0, length);
//       length = Math.min(40, length);
//       return longString.substr(longString.indexOf(character), length);
//     },
    
//     wrap : function (text, length, character) {
//       var padLength = length - text.length - 3;
//       var wrapText = character + " " + text;      
//       wrapText += spacer.line(padLength, " ");
//       wrapText += character;
//       return wrapText;
//     },
  
//     box: function (text, length, character) {
//       var boxText = spacer.newLine();
//       boxText += spacer.line(length, character) + spacer.newLine();
//       boxText += spacer.wrap(text, length, character) + spacer.newLine(); 
//       boxText += spacer.line(length, character) + spacer.newLine();
//       return boxText;
//     }
//   };
  
  
//   // The Place constructor
  
//   var Place = function (title, description) {
//       var newLine = spacer.newLine();
    
//       this.title = title;
//       this.description = description;
//       this.items = [];
//       this.exits = [];
    
//       this.getItemsInfo = function () {
//           var itemsString = "Items: " + newLine;
//           this.items.forEach(function (item) {
//               itemsString += "   - " + item;
//               itemsString += newLine;
//           });
//           return itemsString;
//       };
    
//       this.getExitsInfo = function () {
//           var exitsString = "Exits from " + this.title;
//           exitsString += ":" + newLine;
          
//           this.exits.forEach(function (exit) {
//               exitsString += "   - " + exit.title;
//               exitsString += newLine;
//           });
        
//           return exitsString;
//       };
  
//       this.getTitleInfo = function () {
//           return spacer.box(
//               this.title,
//               this.title.length + 4,
//               "="
//           );
//       };
  
//       this.getInfo = function () {
//           var infoString = this.getTitleInfo();
//           infoString += this.description;
//           infoString += newLine + newLine;
//           infoString += this.getItemsInfo() + newLine;
//           infoString += this.getExitsInfo();
//           infoString += spacer.line(40, "=") + newLine;
//           return infoString;
//       };
  
    
//       this.showInfo = function () {
//           console.log(this.getInfo());
//       };
  
//       this.addItem = function (item) {
//           this.items.push(item);
//       };
    
//       this.addExit = function (exit) {
//           this.exits.push(exit);
//       };
//   };
  
  
//   // Test the Place constructor
  
//   var library = new Place(
//       "The Old Library",
//       "You are in a library. Dusty books line the walls."
//   );
  
//   var kitchen = new Place(
//       "The Kitchen",
//       "You are in the kitchen. There is a disturbing smell."
//   );
  
//   var hall = new Place(
//       "The Main Hall",
//       "You are in a large hall. It is strangely empty."
//   );
  
//   library.addItem("a rusty key");
//   library.addExit(kitchen);
//   library.addExit(hall);
  
//   library.showInfo();

//----------

// //Criador de lugares para o jogo, exemplo próprio

// //Criador de Lugar
// var Lugar = function (nome, descricao) {
//     this.nome = nome;
//     this.descricao = descricao;
//     this.items = [];
//     this.saidas = [];

//     this.informacoes = function () {
//         var informacoes = 'Local: ' + this.nome + '.\n';
//         informacoes += 'Descricao: ' + this.descricao + '.\n';
//         informacoes += 'Itens: ' + this.items.join('; \n       ') + '.\n';
//         informacoes += 'Saidas: ' + this.saidas + '.\n';
//         console.log(informacoes);
//     };

//     this.addItem = function(item) {
//         this.items.push(item);
//     };

//     this.addSaida = function(saida) {
//         this.saidas.push(saida);
//     };
// };

// var salao = new Lugar ('Salao', 'Um salao cheio de estatuas e quadros. Poeira se amontoa nos cantos, parece que ninguem vive aqui há anos.');
// salao.addItem('Lanterna');
// salao.addItem('Tocha');
// salao.addSaida('Cozinha');

// salao.informacoes();

//----------

// // Quiz()
// var Quiz = function (pergunta, resposta) {
//     this.pergunta = pergunta;
//     this.resposta = resposta;
//     this.opcoes = [];
    
//     this.addOpcao = function (opcao) {
//         this.opcoes.push(opcao);
//     };
//     this.mostrarQuiz = function () {
//         console.log(this.pergunta);
//         this.opcoes.forEach( function (opcao, i) {
//             console.log("(" + (i+1) + ") " + opcao);
//         }) ;
//     };
// };

// var questao1 = new Quiz("Qual o animal que come com o rabo?",
//                         "Todos.");
// questao1.addOpcao("Todos.");
// questao1.addOpcao("Cachorro.");
// questao1.addOpcao("Gato.");
// questao1.addOpcao("Sapato.");

// questao1.mostrarQuiz();

//----------

// var item1 = new Planet("Jupiter", 5, "Gas Giant");
// console.log(item1 instanceof Planet);

//----------

// //Mais um exemplo de como modificar e incluir parametros em objetos:
// var Item = function(name, quantity){
//     this.name = name; 
//     this.quantity = quantity;
//     this.raridade = [];
//     this.showItem = function(){
//         console.log('Item: ' + name + '; quantidade: ' + quantity);
//     };
//     this.addRar = function (rar){
//         this.raridade.unshift(rar);
//     }
// };

// var itemTeste = new Item('Garrafas de água',5); 
// itemTeste.showItem(); 

//----------

// // Criando um novo objeto utilizando uma funcao com 'new' e 'this'
// var Item = function(name, quantity){
//     this.name = name; //cria-se usando o this para atribuir os valores ao objeto vazio criado pelo 'new'
//     this.quantity = quantity;
    
//     this.showItem = function(){
//         console.log('Item: ' + name + '; quantidade: ' + quantity);
//     };
// };

// var itemTeste = new Item('Garrafas de água',5); //Usa-se o new para que o JS entenda que estamos querendo criar um objeto vazio novo para a variavel em questao.
// itemTeste.showItem(); // Exemplo de acesso da funcao 'showItem()' criada pela funcao 'Item()'

//----------

// // Ideia geral de como fazer uma funcao que cria objetos:
// var buildPlanet = function (name, position, type) {
//     var planet = {}; // You create an empty object
//     planet.name = name; // Assign properties
//     planet.position = position; // Assign properties
//     planet.type = type; // Assign properties
//     return planet; // You return the object
//     };

//----------

// // métodos em objetos:
// var buildPlanet = function (name, position, type) {
//     var planet = {};
  
//     planet.name = name;
//     planet.position = position;
//     planet.type = type;

//     planet.showPlanet = function () {
//         var info = planet.name;
//         info += ": planet " + planet.position;
//         info += " - " + planet.type;
//         console.log(info);
//     };
  
//     return planet;
// };

// var planet1 = buildPlanet(
//     "Jupiter",
//     5,
//     "Gas Giant"
// );

// planet1.showPlanet();

//----------

// var spacer = {
//     blank: function () {
//       return "";
//     },
  
//     newLine: function () {
//       return "\n";
//     },
  
//     line: function (length, character) {
//       var longString = "****************************************";
//       longString += "----------------------------------------";
//       longString += "========================================";
//       longString += "++++++++++++++++++++++++++++++++++++++++";
//       longString += "                                        ";
  
//       length = Math.max(0, length);
//       length = Math.min(40, length);
//       return longString.substr(longString.indexOf(character), length);
//     },
    
//     wrap : function (text, length, character) {
//       var padLength = length - text.length - 3;
//       var wrapText = character + " " + text;      
//       wrapText += spacer.line(padLength, " ");
//       wrapText += character;
//       return wrapText;
//     },
  
//     box: function (text, length, character) {
//       var boxText = spacer.newLine();
//       boxText += spacer.line(length, character) + spacer.newLine();
//       boxText += spacer.wrap(text, length, character) + spacer.newLine(); 
//       boxText += spacer.line(length, character) + spacer.newLine();
//       return boxText;
//     }
//   };
  
  
//   // Player display code
  
//   var getPlayerName = function (player) {
//     return player.name;
//   };
  
//   var getPlayerHealth = function (player) {
//     return player.name + " has health " + player.health;
//   };
  
//   var getPlayerPlace = function (player) {
//     return player.name + " is in " + player.place;
//   };
  
//   var getPlayerItems = function (player) {
//     var itemsString = "Items:" + spacer.newLine();
  
//     player.items.forEach(function (item,i) {
//       itemsString += "   - " + "(" +(i+1) + ") " + item + spacer.newLine();
//     });
    
//     return itemsString;
//   };
  
//   var getPlayerInfo = function (player, character) {  
//     var place = getPlayerPlace(player);
//     var health = getPlayerHealth(player);
//     var longest = Math.max(place.length, health.length) + 4;
  
//     var info = spacer.box(getPlayerName(player), longest, character);
//     info += spacer.wrap(place, longest, character);
//     info += spacer.newLine() + spacer.wrap(health, longest, character);
//     info += spacer.newLine() + spacer.line(longest, character);
    
//     info += spacer.newLine();
//     info += "  " + getPlayerItems(player);
//     info += spacer.newLine();
//     info += spacer.line(longest, character);
    
//     info += spacer.newLine();
  
//     return info;
//   };
  
//   var showPlayerInfo = function (player, character) {
//     console.log(getPlayerInfo(player, character));
//   };
  
//   var showItem = function (player, itemNumber){
//       return (player.items[itemNumber])
//   };
  
//   var addItem = function (player, item){
//       player.items.push(item);
//       return "Item added to inventory!"
//   };
  
//   // Create a player
  
//   var player1 = {
//     name: "Kandra",
//     place: "The Dungeon of Doom",
//     health: 50,
//     items : ["a trusty lamp"]
//   };
  
//   showPlayerInfo(player1, "="); 
  
//   player1.items.push("a rusty key"); 
  
//   showPlayerInfo(player1, "*"); 
  

//----------

// var displayQuestion = function (questionArray){
//     var options = [ "A", "B", "C", "D", "E" ];
//     questionArray.forEach(function (item,i){ //Aqui o programa vai correr por cada questao no array de questoes passado e primeiramente imprimir qual é a pergunta
//         console.log('Question No.' + (i+1))
//         console.log(item.question)
//         item.answers.forEach(function (answer,j){ // Aqui o programa ira correr a lista de respostas que fica armazenada em '.answers' de cada objeto e imprimir a opcao correspondetne baseada no indice de cada uma e a resposta correspondente.
//             console.log(options[j] + ' - ' + answer)
//         })
//         console.log('\n')
//     })
// }
// var question1 = {
//     question : "What is the capital of France?",
//     answers : [
//       "Bordeaux",
//       "F",
//       "Paris",
//       "Brussels"
//     ],
//     correctAnswer : "Paris"
//   };
// var question2 = {
//     question : "What is the capital of Russia?",
//     answers : [
//       "Bordeaux",
//       "F",
//       "Paris",
//       "Moscow"
//     ],
//     correctAnswer : "Moscow"
//     };
// var questions = [question1, question2];
// displayQuestion(questions);

//----------

// [ "Dax", "Jahver", "Kandra" ].forEach(function (item, index, wholeArray) {
//     console.log("Item: " + item);
//     console.log("Index: " + index);
//     console.log("Array: " + wholeArray);
//   });

//----------

// var getTotalBill = function (itemList) {
// 	var total = 0;
// // a seguir ele vai pegar a lista que estiver como argumento para executar o que segue.
// 	itemList.forEach(function (item) { // usando apenas um parametro na funcao o forEach vai pegar apenas seu primeiro argumento que é o de elemento, no caso ele vai pegar um dos elementos de cada vez
// 		total += item.cost * item.number; // para cada elemento ele vai multiplicar o '.cost' pelo '.number' e somar na variavel 'total'
// 	});

// 	return total; // e vai devolver ao programa o valor da variavel 'total'
// };

// var items = [{cost:1 ,number:10},
//              {cost:2 ,number:5},
//              {cost:3 ,number:3},
//              {cost:4 ,number:2},
//              {cost:5 ,number:1}]


// console.log('Soma dos custos: ' + getTotalBill(items));

//----------
// // contando o total de letra usando o forEach
// var items;
// var showInfo;
// var total = 0;
// items = [
//   "The Pyramids",
//   "The Grand Canyon",
//   "Bondi Beach"
// ];

// showInfo = function (item, index, array) {
//     total += array[index].length;
//     console.log(item);
//     return total;
// };

// items.forEach(showInfo);
// console.log(total);

//----------

// // Exemplo de ForEach()
// var items;
// var showInfo;

// items = [
//   "The Pyramids",
//   "The Grand Canyon",
//   "Bondi Beach",
//   "Ubatuba"
// ];

// showInfo = function (itemToShow) {
//     var num = items.length;
//     var letters = 0;
//     for (var i = 0 ; i < num; i++){
//         console.log(itemToShow[i]);
//         console.log("There are " + itemToShow[i].length + " letters in this item");
//         console.log("----------------------------------");
//         letters += itemToShow[i].length;
//     };
//     console.log("There are " + letters + " letters in total")
// };

// showInfo(items)

//----------

// // Exemplo de métodos em arrays
// var items = [];
// var item = "The Pyramids";
// var removed;

// items.push(item);
// items.push("The Grand Canyon");
// items.push("Bondi Beach");
// items.push("Ubatuba","Pindamonhangaba","Itaquaquecetuba");

// console.log("Aqui está a lista de items depois dos 3 primeiros pushes: " + items);

// items[0] = "Fernando de Noronha"
// removed = items.pop();

// console.log("Poping " + removed + " and adding " + items[0]);
// console.log("Mostrando o restante da lista usando o 'join': " + items.join(" and "));

//----------

// var getVisitorReport = function (visitorArray, dayInWeek) {
//     var days = ["Segunda-Feira",
//                 "Terça-Feira",
//                 "Quarta-Feira",
//                 "Quinta-Feira",
//                 "Sexta-Feira"
//                ];
//     var index = dayInWeek - 1;
//     var visitorReport; // Perceba que aqui é criada a variavel para depois montar, dessa forma o codigo fica mais organizado.
//     visitorReport = "Houveram ";
//     visitorReport += visitorArray[index];
//     visitorReport += " acessos na ";
//     visitorReport += days[index];
//     return visitorReport;
// };

// var visitors = [111,222,333,444,555]; //Aqui está representado a quantidade de visitantes por dia.

// var day = 2; //Terça-Feira.
// var report = getVisitorReport(visitors, day);

// console.log(report);

//----------

// // Organização: este codigo organiza lugares para visitar utilizando arrays
// var lugar1 = {nome: "Belo Horizonte", estado: "Minas Gerais"};
// var lugar2 = {nome: "Catanduva", estado: "Sao Paulo"};
// var lugar3 = {nome: "Ilha das Couves", estado: "Sao Paulo"};

// var esseAno = [lugar1, lugar2];
// var proximoAno = [lugar3];
                  
// console.log(esseAno);
// console.log(proximoAno);

//----------

// // exemplo de array (listas ordenadas)
// var array1 = ["gato","cachorro","periquito"];
// var array2 = ["elefante","girafa","refrigerante"];
// console.log(array1);
// console.log(array2)

//----------

// var spacer = {
//     blank: function () {
//       return "";
//     },
  
//     newLine: function () {
//       return "\n";
//     },
  
//     line: function (length, character) {
//       var longString = "****************************************".repeat(2);
//       longString += "----------------------------------------".repeat(2);
//       longString += "========================================".repeat(2);
//       longString += "++++++++++++++++++++++++++++++++++++++++".repeat(2);
//       longString += "                                        ".repeat(2);
  
//       length = Math.max(0, length);
//       length = Math.min(80, length);
//       return longString.substr(longString.indexOf(character), length);
//     },
    
//     wrap : function (text, length, character) {
//       var padLength = length - text.length - 3;
//       var wrapText = character + " " + text;      
//       wrapText += spacer.line(padLength, " ");
//       wrapText += character;
//       return wrapText;
//     },
  
//     box: function (text, length, character) {
//       var boxText = spacer.newLine();
//       boxText += spacer.line(length, character) + spacer.newLine();
//       boxText += spacer.wrap(text, length, character) + spacer.newLine(); 
//       boxText += spacer.line(length, character) + spacer.newLine();
//       return boxText;
//     }
//   };
  
//   var getPlayerName = function (player) {
//     return player.name;
//   };
  
//   var getPlayerHealth = function (player) {
//     return player.name + " está com " + player.HP + " HP.";
//   };
  
//   var getPlayerPlace = function (player) {
//     return player.name + " está em " + player.place;
//   };
//   var getPlayerClasse = function (player) {
//       return player.name + " é um(a) " + player.classe;
//   };
//   var getPlayerItems = function (player) {
//       return player.name + " possui esses items: " + player.items;
//   };
  
//   var getPlayerInfo = function (player, character) {  
//     var place = getPlayerPlace(player);
//     var health = getPlayerHealth(player);
//     var classe = getPlayerClasse(player);
//     var items = getPlayerItems(player);
//     var longest = Math.max(place.length, items.length) + 4;
      
//     var info = spacer.box(getPlayerName(player), longest, character);
//     info += spacer.wrap(place, longest, character);
//     info += spacer.newLine() + spacer.wrap(health, longest, character);
//     info += spacer.newLine() + spacer.wrap(classe, longest, character);
//     info += spacer.newLine() + spacer.wrap(items, longest, character);  
//     info += spacer.newLine() + spacer.line(longest, character);
  
//     return info;
//   };
  
//   var player1 = {
//       name: "Leo",
//       classe: "Feiticeiro",
//       place: "Torre do desespero",
//       items: "celular, computador e oculos",
//       HP: 100
//   };
//   var player2 = {
//       name: "Nicolly",
//       classe: "Barbara",
//       place: "Casa dos elfos caolhos",
//       items: "espatula, panela e celular",
//       HP: 80
//   };
  
//   console.log(getPlayerInfo(player1, "="));
//   console.log(getPlayerInfo(player2, "+"));

//----------

// var spacer = {
//     blank: function () {
//       return "";
//     },
  
//     newLine: function () {
//       return "\n";
//     },
  
//     line: function (length, character) {
//       var longString = "****************************************";
//       longString += "----------------------------------------";
//       longString += "========================================";
//       longString += "++++++++++++++++++++++++++++++++++++++++";
//       longString += "                                        ";
  
//       length = Math.max(0, length);
//       length = Math.min(40, length);
//       return longString.substr(longString.indexOf(character), length);
//     },
    
//     wrap : function (text, length, character) {
//       var padLength = length - text.length - 3;
//       var wrapText = character + " " + text;      
//       wrapText += spacer.line(padLength, " ");
//       wrapText += character;
//       return wrapText;
//     },
  
//     box: function (text, character) {
//       var boxText = spacer.newLine();
//       var length = text.length;
//       boxText += spacer.line(length+4, character) + spacer.newLine();
//       boxText += character + spacer.line(length+2, " ") + character + spacer.newLine();
//       boxText += spacer.wrap(text, length+4, character) + spacer.newLine();
//         boxText += character + spacer.line(length+2, " ") + character + spacer.newLine();
//       boxText += spacer.line(length+4, character) + spacer.newLine();
//       return boxText;
//     }
//   };
  
//   console.log(spacer.box("Isso só funciona para str de ate 40", "="));
//   console.log(spacer.box("Mars", "*"));

//----------

// var planet = "Jupiter";
// var bigPlanet = planet.toUpperCase();
// var getBig = function (text){
//     text = text.toUpperCase();
//     return text;
// };
// var getSmall = function (text){
//     return console.log(text + " becomes " + text.toLowerCase());
// };
// console.log(planet + " becomes " + bigPlanet);
// console.log(getBig("leonardo"));
// getSmall("SUPIMPA");


//----------

// var line = function (lineLength) {
//     var line = "========================================";
//     lineLength = Math.max(0, lineLength);
//     lineLength = Math.min(40, lineLength);
//     return line.substr(0, lineLength);
//   };
  
//   var spaceLine = function (lineLength) {
//     var line = "                                        ";
//     lineLength = Math.max(0, lineLength);
//     lineLength = Math.min(40, lineLength);
//     return line.substr(0, lineLength);
//   };
  
  
//   var emptyBox = function (boxLength) {
//     var line = "========================================";
//     var space = "                                        ";
//     var num = 2;
//     boxLength = Math.max(0, boxLength);
//     boxLength = Math.min(40, boxLength);
//     return line.substr(0, boxLength) + "\n=" + space.substr(0, boxLength - num) + "=\n=" + space.substr(0, boxLength - num) + "=\n=" +  space.substr(0, boxLength - num) + "=\n=" + line.substr(0, boxLength);
//   };
  
//   console.log(line(30));
//   console.log(line(40));
//   console.log(spaceLine(50) + "home");
//   console.log(emptyBox(60));

//----------

// var espaco;

// espaco.newLine = function (){
//     return "\n";
// };
// espaco.blank = function(){
//     return "";
// };
//                  // ou pode-se fazer deste outro jeito
// espaco = {
//     newLine : function () {return "\n";},
//     blank : function () {return "";},
// };
//                 // Para demonstrar: 
// console.log("Linha 1");
// espaco.newLine();
// espaco.blank();
// console.log("Linha 2");

//----------

// var point1;
// var point2;
// var move;
// var showPoint;
// var reflectX;
// var rotate;

// rotate = function (point) {
//     spam = {
//         x : -point.y, 
//         y : point.x
//     };
//    return point = {
//         x : spam.x,
//         y : spam.y
//     };
// };

// reflectX = function (point) {
//     return {
//         x : -point.x,
//         y : point.y
//     };
// };
// move = function (point, change) {
//     return {
//         x: point.x + change.x,
//         y: point.y + change.y
//     };
// };

// showPoint = function (point) {
//     console.log("( " + point.x + " , " + point.y + " )");
// };

// point1 = { x : 2, 
//           y : 5 
//          };

// point2 = move(point1, { x : 7, y : -6 });

// showPoint(point1);
// console.log("Move 7 across and 6 down: ");
// showPoint(point2);
// console.log("Reflecting the second point in the x-axis: ");
// point2 = reflectX(point2);
// showPoint(point2);
// console.log("Rotating the reflected point by 90 degrees: ");
// point2 = rotate(point2);
// showPoint(point2);

//----------

// var planet1 = { name: "Jupiter", radius: 69911 };

// var calculateSizes = function (planet) {
//     var r = planet.radius;
//     planet.diameter = 2 * r;
//     planet.area = 4 * 3.142 * r * r;
//     planet.volume = 4 * 3.142 * r * r * r / 3;
// };

// var displaySizes = function (planet) {
//     console.log(planet.name);
//     console.log("diameter = " + planet.diameter + " km");
//     console.log("surface area = " + planet.area + " square km");
//     console.log("volume = " + planet.volume + " cubic km");
// };

// calculateSizes(planet1);
// displaySizes(planet1);

//----------

// var planet1;
// var getPlanetInfo;
// var planet2;

// planet1 = {
//     name: "Jupiter",
//     position: 5,
//     type: "Gas Giant",
//     radius: 69911,
//     sizeRank: 1
// };
// planet2 = {
//     name: "Xuxa",
//     position: 666,
//     type: "Fun house",
//     radius: 666000,
//     sizeRank: 69
// };

// getPlanetInfo = function (planet) {
//     return planet.name + ": planet number " + planet.position + ", " + planet.type + ", " + planet.radius + "km of radius, size Rank no. " + planet.sizeRank;
// };

// console.log(getPlanetInfo(planet1));
// console.log(getPlanetInfo(planet2));

//----------

// var player = {
//     name : ["Leo","Nicolly"],
//     place : ["Tower of Doom","Sisters of Fate"],
//     HP : [50,70],
//     items: ["A bottle of wine, one dirty sock","One pearl necklace, one sticky finger"],
// };

// var getLine = function () {
//     return "==============================";
// };
// var getName = function (name) {
//     return name;
// };
// var getLocation = function (name, location) {
//     return name + " is in the " + location;
// };
// var getHP = function (name, HP) {
//     return name + " has " + HP + " HitPoints";
// };
// var getItems = function (name, items) {
//     return name + " has these items: " + items; 
// };
// var playerInfo = function (name, place, HP, items) {
//     var playerInfo = name;
//     playerInfo += "\n" + getLine();
//     playerInfo += "\n" + getLocation(name, place);
//     playerInfo += "\n" + getHP(name,HP);
//     playerInfo += "\n" + getItems(name, items);
//     playerInfo += "\n" + getLine();
//     playerInfo += "\n";
//     return playerInfo;
// };

// console.log(playerInfo(player.name[0], player.place[0], player.HP[0], player.items[0]));
// console.log(playerInfo(player.name[1], player.place[1], player.HP[1], player.items[1]));

//----------

// var player1 = {
//     name : "Leo",
//     place : "Tower of Doom",
//     HP : 50,
//     items: "A bottle of wine, one dirty sock"
// };
// var player2 = {
//     name : "Nicolly",
//     place : "Sisters of Fate",
//     HP : 50,
//     items: "One pearl necklace, one sticky finger"
// };

// var getLine = function () {
//     return "==============================";
// };
// var getName = function (name) {
//     return name;
// };
// var getLocation = function (name, location) {
//     return name + " is in the " + location;
// };
// var getHP = function (name, HP) {
//     return name + " has " + HP + " HitPoints";
// };
// var getItems = function (name, items) {
//     return name + " has these items: " + items; 
// };
// var playerInfo = function (name, place, HP, items) {
//     var playerInfo = name;
//     playerInfo += "\n" + getLine();
//     playerInfo += "\n" + getLocation(name, place);
//     playerInfo += "\n" + getHP(name,HP);
//     playerInfo += "\n" + getItems(name, items);
//     playerInfo += "\n" + getLine();
//     playerInfo += "\n";
//     return playerInfo;
// };

// console.log(playerInfo(player1.name, player1.place, player1.HP, player1.items));
// console.log(playerInfo(player2.name, player2.place, player2.HP, player2.items));

//----------

// var add;
// var sum;
// add = function (number1, number2, number3) {
// 	var total = number1 + number2 + number3;

// 	return "The sum of " + number1 + " and " + number2 + " and " + number3 + " is " + total;
// };

// sum = add(23,50,34);
// console.log(sum)

//----------

// var getMyMessage;
// getMyMessage = function (message){
//     return message
// }

//----------

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

//----------

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

//----------

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

//----------

// var showMessage;
// message = "oi meu nome é bruce!";
// showMessage = function (message, message2, message3) {
// 	console.log("A mensagem no.1 é: " + message);
//     console.log("A mensagem no.2 é: " + message2);
//     console.log("A mensagem no.3 é: " + message3);
// };

// showMessage("testando 1, 2...", "Aparentemente funcionou", "Sou um genio da computacao");
// console.log(message);

//----------

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

//----------

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

//----------

// function total (a, b) {
//     resultado = a + b;
//     console.log (resultado);
// };
// total(10, 10);
// console.log (resultado);

//----------

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

//----------

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

//----------

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

//----------

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