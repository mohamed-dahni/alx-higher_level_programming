#!/usr/bin/node

// Define a function to compute factorial recursively
const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    // Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1);
  }
};

const arg = parseInt(process.argv[2]);

console.log(factorial(arg));
