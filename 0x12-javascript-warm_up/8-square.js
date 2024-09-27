#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    const line = 'X'.repeat(size);
    console.log(line);
  }
} else {
  console.log('Missing size');
}
