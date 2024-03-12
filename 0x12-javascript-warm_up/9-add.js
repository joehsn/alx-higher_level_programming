#!/usr/bin/node

function add (a, b) {
  return a + b; // Add the arguments and return the result
}

const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

if (isNaN(firstArg) || isNaN(secondArg)) {
  console.log('NaN'); // Print NaN for non-numeric arguments
} else {
  console.log(add(firstArg, secondArg)); // Call the function to add and print the result
}
