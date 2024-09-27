#!/usr/bin/node

/**
 * Extract the list of arguments (excluding the first two,
 * which are node and the script filename)
 */
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  // Convert arguments to integers
  const numbers = args.map(arg => parseInt(arg));
  numbers.sort((a, b) => b - a); // Sort in des order
  console.log(numbers[1]);
}
