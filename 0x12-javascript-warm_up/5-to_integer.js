#!/usr/bin/node

const firstArg = process.argv[2];

if (isNaN(parseInt(firstArg))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(firstArg)}`);
}
