// prime number checker 


// function isPrime(num){
//     if (num <= 1) {
//         return false
//     }
//     for (let index = 2; index < num; index++) {
//        if (num % index === 0) {
//         return false
//        }
//     }
//     return true
// }

// console.log(isPrime(7)) 


// =========================================


// function isEven(num){
//     if(num % 2 === 0){
//         return true
//     }else{
//         return false
//     }
// }
// console.log(isEven(2)) 


// function isOdd(num){
//     if(num % 2 === 0){
//         console.log("Even Number")
//     }else{
//         console.log("Odd Number")
//     }
// }
// isOdd(89)


// ==============================

// check palindrome

function palindrome(str){
    return str.split("").reverse().join("")
}


console.log(palindrome("usama"))