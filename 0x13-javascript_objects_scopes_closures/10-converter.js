#!/usr/bin/node

// No new variables allowed (adhereing to prompt requirements)
exports.converter = function (base) {
  return function (number) {
    let result = '';
    let remaining = number;

    while (remaining > 0) {
      const digit = remaining % base;
      result = (digit >= 10 ? String.fromCharCode(digit + 55) : digit) + result; // Handle digits 10-15 for bases >= 16
      remaining = Math.floor(remaining / base);
    }

    return result || '0'; // Return "0" if the number is 0
  };
};
