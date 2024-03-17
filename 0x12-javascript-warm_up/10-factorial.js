#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1; // Factorial of NaN or 0 is 1
  } else {
    return n * factorial(n - 1); // Recursive call for factorial calculation
  }
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
