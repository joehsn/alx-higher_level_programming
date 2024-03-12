#!/usr/bin/node

const firstArg = process.argv[2]; // Access the second element of process.argv

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
