#!/usr/bin/node

let argumentCount = 0; // Keeps track of the number of arguments printed

exports.logMe = function (item) {
  console.log(`${argumentCount}: ${item}`);
  argumentCount++; // Increment after printing
};
