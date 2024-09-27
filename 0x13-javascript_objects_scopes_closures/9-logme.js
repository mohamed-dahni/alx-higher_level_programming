#!/usr/bin/node

let numberOfArguments = 0;

/**
 * logMe : function that prints the number of arguments already
 * printed and the new argument value
 */
exports.logMe = function (item) {
  console.log(`${numberOfArguments}: ${item}`);
  numberOfArguments++;
};
