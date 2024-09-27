#!/usr/bin/node

// Define a function to increment a number and call another function
exports.addMeMaybe = function (number, theFunction) {
  const incrementedNumber = number + 1;
  theFunction(incrementedNumber);
};
