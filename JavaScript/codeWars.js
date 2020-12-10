//----------

// //recursive sum of array of numbers
// function digital_root(n) {
//   n += '';
//   n = n.split('') // create array of strings
//   var sum = 0
//   for (let i = 0; i < n.length; i++) {
//     n[i] = parseInt(n[i], 10) //turns each element of the array into Int
//   }
//   for (item of n) {
//     sum += item; //add element to sum
//     if (sum > 9) { //if sum > 10, execute digital_root again using sum
//       sum = digital_root(sum)
//     }
//   }
//   return sum;
// }

//----------
// function binaryArrayToNumber(arr){
//   var result = 0;
//   var size = arr.length
//   var counter = 0;
//   for (let i = arr.length-1; i >= 0; i--){
//     result += arr[i]*(2**counter)
//     counter++
//   }
//   return result
// }

// binaryArrayToNumber([0,0,0,1])

//----------
// function getCount(str) {
//     var vowelsCount = 0;
//     var vowels = ["a", "e", "i", "o", "u"]
//     for (var i = 0; i <= str.length; i++){
//       if (vowels.includes(str[i])){
//           vowelsCount += 1;
//       }
//     }
//       return vowelsCount;
//   }
  
//   console.log(getCount('testando dois'))
  //----------
  // function descendingOrder(n){
  //     n = n + "";
  //     n = n.split("");
  //     n = n.sort();
  //     n = n.reverse();
  //     return n;
  //   }
    
  //   var list = 456123;
  //   console.log(descendingOrder(list));