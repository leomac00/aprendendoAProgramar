//----------

//  //Demonstração de imutabilidade
//  const students = [{
//     name: 'Leo',
//     grade: 10
//   },
//   {
//     name: 'Nicolly',
//     grade: 6
//   },
// ];

// function getApproved(studentList) {
//   return studentList.filter(student => student.grade >= 7);
// }

// console.log('Lista de alunos aprovados:');
// console.log(getApproved(students));

// console.log('\nLista de todos os alunos:');
// console.log(students); // Perceba que a lista de estudantes original não é alterado após aplicar a função

//----------

// //Aplicação do Currying:
// function soma(a, b){
// 	return a + b;
// }

// soma(2, 3); 
// soma(2, 4);
// soma(2, 5);
// soma(2, 6); //Perceba que o primeiro parâmetro é igual em todas as chamadas

// //Aplicando Currying poderiamos fazer o seguinte:
// const soma2 = soma(2);
// soma2(3);
// soma2(4);
// soma2(5);
// soma2(6); //Perceba que agora só foi neceário digitar um parâmetro