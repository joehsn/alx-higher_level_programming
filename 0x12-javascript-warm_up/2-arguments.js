#!/usr/bin/node

const args = process.argv.slice(2); // Get command-line arguments except the script name

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
