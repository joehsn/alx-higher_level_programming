#!/usr/bin/node

const args = process.argv.slice(2); // Get arguments except script name

if (args.length === 0) {
  console.log(0); // No arguments
} else if (args.length === 1) {
  console.log(0); // Only one argument
} else {
  // Convert arguments to integers
  const numbers = args.map(Number);

  // Find the two largest numbers
  let firstMax = -Infinity;
  let secondMax = -Infinity;

  for (const num of numbers) {
    if (num > firstMax) {
      secondMax = firstMax;
      firstMax = num;
    } else if (num > secondMax && num !== firstMax) {
      secondMax = num;
    }
  }

  console.log(secondMax); // Print the second-biggest
}
